from manim import *
from manim_slides import Slide

class MoERoutingSlide(Slide):
    def construct(self):
        # 1. Slide Title
        title = Text("How MoE Routes Diffusion Steps", font_size=40, weight=BOLD).to_edge(UP)
        self.play(FadeIn(title, shift=UP))

        # 2. Layout anchors (keeps positions stable across resolutions)
        content_y = title.get_bottom()[1] - 2.4

        # 3. The Router
        router = Circle(radius=0.8, color=YELLOW).move_to(LEFT * 4 + UP * content_y)
        router_text = Text("Router\n(SNR)", font_size=20).move_to(router.get_center())
        router_group = VGroup(router, router_text)

        # 4. High-Noise Expert
        expert_high = Rectangle(width=3.5, height=1.5, color=ORANGE).move_to(RIGHT * 2 + UP * (content_y + 1.1))
        expert_high_text = Text("High-Noise Expert\n(Macro-Structure)", font_size=20).move_to(expert_high.get_center())
        group_high = VGroup(expert_high, expert_high_text)

        # 5. Low-Noise Expert
        expert_low = Rectangle(width=3.5, height=1.5, color=TEAL).move_to(RIGHT * 2 + UP * (content_y - 1.1))
        expert_low_text = Text("Low-Noise Expert\n(Micro-Details)", font_size=20).move_to(expert_low.get_center())
        group_low = VGroup(expert_low, expert_low_text)

    # 6. Arrows from router to experts
        arrow_high = Arrow(router.get_right(), expert_high.get_left(), buff=0.1)
        arrow_low = Arrow(router.get_right(), expert_low.get_left(), buff=0.1)

        self.play(Create(router_group), Create(group_high), Create(group_low), GrowArrow(arrow_high), GrowArrow(arrow_low))

    # 7. Animate a High-Noise Token
        noisy_token = Dot(color=GRAY, radius=0.2).next_to(router, LEFT, buff=2)
        noisy_label = Text("Early Timestep\n(High Noise)", font_size=16).next_to(noisy_token, UP)
        
        self.play(FadeIn(noisy_token), FadeIn(noisy_label))
        self.play(noisy_token.animate.move_to(router.get_center()))
        self.play(noisy_token.animate.move_to(expert_high.get_center()), run_time=1.5)
        
        # Pause to explain High Noise
        self.next_slide()

    # 8. Clean up High-Noise token, bring in Low-Noise token
        self.play(FadeOut(noisy_token), FadeOut(noisy_label))
        
        clean_token = Dot(color=BLUE, radius=0.2).next_to(router, LEFT, buff=2)
        clean_label = Text("Late Timestep\n(Low Noise)", font_size=16).next_to(clean_token, UP)

        self.play(FadeIn(clean_token), FadeIn(clean_label))
        self.play(clean_token.animate.move_to(router.get_center()))
        self.play(clean_token.animate.move_to(expert_low.get_center()), run_time=1.5)

        # Pause to explain Low Noise
        self.next_slide()

    # 9. Clean exit
        self.play(FadeOut(Group(*self.mobjects)))
