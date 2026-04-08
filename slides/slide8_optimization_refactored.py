from manim import *
from manim_slides import Slide

class OptimizationComputeSlide(Slide):
    def construct(self):
        # 1. Slide Title
        title = Text("Quality vs. Compute Optimization", font_size=36, weight=BOLD).to_edge(UP)
        self.play(FadeIn(title, shift=UP))

        # 2. Setup the Text Area (Left Side)
        bullet_font = 18
        text_group = VGroup()

        bullet1 = Text(
            "• The Trade-Off: Increased steps (5 -> 21)\nboosted clarity but pushed time to 4h 20m.", 
            font_size=bullet_font, line_spacing=1.2
        ).to_edge(LEFT, buff=0.5).shift(UP * 1.5)
        text_group.add(bullet1)
        
        # --- Visual: The Dials (Right Side) ---
        # Helper to create a half-circle dial
        def create_dial(label_text, color, shift_pos):
            arc = Arc(radius=1.2, start_angle=0, angle=PI, color=color, stroke_width=6)
            center = arc.get_arc_center()
            # Start needle pointing left (Low)
            needle = Line(center, center + LEFT * 1, color=WHITE, stroke_width=4)
            dot = Dot(center, color=WHITE)
            label = Text(label_text, font_size=16).next_to(arc, DOWN)
            
            group = VGroup(arc, needle, dot, label).shift(shift_pos)
            return group, needle, center

        # Create Quality and Compute dials
        quality_group, quality_needle, q_center = create_dial("Quality / Steps", BLUE, RIGHT * 1.5 + UP * 1)
        compute_group, compute_needle, c_center = create_dial("Compute Time", RED, RIGHT * 4.5 + UP * 1)

        self.play(FadeIn(bullet1))
        self.play(Create(quality_group), Create(compute_group))
        
        # Animate the trade-off: Quality goes up, but Compute hits the redline
        self.play(
            # Rotate needle to the right (High)
            Rotate(quality_needle, angle=-PI*0.8, about_point=q_center),
            Rotate(compute_needle, angle=-PI*0.9, about_point=c_center),
            run_time=1.5
        )
        self.next_slide()

        # 3. Resolution Upscale (Text + Visual)
        bullet2 = Text(
            "• Resolution: Upgraded latent from 480p\nto 1080p using the 4Ultrasharp model.", 
            font_size=bullet_font, line_spacing=1.2
        ).next_to(bullet1, DOWN, buff=0.5).align_to(bullet1, LEFT)
        text_group.add(bullet2)

        # Visual for Resolution
        res_480 = Rectangle(width=1.2, height=0.7, color=GRAY)
        res_480_text = Text("480p", font_size=14).move_to(res_480)
        group_480 = VGroup(res_480, res_480_text).shift(RIGHT * 3 + DOWN * 1.5)
        
        res_1080 = Rectangle(width=2.5, height=1.4, color=TEAL)
        res_1080_text = Text("1080p (4Ultrasharp)", font_size=14).move_to(res_1080)
        group_1080 = VGroup(res_1080, res_1080_text).shift(RIGHT * 3 + DOWN * 1.5)

        self.play(FadeIn(bullet2))
        self.play(Create(group_480))
        self.play(Transform(group_480, group_1080)) # Animate the upscale
        
        self.next_slide()

        # 4. Speed Optimization (Text)
        bullet3 = Text(
            "• Speed Optimization: Integrated Wan Tea Cache\nand distilled LoRA to bypass redundant inference.", 
            font_size=bullet_font, line_spacing=1.2
        ).next_to(bullet2, DOWN, buff=0.5).align_to(bullet1, LEFT)
        text_group.add(bullet3)

        self.play(FadeIn(bullet3))
        
        # Animate the Compute needle dropping back down to a manageable level
        self.play(
            Rotate(compute_needle, angle=PI*0.5, about_point=c_center),
            compute_group[0].animate.set_color(GREEN), # Change arc color to green to show optimization
            run_time=1.5
        )
        
        self.next_slide()

        # 5. Clean exit
        self.play(FadeOut(Group(*self.mobjects)))
