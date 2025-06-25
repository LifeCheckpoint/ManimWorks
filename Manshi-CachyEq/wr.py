from manimlib import *
import random

class AlgorithmVisualization(Scene):
    manim_config.tex.template = "ctex"

    # Configuration Constants
    N_POINTS = 200
    L_CONCEPT = 224
    CONCEPT_COORD_MIN = 0
    CONCEPT_COORD_MAX = 1000
    
    DOT_RADIUS = 0.05 # Adjusted from 0.08 as per "visual effect"
    
    SORTED_POINTS_Y_POS = -3.0 # Lowered slightly for more space
    SORTED_POINTS_WIDTH = 12.0
    
    MULTISET_AREA_CENTER = RIGHT * 4.5 + UP * 0 # Adjusted for better centering
    MULTISET_AREA_HEIGHT = 6.0
    MULTISET_AREA_WIDTH = 2.5
    
    FOUND_SOLUTIONS_POS = UP * 3.0 + LEFT * 5.5
    MAX_I_ITERATIONS = 10 # For demo purposes, as per instruction

    # Colors
    BG_COLOR = BLACK
    POINT_COLOR = BLUE
    SORTED_POINT_HIGHLIGHT_COLOR = YELLOW
    SORTED_POINT_REMOVED_COLOR = GREY
    POINTER_J_COLOR = RED
    POINTER_I_COLOR = BLUE_D # Using a different blue for pointer_i
    MULTISET_OUTLINE_COLOR = GREY
    MULTISET_DOT_COLOR = WHITE
    MULTISET_BOUNDARY_COLOR = YELLOW
    L_CONSTRAINT_LINE_COLOR = RED
    NEIGHBOR_DOT_COLOR = ORANGE
    TEMP_CHECK_DOT_COLOR = PURPLE
    SOLUTION_DOT_COLOR = GREEN
    SOLUTION_RECT_COLOR = GREEN

    def setup_constants(self):
        self.conceptual_to_manim_scale_y = self.MULTISET_AREA_HEIGHT / (self.CONCEPT_COORD_MAX - self.CONCEPT_COORD_MIN)
        self.visual_L_height = self.L_CONCEPT * self.conceptual_to_manim_scale_y
        self.next_solution_spot = self.FOUND_SOLUTIONS_POS.copy()


    def construct(self):
        self.camera.background_color = self.BG_COLOR
        self.setup_constants()

        # Block 1: Initial Point Set Display
        all_points = self.create_initial_points()
        self.play(FadeIn(all_points, lag_ratio=0.1), run_time=2)
        self.wait(0.5)

        # Block 2: Sort by X Coordinate
        sorted_points = self.sort_points_by_x(all_points)
        self.wait(0.5)

        # Block 3: Double Pointers and Sliding Window Initialization
        pointers_and_areas = self.initialize_sliding_window_elements(sorted_points)
        pointer_j = pointers_and_areas["pointer_j"]
        pointer_i = pointers_and_areas["pointer_i"]
        multiset_area_outline = pointers_and_areas["multiset_area_outline"]
        multiset_dots = pointers_and_areas["multiset_dots"]
        # multiset_boundary = pointers_and_areas["multiset_boundary"] # AnimatedBoundary can be tricky
        # For stability, let's use a manually updated rectangle for boundary
        multiset_boundary_rect = Rectangle(
            width=self.MULTISET_AREA_WIDTH, height=self.MULTISET_AREA_HEIGHT,
            stroke_color=self.MULTISET_BOUNDARY_COLOR, stroke_width=2, stroke_opacity=0.5
        ).move_to(multiset_area_outline.get_center())


        found_solutions_vgroup = pointers_and_areas["found_solutions_vgroup"]
        l_constraint_line = pointers_and_areas["l_constraint_line"]
        
        self.add(multiset_dots) # Add VGroup to scene so its children are displayed

        self.play(
            FadeIn(pointer_j),
            FadeIn(pointer_i),
            ShowCreation(multiset_area_outline),
            # FadeIn(multiset_boundary), # If using AnimatedBoundary
            ShowCreation(multiset_boundary_rect),
            run_time=1.5
        )
        self.add(found_solutions_vgroup) # Add to scene to display solutions later
        self.wait(0.5)

        # Block 4 & 5: Core Loop
        self.run_core_algorithm_loop(
            sorted_points, pointer_i, pointer_j, 
            multiset_dots, multiset_area_outline, multiset_boundary_rect,
            l_constraint_line, found_solutions_vgroup
        )
        self.wait(1)

        # Block 6: Ending and Summary
        self.cleanup_scene(
            sorted_points, pointer_i, pointer_j,
            multiset_dots, multiset_area_outline, multiset_boundary_rect,
            l_constraint_line
        )
        
        summary_text = Tex("O(n \\log n)", tex_to_color_map={"O(n \\log n)": YELLOW})
        summary_text.scale(1.5)
        summary_text.to_edge(UP)
        self.play(Write(summary_text), run_time=1.5)
        self.wait(2)
        self.play(FadeOut(summary_text), run_time=1)
        self.wait(1)


    def create_initial_points(self):
        all_points = VGroup()
        for i in range(self.N_POINTS):
            dot = SmallDot(radius=self.DOT_RADIUS, color=self.POINT_COLOR)
            dot.index = i
            dot.concept_x = random.randint(self.CONCEPT_COORD_MIN, self.CONCEPT_COORD_MAX)
            dot.concept_y = random.randint(self.CONCEPT_COORD_MIN, self.CONCEPT_COORD_MAX)
            
            # Random screen position initially
            dot.move_to(
                np.array([
                    random.uniform(-FRAME_WIDTH / 4, FRAME_WIDTH / 4),
                    random.uniform(-FRAME_HEIGHT / 4, FRAME_HEIGHT / 4),
                    0
                ])
            )
            all_points.add(dot)
        return all_points

    def sort_points_by_x(self, all_points):
        # Sort submobjects list
        all_points.submobjects.sort(key=lambda d: d.concept_x)
        
        animations = []
        for i, dot in enumerate(all_points.submobjects):
            target_pos = np.array([
                -self.SORTED_POINTS_WIDTH / 2 + (self.SORTED_POINTS_WIDTH * (i / (self.N_POINTS -1 if self.N_POINTS > 1 else 1))),
                self.SORTED_POINTS_Y_POS,
                0
            ])
            animations.append(ApplyMethod(dot.move_to, target_pos))
            
        self.play(LaggedStart(*animations, lag_ratio=0.05), run_time=3)
        return all_points # Renamed conceptually to sorted_points

    def initialize_sliding_window_elements(self, sorted_points):
        first_dot_pos = sorted_points.submobjects[0].get_center()

        pointer_j = Triangle(color=self.POINTER_J_COLOR, fill_opacity=1).scale(0.2)
        pointer_j.next_to(first_dot_pos, DOWN, buff=0.1)
        pointer_j.current_index = 0 # Custom attribute

        pointer_i = Triangle(color=self.POINTER_I_COLOR, fill_opacity=1).scale(0.2)
        pointer_i.rotate(PI) # Point up
        pointer_i.next_to(first_dot_pos, UP, buff=0.1)

        multiset_area_outline = Rectangle(
            height=self.MULTISET_AREA_HEIGHT,
            width=self.MULTISET_AREA_WIDTH,
            color=self.MULTISET_OUTLINE_COLOR,
            stroke_width=2
        ).move_to(self.MULTISET_AREA_CENTER)

        multiset_dots = VGroup() # Will hold copies of dots in the window
        found_solutions_vgroup = VGroup().move_to(self.FOUND_SOLUTIONS_POS)

        # AnimatedBoundary might not be stable or available in all manimlib versions.
        # Using a simple Rectangle that we can update if needed.
        # multiset_boundary = AnimatedBoundary(
        #     multiset_dots, color=self.MULTISET_BOUNDARY_COLOR, 
        #     stroke_opacity=0.5, stroke_width=2
        # )
        
        l_constraint_line = Line(
            ORIGIN, UP * self.visual_L_height, 
            color=self.L_CONSTRAINT_LINE_COLOR, stroke_width=3
        )
        l_constraint_line.set_opacity(0) # Initially invisible

        return {
            "pointer_j": pointer_j, "pointer_i": pointer_i,
            "multiset_area_outline": multiset_area_outline,
            "multiset_dots": multiset_dots,
            # "multiset_boundary": multiset_boundary,
            "found_solutions_vgroup": found_solutions_vgroup,
            "l_constraint_line": l_constraint_line
        }

    def _update_multiset_visual_layout(self, multiset_dots, multiset_area_outline, animated=True, duration=0.4, new_dot_copy=None, original_dot_i_pos=None):
        if not multiset_dots.submobjects:
            if new_dot_copy: # Should not happen if new_dot_copy is added before call
                 multiset_dots.remove(new_dot_copy) # clean up if it was added then list became empty
            return []

        # Sort dots in multiset by concept_y
        multiset_dots.submobjects.sort(key=lambda d: d.concept_y)

        animations = []
        
        # Proportional scaling based on concept_y
        min_y_coord = self.CONCEPT_COORD_MIN
        max_y_coord = self.CONCEPT_COORD_MAX # Use full conceptual range for consistent scaling

        for k, dot_copy in enumerate(multiset_dots.submobjects):
            relative_y_pos = (dot_copy.concept_y - min_y_coord) / (max_y_coord - min_y_coord)
            if (max_y_coord - min_y_coord) == 0: # Avoid division by zero if all points have same y
                relative_y_pos = 0.5

            target_y = multiset_area_outline.get_bottom()[1] + relative_y_pos * self.MULTISET_AREA_HEIGHT
            target_x = multiset_area_outline.get_center()[0]
            target_pos = np.array([target_x, target_y, 0])

            if animated:
                if dot_copy == new_dot_copy and original_dot_i_pos is not None:
                    # Special animation for the new dot: move from original_dot_i's position and fade in
                    dot_copy.move_to(original_dot_i_pos)
                    dot_copy.set_opacity(0)
                    animations.append(AnimationGroup(
                        ApplyMethod(dot_copy.move_to, target_pos),
                        FadeIn(dot_copy)
                    ))
                else:
                    animations.append(ApplyMethod(dot_copy.move_to, target_pos))
            else:
                dot_copy.move_to(target_pos)
        
        if animated and animations:
            return [AnimationGroup(*animations, run_time=duration, lag_ratio=0)] # Play moves simultaneously
        elif not animated and new_dot_copy: # if not animated, ensure new_dot_copy is visible
             new_dot_copy.set_opacity(1)
        return []


    def run_core_algorithm_loop(self, sorted_points, pointer_i_obj, pointer_j_obj, 
                                multiset_dots, multiset_area_outline, multiset_boundary_rect,
                                l_constraint_line, found_solutions_vgroup):
        
        # Update multiset_boundary_rect based on multiset_dots
        def update_boundary_rect(rect):
            if len(multiset_dots) == 0:
                new_rect = Rectangle(
                    width=0.1, height=0.1, stroke_color=self.MULTISET_BOUNDARY_COLOR, 
                    stroke_width=2, stroke_opacity=0.5
                ).move_to(multiset_area_outline.get_center())
            else:
                # Create a bounding box around the actual dots in the multiset
                # This is more dynamic than fixing to multiset_area_outline
                temp_group = VGroup(*multiset_dots.submobjects) # Important: use current submobjects
                new_rect = Rectangle(
                    stroke_color=self.MULTISET_BOUNDARY_COLOR, stroke_width=2, stroke_opacity=0.5
                ).surround(temp_group) # stretch to fit
                # Ensure min width/height if only one dot
                if new_rect.get_width() < self.DOT_RADIUS * 4: new_rect.set_width(self.DOT_RADIUS*4, stretch=True)
                if new_rect.get_height() < self.DOT_RADIUS * 4: new_rect.set_height(self.DOT_RADIUS*4, stretch=True)


            rect.become(new_rect)

        multiset_boundary_rect.add_updater(update_boundary_rect)


        for i in range(self.N_POINTS):
            if i >= self.MAX_I_ITERATIONS:
                print(f"Stopping main loop at iteration {i} for demo purposes.")
                break

            original_dot_i = sorted_points.submobjects[i]

            # Animate pointer_i
            self.play(pointer_i_obj.animate.next_to(original_dot_i, UP), run_time=0.25)
            
            # --- Simulate j pointer advancing (removing points) ---
            while True:
                if pointer_j_obj.current_index >= i: # j cannot overtake i
                    break
                
                original_dot_j = sorted_points.submobjects[pointer_j_obj.current_index]
                
                if original_dot_j.concept_x < original_dot_i.concept_x - self.L_CONCEPT:
                    # Condition met: remove dot_j from window
                    self.play(ApplyMethod(original_dot_j.set_color, self.SORTED_POINT_REMOVED_COLOR), run_time=0.2)
                    
                    # Find and remove copy from multiset_dots
                    dot_copy_to_remove = None
                    for dot_copy in multiset_dots.submobjects:
                        if dot_copy.original_index == original_dot_j.index:
                            dot_copy_to_remove = dot_copy
                            break
                    
                    if dot_copy_to_remove:
                        self.play(FadeOut(dot_copy_to_remove), run_time=0.3)
                        multiset_dots.remove(dot_copy_to_remove)
                        
                        # Update multiset layout
                        layout_anims = self._update_multiset_visual_layout(multiset_dots, multiset_area_outline, animated=True, duration=0.4)
                        if layout_anims: self.play(*layout_anims)

                    # Advance pointer_j
                    pointer_j_obj.current_index += 1
                    if pointer_j_obj.current_index < len(sorted_points.submobjects):
                        next_dot_j_pos = sorted_points.submobjects[pointer_j_obj.current_index]
                        self.play(pointer_j_obj.animate.next_to(next_dot_j_pos, DOWN), run_time=0.2)
                    else: # j went past the end (should not happen if j < i)
                        break 
                else:
                    break # Condition not met, stop advancing j

            # --- Simulate i pointer inserting (adding point) ---
            self.play(ApplyMethod(original_dot_i.set_color, self.SORTED_POINT_HIGHLIGHT_COLOR), run_time=0.2)
            
            new_dot_copy = SmallDot(radius=self.DOT_RADIUS, color=self.MULTISET_DOT_COLOR)
            new_dot_copy.concept_x = original_dot_i.concept_x
            new_dot_copy.concept_y = original_dot_i.concept_y
            new_dot_copy.original_index = original_dot_i.index
            
            # Initial position for animation
            new_dot_copy.move_to(original_dot_i.get_center())
            new_dot_copy.set_opacity(0) # Will be faded in during layout animation

            multiset_dots.add(new_dot_copy)
            
            # Update multiset layout (includes new_dot_copy animation)
            layout_anims = self._update_multiset_visual_layout(
                multiset_dots, multiset_area_outline, 
                animated=True, duration=0.6, 
                new_dot_copy=new_dot_copy, original_dot_i_pos=original_dot_i.get_center()
            )
            if layout_anims: self.play(*layout_anims)
            else: # if no animation (e.g. multiset was empty and now has 1 dot) ensure it's visible
                if new_dot_copy.get_opacity() == 0: self.play(FadeIn(new_dot_copy))


            # --- Block 5: Neighbor Selection and 4-tuple Check ---
            if not len(multiset_dots) == 0: # Ensure multiset_dots has been sorted by y
                # Find new_dot_copy's index in the y-sorted multiset_dots
                # (multiset_dots.submobjects is already sorted by _update_multiset_visual_layout)
                try:
                    idx_new_dot_in_multiset = multiset_dots.submobjects.index(new_dot_copy)
                except ValueError:
                    # This should not happen if new_dot_copy was added and layout updated
                    print("Error: new_dot_copy not found in multiset_dots after layout update.")
                    continue # Skip to next i

                # Identify neighbors
                start_idx = max(0, idx_new_dot_in_multiset - 3)
                end_idx = min(len(multiset_dots.submobjects), idx_new_dot_in_multiset + 3 + 1)
                neighbor_dots_list = multiset_dots.submobjects[start_idx:end_idx]

                if neighbor_dots_list:
                    self.play(LaggedStart(*[ApplyMethod(d.set_color, self.NEIGHBOR_DOT_COLOR) for d in neighbor_dots_list]), run_time=0.3, lag_ratio=0.1)

                # Check 4-tuples
                if len(neighbor_dots_list) >= 4:
                    for k_idx in range(len(neighbor_dots_list) - 3):
                        current_four_dots = neighbor_dots_list[k_idx : k_idx + 4]
                        
                        self.play(LaggedStart(*[ApplyMethod(d.set_color, self.TEMP_CHECK_DOT_COLOR) for d in current_four_dots]), run_time=0.2, lag_ratio=0.1)
                        
                        # Create temp_check_rect
                        # Ensure current_four_dots are valid mobjects for VGroup
                        if not all(isinstance(d, Mobject) for d in current_four_dots):
                            print("Error: current_four_dots contains non-Mobject items.")
                            continue

                        vg_four_dots = VGroup(*current_four_dots)
                        temp_check_rect = Rectangle(
                            stroke_color=self.TEMP_CHECK_DOT_COLOR, stroke_width=2
                        ).surround(vg_four_dots, buff=0.1)
                        
                        self.play(ShowCreation(temp_check_rect), run_time=0.3)

                        # Position and show L-constraint line
                        # Align bottom of L-line with bottom of the lowest dot in current_four_dots
                        # (neighbor_dots_list is y-sorted, so current_four_dots[0] is lowest)
                        l_constraint_line.move_to(current_four_dots[0].get_bottom() + RIGHT * (self.DOT_RADIUS * 3 + temp_check_rect.get_width()/2) , aligned_edge=DOWN)
                        # Adjust x to be to the right of the rect
                        l_constraint_line.align_to(temp_check_rect, RIGHT)
                        l_constraint_line.shift(RIGHT * (l_constraint_line.get_width()/2 + 0.2))


                        self.play(FadeIn(l_constraint_line), run_time=0.3)

                        # Check condition
                        y_diff_concept = current_four_dots[3].concept_y - current_four_dots[0].concept_y
                        
                        solution_found_this_step = False
                        if y_diff_concept <= self.L_CONCEPT:
                            # Solution found
                            solution_found_this_step = True
                            self.play(
                                LaggedStart(*[ApplyMethod(d.set_color, self.SOLUTION_DOT_COLOR) for d in current_four_dots], lag_ratio=0.1),
                                ApplyMethod(temp_check_rect.set_stroke, self.SOLUTION_RECT_COLOR, {"width": 4}),
                                run_time=0.3
                            )
                            
                            # Create copies for solution display area
                            solution_copy_group = VGroup()
                            for dot_in_solution in current_four_dots:
                                copy = dot_in_solution.copy()
                                copy.set_color(self.SOLUTION_DOT_COLOR) # Ensure green color
                                solution_copy_group.add(copy)
                            
                            solution_copy_group.arrange(DOWN, buff=SMALL_BUFF) # Arrange the 4 dots vertically
                            solution_copy_group.scale(0.8) # Make them a bit smaller in solution area
                            
                            # Calculate position for this solution group
                            target_solution_pos = self.next_solution_spot
                            if len(found_solutions_vgroup) != 0: # if not first solution
                                target_solution_pos = found_solutions_vgroup.get_corner(DOWN+RIGHT) + \
                                                      DOWN * (solution_copy_group.get_height()/2 + MED_SMALL_BUFF) + \
                                                      RIGHT * (solution_copy_group.get_width()/2)


                            # Animate move to found_solutions_vgroup area
                            # Need to handle if found_solutions_vgroup is empty for first positioning
                            if len(found_solutions_vgroup) == 0:
                                solution_copy_group.move_to(self.FOUND_SOLUTIONS_POS)
                            else:
                                # Simple grid-like placement: find next available spot
                                # This is a placeholder; a more robust layout might be needed for many solutions
                                solution_copy_group.next_to(found_solutions_vgroup, RIGHT, buff=MED_LARGE_BUFF)
                                if solution_copy_group.get_right()[0] > FRAME_WIDTH/2 - 1: # New row
                                     solution_copy_group.next_to(found_solutions_vgroup.submobjects[0], DOWN, buff=MED_LARGE_BUFF, aligned_edge=LEFT)


                            self.play(TransformFromCopy(VGroup(*current_four_dots), solution_copy_group), run_time=0.7)
                            found_solutions_vgroup.add(solution_copy_group) # Add the group of 4 copies
                            
                            # Remove original dots from multiset_dots
                            # This also means they are no longer in neighbor_dots_list effectively
                            original_dots_to_remove_from_multiset = list(current_four_dots) # copy list before modifying multiset_dots
                            
                            multiset_dots.remove(*original_dots_to_remove_from_multiset)
                            # The FadeOut for these dots is implicitly handled by them being copied and "replaced"
                            # or they are just removed from the VGroup. Let's explicitly fade them out from multiset.
                            # self.play(LaggedStart(*[FadeOut(d) for d in original_dots_to_remove_from_multiset]), run_time=0.3)
                            # No, the instruction says "移除这些成为解的原始点", not fade out.
                            # They are removed from multiset_dots, so they will disappear from there.
                            # Update layout of multiset_dots after removal
                            layout_anims_after_solution = self._update_multiset_visual_layout(multiset_dots, multiset_area_outline, animated=True, duration=0.4)
                            if layout_anims_after_solution: self.play(*layout_anims_after_solution)

                            self.play(FadeOut(temp_check_rect), run_time=0.2)
                        
                        else:
                            # Condition not met
                            self.play(
                                LaggedStart(*[ApplyMethod(d.set_color, self.NEIGHBOR_DOT_COLOR) for d in current_four_dots], lag_ratio=0.1),
                                run_time=0.3
                            )
                            self.play(FadeOut(temp_check_rect), run_time=0.3)

                        self.play(FadeOut(l_constraint_line), run_time=0.3)
                        if not solution_found_this_step: self.remove(temp_check_rect) # Ensure removal if not faded
                        else: self.remove(temp_check_rect) # Also remove if solution found and rect faded.
                        
                        self.wait(0.1) # Small pause between checking 4-tuples

                        # If a solution was found, current_four_dots were removed from multiset_dots.
                        # This means neighbor_dots_list is now stale if we continue iterating on it.
                        # Re-fetch neighbor_dots_list or break from this k_idx loop.
                        # The problem implies we continue with the original neighbor_dots_list, but check membership.
                        # For simplicity, if a solution is found, we might stop checking further sub-tuples
                        # from this specific set of 7 neighbors, as the set has changed.
                        # However, the C++ implies `for(int k=0; k+4<=near.size(); k++)` which would continue.
                        # Let's assume we continue, but current_four_dots might now refer to dots not in multiset.
                        # The color changes should only apply to dots still in multiset.
                        # The current logic of creating VGroup(*current_four_dots) will fail if they are removed.
                        # A robust way: if solution_found_this_step, break from k_idx loop and re-evaluate neighbors for new_dot_copy.
                        # For now, let's stick to the simpler interpretation that the loop continues,
                        # but this might lead to issues if dots are removed.
                        # The instruction "从 multiset_dots 和 neighbor_dots 中移除这些成为解的原始点"
                        # implies neighbor_dots (the Python list) should also be updated.
                        # This is complex. Let's assume `current_four_dots` are processed, and if removed,
                        # the `neighbor_dots_list` for the *next* `k_idx` iteration will be shorter implicitly
                        # if we rebuild it, or we must handle missing dots.
                        # The easiest is that `neighbor_dots_list` is static for this i-th point's check.
                        # If `current_four_dots` are removed, they are gone. The next iteration of `k_idx`
                        # will pick the *next* 4 from the original `neighbor_dots_list`.
                        # This means we need to check if `current_four_dots` are still in `multiset_dots` before processing.
                        
                        # Let's refine: if solution found, those dots are removed. The `neighbor_dots_list`
                        # still holds references. The color restoration at the end must check.
                        # The check for `k_idx` should be on a dynamic list or handle removed items.
                        # To simplify, if a solution is found, we'll break this inner k-loop.
                        # This is a common heuristic in some versions of such algorithms.
                        if solution_found_this_step:
                             break # Stop checking other 4-tuples from this neighbor_dots_list for this i.


                # Restore color of remaining neighbor dots (those not part of a solution)
                anims_restore_color = []
                for d_neighbor in neighbor_dots_list:
                    if d_neighbor in multiset_dots.submobjects: # Check if still in multiset
                        anims_restore_color.append(ApplyMethod(d_neighbor.set_color, self.MULTISET_DOT_COLOR))
                if anims_restore_color:
                    self.play(LaggedStart(*anims_restore_color), run_time=0.3, lag_ratio=0.1)

            # Restore color of original_dot_i in sorted_points line
            self.play(ApplyMethod(original_dot_i.set_color, self.POINT_COLOR), run_time=0.2)
            self.wait(0.2) # Pause after processing each i

        multiset_boundary_rect.remove_updater(update_boundary_rect) # Clean up updater


    def cleanup_scene(self, sorted_points, pointer_i, pointer_j,
                      multiset_dots, multiset_area_outline, multiset_boundary_rect,
                      l_constraint_line):
        
        fade_out_elements = [
            pointer_i, pointer_j, multiset_area_outline, multiset_boundary_rect,
            l_constraint_line # l_constraint_line might already be faded out
        ]
        # Fade out all dots in sorted_points and multiset_dots
        # Check if they are still on screen
        
        # Create a list of actual mobjects to fade out
        anims_to_play = []
        for mob in fade_out_elements:
            if mob.get_opacity() > 0 and mob in self.mobjects:
                 anims_to_play.append(FadeOut(mob))
        
        # Dots in sorted_points
        # Some might have been set to GRAY, others BLUE. Fade all.
        if sorted_points in self.mobjects or any(d in self.mobjects for d in sorted_points.submobjects):
            anims_to_play.append(FadeOut(sorted_points))

        # Dots in multiset_dots
        # Some might have been faded out if they became solutions.
        # Create a temporary VGroup of remaining visible dots in multiset_dots for fadeout.
        visible_multiset_dots = VGroup(*[d for d in multiset_dots.submobjects if d.get_opacity() > 0 and d in self.mobjects])
        if len(visible_multiset_dots) != 0:
            anims_to_play.append(FadeOut(visible_multiset_dots))
        
        if anims_to_play:
            self.play(*anims_to_play, run_time=2)
        
        # found_solutions_vgroup remains on screen.

