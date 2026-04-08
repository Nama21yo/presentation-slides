from manim import *
from manim_slides import Slide

class LengthBarrierSlide(Slide):
    def construct(self):
        # 1. Slide Title
        title = Text("Breaking the Length Barrier & Memory Management", font_size=36, weight=BOLD).to_edge(UP)
        self.play(FadeIn(title, shift=UP))

        # 2. Setup the Timeline Background
        timeline_bg = Rectangle(width=10, height=0.5, color=DARK_GRAY, fill_opacity=0.5).shift(UP*1.5)
        self.play(Create(timeline_bg))

        # 3. Animate to 10s and hit the wall
        bar = Rectangle(width=1.6, height=0.5, color=BLUE, fill_opacity=1).align_to(timeline_bg, LEFT).shift(UP*1.5)
        label_time = Text("10s", font_size=20).next_to(bar, DOWN)
        red_wall = Line(bar.get_corner(UR) + UP*0.5, bar.get_corner(DR) + DOWN*0.5, color=RED, stroke_width=6)
        
        self.play(GrowFromEdge(bar, LEFT))
        self.play(FadeIn(label_time), Create(red_wall))

        # Display The Problem
        bullet1 = Text("• The Problem: Extending generation capability for longer videos.", font_size=22).next_to(timeline_bg, DOWN, buff=1.5).align_to(timeline_bg, LEFT)
        self.play(FadeIn(bullet1))
        
        # Pause 1
        self.next_slide()

        # 4. Break the wall, extend to 25s, and show overlapping loops
        self.play(FadeOut(red_wall))
        bar_25s = Rectangle(width=4.1, height=0.5, color=TEAL, fill_opacity=1).align_to(timeline_bg, LEFT).shift(UP*1.5)
        label_25s = Text("25s (405 frames)", font_size=20).next_to(bar_25s, DOWN, aligned_edge=RIGHT)
        
        # Visualizing the 8-frame overlap with 5 loops
        loops = VGroup(*[Rectangle(width=1, height=0.3, color=YELLOW, fill_opacity=0.6) for _ in range(5)])
        loops.arrange(RIGHT, buff=-0.2).next_to(bar_25s, UP, buff=0.2).align_to(bar_25s, LEFT)
        
        self.play(Transform(bar, bar_25s), Transform(label_time, label_25s))
        self.play(Create(loops, lag_ratio=0.2))

        bullet2 = Text("• Autoregressive Looping: Integrated WanVideoLoopArgs (5 loops, 8-frame overlap).", font_size=22).next_to(bullet1, DOWN, buff=0.4).align_to(bullet1, LEFT)
        self.play(FadeIn(bullet2))
        
        # Pause 2
        self.next_slide()

        # 5. Extend to full length and address Memory/Blending
        bar_full = Rectangle(width=10, height=0.5, color=GREEN, fill_opacity=1).align_to(timeline_bg, LEFT).shift(UP*1.5)
        label_full = Text("Long-Form Video", font_size=20).next_to(bar_full, DOWN, aligned_edge=RIGHT)
        
        self.play(Transform(bar, bar_full), Transform(label_time, label_full), FadeOut(loops))

        bullet3 = Text("• Seamless Transitions: Wanlooper divides videos, blending via Hamming Window.", font_size=22).next_to(bullet2, DOWN, buff=0.4).align_to(bullet1, LEFT)
        # Using a slightly reddish color to emphasize the memory error
        bullet4 = Text("• Memory Constraints: Fixed 'Process Killed' OOM error by controlling RAM loading.", font_size=22, color=RED_A).next_to(bullet3, DOWN, buff=0.4).align_to(bullet1, LEFT)

        self.play(FadeIn(bullet3))
        self.play(FadeIn(bullet4))
        
        # Pause 3
        self.next_slide()

        # 6. Clean exit
        self.play(FadeOut(Group(*self.mobjects)))
