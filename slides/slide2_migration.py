from manim import *
from manim_slides import Slide

class MigrationSlide(Slide):
    def construct(self):
        # 1. Slide Title
        title = Text("Architecture Shift: Migrating to Wan 2.2", font_size=40, weight=BOLD).to_edge(UP)
        self.play(FadeIn(title, shift=UP))

        # 2. Wan 2.1 Box (Dense)
        box21 = Rectangle(width=4, height=2, color=RED)
        text21 = Text("Wan 2.1\n(Dense DiT)", font_size=24).move_to(box21.get_center())
        group21 = VGroup(box21, text21).shift(LEFT * 3)

        # 3. Wan 2.2 Box (MoE)
        box22 = Rectangle(width=4, height=2, color=GREEN)
        text22 = Text("Wan 2.2\n(Mixture of Experts)", font_size=24).move_to(box22.get_center())
        group22 = VGroup(box22, text22).shift(RIGHT * 3)

        # 4. Connecting Arrow
        arrow = Arrow(group21.get_right(), group22.get_left(), buff=0.2)

        # 5. Animate the boxes appearing
        self.play(Create(group21))
        self.play(GrowArrow(arrow))
        self.play(Create(group22))

        # 6. Add contextual bullet points under the boxes
        bullet1 = Text("• All parameters compute every step\n• Heavy compute bottleneck", font_size=18, color=LIGHT_GREY, line_spacing=1).next_to(group21, DOWN, buff=0.5)
        bullet2 = Text("• Sparse routing\n• 27B Parameters (Only 14B Active)", font_size=18, color=LIGHT_GREY, line_spacing=1).next_to(group22, DOWN, buff=0.5)

        self.play(FadeIn(bullet1))
        self.play(FadeIn(bullet2))

        # 7. Pause for speaker
        self.next_slide()

        # 8. Clean exit
        self.play(FadeOut(Group(*self.mobjects)))
