from manimlib import *
from typing import List, Tuple, Union

def tex_typing_animate(
        self: Scene, 
        tex: Union[Tex, Text], 
        typing_interval: float = 0.1, 
        underline_len: float = 0.25, 
        underline_height: float = 0.05,
        blinking_interval: float = 1,
    ):
    # participate the tex
    tex_parts = [char for char in tex]

    # Underline
    blink_opacity = lambda: 1 if (self.time % blinking_interval) < (blinking_interval / 2) else 0
    underline_rec = Rectangle(width=underline_len, height=underline_height, color=WHITE, fill_opacity=1).set_fill(WHITE, opacity=1)
    underline_rec.add_updater(
        lambda line: line.set_opacity(blink_opacity())
    )
    self.add(underline_rec)

    # Positions
    pos = tex.get_center()
    pos_up = tex.get_top()
    pos_down = tex.get_bottom()
    height = np.linalg.norm(pos_up - pos_down)

    # Typing
    for i in range(len(tex_parts)):
        # get the position of the part
        current_tex_group = VGroup(*[part.copy().move_to(part.get_center()) for part in tex_parts[:i+1]])
        current_tex_group.move_to(pos)

        underline_rec.next_to(current_tex_group, RIGHT, buff=0.1)
        underline_rec.shift(DOWN * (height / 2 - underline_height / 2))
        
        self.add(current_tex_group)
        self.wait(typing_interval)
        self.remove(current_tex_group)
    
    underline_rec.clear_updaters()
    self.remove(underline_rec)
    self.add(tex)

def animate_scaling_exponential_decay(init_current: float, t: float, duration: float, half_life: float, max_vec: float = 0.01, zoom_direction: str = "in"):
    walk = t - init_current
    if walk > duration or walk < 0:
        zoom = 1
    elif zoom_direction == "in":
        zoom = 1 - max_vec * (1 - exponential_decay(walk / duration, half_life / duration))
    elif zoom_direction == "out":
        zoom = 1 + max_vec * (1 - exponential_decay(walk / duration, half_life / duration))
    return zoom

def animate_scaling_smooth(init_current: float, t: float, duration: float, max_vec: float = 0.01, zoom_direction: str = "in"):
    walk = t - init_current
    if walk > duration or walk < 0:
        zoom = 1
    elif zoom_direction == "in":
        zoom = 1 - max_vec * (1 - smooth(walk / duration))
    elif zoom_direction == "out":
        zoom = 1 + max_vec * (1 - smooth(walk / duration))
    return zoom

def animate_scaling_linear(init_current: float, t: float, duration: float, max_vec: float = 0.01, zoom_direction: str = "in"):
    walk = t - init_current
    if walk > duration or walk < 0:
        zoom = 1
    elif zoom_direction == "in":
        zoom = 1 - max_vec * (1 - (walk / duration))
    elif zoom_direction == "out":
        zoom = 1 + max_vec * (1 - (walk / duration))
    return zoom

def animate_shift_smooth(init_current: float, t: float, duration: float, max_vec: float = 0.01, shift_direction: str = "pos"):
    walk = t - init_current
    if walk > duration or walk < 0:
        shift = 0
    elif shift_direction == "neg":
        shift = 0 - max_vec * (1 - smooth(walk / duration))
    elif shift_direction == "pos":
        shift = 0 + max_vec * (1 - smooth(walk / duration))
    return shift

def homotopic_showin(x: float, y: float, z: float, t: float) -> List[float]:
    # can be use with FadeIn
    scaling_const = 0.4
    init_scaling = 0.1

    scaling = lambda theta: abs(np.sin(2 * theta)) * scaling_const * (1 - t) + 1
    theta = np.atan2(y, x)
    mutiplier = (1 + init_scaling * (1 - t)) * scaling(theta)
    return [x * mutiplier, y * mutiplier, z]

def transformMatchingIndex(mob1: Union[Tex, Text, VGroup], mob2: Union[Tex, Text, VGroup], map_index: Tuple[List[int]], transform_type: Union[ReplacementTransform, TransformMatchingShapes, TransformMatchingTex] = ReplacementTransform) -> List[Animation]:
    """
    Transform Matching Index
    
    For all submobs in mob1, if the indexes are not in map_index[0], then the submob will be FadeOut. If the target indexes are not in map_index[1], then the submob will be FadeIn.
    """
    # Check if the map_index is a tuple of two lists
    if not isinstance(map_index, tuple) or len(map_index) != 2 or not all(isinstance(i, list) for i in map_index):
        raise ValueError("map_index must be a tuple of two lists")
    
    # Check if the indexes in map_index are valid
    for i in map_index[0]:
        if i >= len(mob1):
            raise ValueError(f"Index {i} is out of range for mob1")
    for i in map_index[1]:
        if i >= len(mob2):
            raise ValueError(f"Index {i} is out of range for mob2")
    
    animations = []
    # FadeOut the submobs in mob1 that are not in map_index[0]
    for i in range(len(mob1)):
        if i not in map_index[0]:
            animations.append(FadeOut(mob1[i]))
    
    # FadeIn the submobs in mob2 that are not in map_index[1]
    for i in range(len(mob2)):
        if i not in map_index[1]:
            animations.append(FadeIn(mob2[i]))

    # TransformMatchingShapes for any mapping
    TransformAni = transform_type
    maps = [(mob1[i], mob2[j]) for i, j in zip(map_index[0], map_index[1])]
    for i, j in maps:
        animations.append(TransformAni(i, j))

    return animations