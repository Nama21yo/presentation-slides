from manim import *
from manim_slides import Slide

class EnvironmentCoherenceSlide(Slide):
    def construct(self):
        # 1. Slide Title
        title = Text("Spatial & Environmental Coherence", font_size=36, weight=BOLD).to_edge(UP)
        self.play(FadeIn(title, shift=UP))

        # 2. Setup the Text Area (Left Side)
        text_group = VGroup()
        bullet_font = 18

        bullet1 = Text(
            "• Segment Interpolation: Incorporated the RIFE VFI\nInterpolation node to resolve frame-to-frame coherence.", 
            font_size=bullet_font, line_spacing=1.2
        )
        text_group.add(bullet1)
        
        bullet1.to_edge(LEFT, buff=0.5).shift(UP * 1)
        self.play(FadeIn(bullet1))
        
        self.next_slide()

        # 3. Background Extraction (Text + Visual)
        bullet2 = Text(
            "• Background Extraction: Integrated Sam2Segmentation\nand custom masking to surgically extract backgrounds.", 
            font_size=bullet_font, line_spacing=1.2
        ).next_to(bullet1, DOWN, buff=0.6).align_to(bullet1, LEFT)
        
        # Visual for Extraction (Right Side)
        # Background layer
        bg_rect = Rectangle(width=2.5, height=1.5, color=DARK_BLUE, fill_opacity=0.8)
        bg_label = Text("Background", font_size=14).next_to(bg_rect, UP)
        bg_group = VGroup(bg_rect, bg_label).shift(RIGHT * 3 + UP * 1)
        
        # Foreground Character layer (A simple stylized person)
        head = Circle(radius=0.25, color=ORANGE, fill_opacity=1)
        body = Polygon(ORIGIN, DOWN*0.8+LEFT*0.4, DOWN*0.8+RIGHT*0.4, color=ORANGE, fill_opacity=1)
        body.next_to(head, DOWN, buff=0)
        fg_person = VGroup(head, body).move_to(bg_rect.get_center())
        fg_label = Text("Foreground", font_size=14, color=ORANGE).next_to(fg_person, DOWN)
        fg_group = VGroup(fg_person, fg_label)

        # Show them merged, then split them apart
        self.play(FadeIn(bullet2), FadeIn(bg_group), FadeIn(fg_group))
        self.play(
            bg_group.animate.shift(RIGHT * 1.5),
            fg_group.animate.shift(LEFT * 1.5),
            run_time=1.5
        )

        self.next_slide()

        # 4. Lighting Stability & Sliding Window (Text + Visual)
        bullet3 = Text(
            "• Lighting Stability: Utilized a sliding window technique\n(81-frame context) to maintain constant lighting.", 
            font_size=bullet_font, line_spacing=1.2
        ).next_to(bullet2, DOWN, buff=0.6).align_to(bullet1, LEFT)

        # Visual for Sliding Window
        timeline = Rectangle(width=5, height=0.2, color=GRAY, fill_opacity=0.4).shift(RIGHT * 3 + DOWN * 2)
        timeline_label = Text("Video Timeline (Frames)", font_size=14).next_to(timeline, DOWN)
        
        window = Rectangle(width=1.5, height=0.4, color=YELLOW, stroke_width=4).move_to(timeline.get_left() + RIGHT * 0.75)
        window_label = Text("81-Frame Context", font_size=14, color=YELLOW).next_to(window, UP)
        window_group = VGroup(window, window_label)

        self.play(FadeIn(bullet3), Create(timeline), FadeIn(timeline_label), Create(window_group))
        
        # Animate the window sliding across the timeline
        self.play(
            window_group.animate.shift(RIGHT * 3.5),
            run_time=3,
            rate_func=there_and_back # Slides right, then slides back left
        )

        self.next_slide()

        # 5. Clean exit
        self.play(FadeOut(Group(*self.mobjects)))
