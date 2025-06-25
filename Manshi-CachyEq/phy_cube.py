import pybullet as p
import pybullet_data
import numpy as np
import time
from typing import Dict, Any, Tuple, List

# Define shape types for convenience
SHAPE_TYPE_BOX = p.GEOM_BOX
SHAPE_TYPE_PLANE = p.GEOM_PLANE

class ManimPybulletSimulator:
    """
    A wrapper around PyBullet for integration with Manim scenes.
    Manages the physics simulation and provides body states in Manim coordinates.
    """
    def __init__(self, sim_time_step: float = 1.0/240.0, gravity: List[float] = [0, 0, -9.8]):
        """
        Initializes the PyBullet simulator.

        Args:
            sim_time_step: The time step for PyBullet simulation (e.g., 1/240 for 240Hz).
            gravity: The gravity vector [gx, gy, gz] in PyBullet's Z-up coordinate system.
        """
        # Connect to the physics server in DIRECT mode (no GUI) [6][13]
        self.physicsClient = p.connect(p.DIRECT)
        if self.physicsClient < 0:
             raise RuntimeError("Failed to connect to PyBullet physics server.")

        # Set gravity [2]
        p.setGravity(gravity[0], gravity[1], gravity[2]) # PyBullet uses Z-up by default

        self.sim_time_step = sim_time_step
        self._current_pb_time = 0.0 # Tracks the total simulated time in PyBullet

        # Dictionary to store information about bodies: {name: {pb_id, shape_type, ...}}
        self._bodies: Dict[str, Dict[str, Any]] = {}
        self._body_counter = 0 # Counter for generating unique names if none provided

        # PyBullet (x, y, z) is Z-up. Manim (x, y, z) is Y-up (for 3D).
        # Transformation: PB(x, y, z) -> Manim(x, z, -y)
        # PyBullet quaternion (x, y, z, w) -> Manim quaternion (x, z, -y, w)
        # Note: Quaternion transformation needs care, this is a simple axis swap.
        self._pb_to_manim_matrix = np.array([
            [1, 0, 0],
            [0, 0, 1],
            [0, -1, 0]
        ])

    def _pb_pos_to_manim(self, pos_pb: Tuple[float, float, float]) -> np.ndarray:
        """Converts PyBullet position (Z-up) to Manim position (Y-up)."""
        return np.dot(self._pb_to_manim_matrix, np.array(pos_pb))

    def _pb_quat_to_manim(self, quat_pb: Tuple[float, float, float, float]) -> np.ndarray:
        """Converts PyBullet quaternion (x, y, z, w) to Manim quaternion (x, z, -y, w)."""
        # PyBullet quaternion is (x, y, z, w)
        # Manim quaternion is (x, y, z, w) but axes are different
        # Simple swap for Z-up to Y-up: (x, y, z, w)_pb -> (x, z, -y, w)_manim
        return np.array([quat_pb[0], quat_pb[2], -quat_pb[1], quat_pb[3]])

    def _manim_pos_to_pb(self, pos_manim: np.ndarray) -> Tuple[float, float, float]:
        """Converts Manim position (Y-up) to PyBullet position (Z-up)."""
        # Inverse transformation: Manim(x, y, z) -> PB(x, z, -y)
        # Inverse matrix is its transpose for orthogonal matrices
        inv_matrix = self._pb_to_manim_matrix.T
        return tuple(np.dot(inv_matrix, pos_manim))

    def _manim_quat_to_pb(self, quat_manim: np.ndarray) -> Tuple[float, float, float, float]:
        """Converts Manim quaternion (x, y, z, w) to PyBullet quaternion (x, -z, y, w)."""
        # Inverse swap: (x, y, z, w)_manim -> (x, -z, y, w)_pb
        return tuple([quat_manim[0], -quat_manim[2], quat_manim[1], quat_manim[3]])


    def add_body(self,
                 name: str = None,
                 shape_type: int = SHAPE_TYPE_BOX,
                 size: List[float] = [0.5, 0.5, 0.5], # halfExtents for BOX, ignored for PLANE
                 mass: float = 1.0, # 0 for static
                 initial_pos_manim: np.ndarray = np.array([0, 0, 0]), # Manim coordinates
                 initial_quat_manim: np.ndarray = np.array([0, 0, 0, 1]), # Manim quaternion (x,y,z,w)
                 restitution: float = 0.1, # Bounce factor
                 color: List[float] = [0.5, 0.5, 0.5, 1.0] # RGBA color for visual shape
                ) -> str:
        """
        Adds a rigid body to the simulation.

        Args:
            name: A unique name for the body. If None, a name is generated.
            shape_type: The PyBullet shape type (e.g., SHAPE_TYPE_BOX, SHAPE_TYPE_PLANE).
            size: Size parameters for the shape (e.g., halfExtents for BOX).
            mass: Mass of the body. Use 0 for static objects (like walls/ground).
            initial_pos_manim: Initial position in Manim's Y-up coordinates.
            initial_quat_manim: Initial orientation as a quaternion in Manim's Y-up orientation.
            restitution: The restitution coefficient for collisions.
            color: RGBA color for the visual representation (used by PyBullet GUI, good practice).

        Returns:
            The unique name assigned to the body.
        """
        if name is None:
            name = f"body_{self._body_counter}"
            self._body_counter += 1
            while name in self._bodies: # Ensure uniqueness
                 name = f"body_{self._body_counter}"
                 self._body_counter += 1

        if name in self._bodies:
            print(f"Warning: Body with name '{name}' already exists. Overwriting.")
            self.remove_body(name) # Remove existing body before adding new one

        # Convert initial position and orientation from Manim to PyBullet coordinates
        initial_pos_pb = self._manim_pos_to_pb(initial_pos_manim)
        initial_quat_pb = self._manim_quat_to_pb(initial_quat_manim)

        # Create collision shape
        if shape_type == SHAPE_TYPE_BOX:
            collision_shape_id = p.createCollisionShape(shapeType=shape_type, halfExtents=size)
        elif shape_type == SHAPE_TYPE_PLANE:
             collision_shape_id = p.createCollisionShape(shapeType=shape_type)
        else:
            raise ValueError(f"Unsupported shape type: {shape_type}")

        # Create visual shape (optional in DIRECT mode, but good for debugging with GUI)
        if shape_type == SHAPE_TYPE_BOX:
             visual_shape_id = p.createVisualShape(shapeType=shape_type, halfExtents=size, rgbaColor=color)
        elif shape_type == SHAPE_TYPE_PLANE:
             # Planes don't typically have visual shapes this way, can use a box or other visual
             # For simplicity, we'll skip visual shape for plane here, Manim handles visualization
             visual_shape_id = -1 # No visual shape
        else:
             visual_shape_id = -1 # No visual shape

        # Create the multibody
        pb_id = p.createMultiBody(baseMass=mass,
                                  baseCollisionShapeIndex=collision_shape_id,
                                  baseVisualShapeIndex=visual_shape_id,
                                  basePosition=initial_pos_pb,
                                  baseOrientation=initial_quat_pb)

        # Set dynamics properties
        p.changeDynamics(pb_id, -1, restitution=restitution) # -1 refers to the base link

        # Store body information
        self._bodies[name] = {
            'pb_id': pb_id,
            'shape_type': shape_type,
            'size': size,
            'mass': mass,
            'restitution': restitution,
            'color': color,
            # Store initial state in Manim coords for reference if needed
            'initial_pos_manim': initial_pos_manim,
            'initial_quat_manim': initial_quat_manim
        }

        return name

    def remove_body(self, name: str):
        """
        Removes a body from the simulation.

        Args:
            name: The unique name of the body to remove.
        """
        if name not in self._bodies:
            print(f"Warning: Body with name '{name}' not found.")
            return

        pb_id = self._bodies[name]['pb_id']
        p.removeBody(pb_id)
        del self._bodies[name]

    def update_simulation(self, current_manim_time: float):
        """
        Steps the PyBullet simulation forward to match the current Manim time.

        Args:
            current_manim_time: The current time elapsed in the Manim animation (self.time).
        """
        # Step the simulation until the PyBullet time catches up to the Manim time
        # Use a small tolerance to avoid infinite loops due to floating point inaccuracies
        while self._current_pb_time < current_manim_time - 1e-6:
            p.stepSimulation()
            self._current_pb_time += self.sim_time_step

        # Ensure we don't overshoot significantly if Manim time jumps
        self._current_pb_time = min(self._current_pb_time, current_manim_time)


    def get_states(self) -> Dict[str, Dict[str, Any]]:
        """
        Gets the current state (position and orientation) of all active bodies.

        Returns:
            A dictionary mapping body names to their state in Manim coordinates:
            {name: {'pos': np.ndarray, 'quat': np.ndarray}}
        """
        states: Dict[str, Dict[str, Any]] = {}
        for name, body_info in self._bodies.items():
            pb_id = body_info['pb_id']
            try:
                pos_pb, orn_pb = p.getBasePositionAndOrientation(pb_id)
                # Convert to Manim coordinates
                pos_manim = self._pb_pos_to_manim(pos_pb)
                quat_manim = self._pb_quat_to_manim(orn_pb)
                states[name] = {'pos': pos_manim, 'quat': quat_manim}
            except p.error as e:
                 # Handle cases where a body might have been removed externally or is invalid
                 print(f"Warning: Could not get state for body '{name}' (ID: {pb_id}). It might have been removed. Error: {e}")
                 # Optionally remove from internal tracking if it's truly gone
                 # del self._bodies[name] # Be cautious with modifying dict during iteration if not careful
                 pass # Just skip this body for this frame

        return states

    def disconnect(self):
        """Disconnects from the PyBullet physics server."""
        if self.physicsClient >= 0:
            p.disconnect()
            self.physicsClient = -1 # Mark as disconnected
            print("PyBullet simulator disconnected.")

    def __del__(self):
        """Ensure disconnection when the object is garbage collected."""
        self.disconnect()

# --- Example Manim Scene using the Simulator ---
# Save this part in a separate file, e.g., cube_drop_scene.py
