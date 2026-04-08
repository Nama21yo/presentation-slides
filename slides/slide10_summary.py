from manim import *
from manim_slides import Slide

class SummarySlide(Slide):
    def construct(self):
        # 1. Slide Title
        title = Text("Executive Summary & Roadmap", font_size=36, weight=BOLD).to_edge(UP)
        self.play(FadeIn(title, shift=UP))

        # 2. Key Achievements (Checklist)
        summary_title = Text("Current Status (Q2 2026):", font_size=24, color=YELLOW).to_edge(LEFT, buff=1).shift(UP * 1.5)
        self.play(Write(summary_title))

        checkpoints = VGroup(
            Text("✔ Finalized Long-Form (60s+) Workflow", font_size=20),
            Text("✔ High-Fidelity 1080p Generation", font_size=20),
            Text("✔ Perceptual Validation (LLIPS/LPIPS)", font_size=20),
        ).arrange(DOWN, aligned_edge=LEFT, buff=0.4).next_to(summary_title, DOWN, buff=0.5).align_to(summary_title, LEFT)

        for check in checkpoints:
            self.play(FadeIn(check, shift=RIGHT * 0.2))
        
        self.next_slide()

        # 3. Future Roadmap (The "Next Steps")
        roadmap_title = Text("Future Directions:", font_size=24, color=BLUE).next_to(checkpoints, DOWN, buff=1.0).align_to(summary_title, LEFT)
        self.play(Write(roadmap_title))

        steps = VGroup(
            Text("Maintenance and Integrating it inside AI Agent Marketing Implementation", font_size=20),
        ).arrange(DOWN, aligned_edge=LEFT, buff=0.4).next_to(roadmap_title, DOWN, buff=0.5).align_to(summary_title, LEFT)

        for step in steps:
            self.play(FadeIn(step, shift=RIGHT * 0.2))

        self.next_slide()

        # 4. Clean exit
        self.play(FadeOut(Group(*self.mobjects)))
