from manim import *
from manim_slides import Slide

class ThanksSlide(Slide):
    def construct(self):
        # 1. Main Thanks
        thanks = Text("Thank You!", font_size=72, weight=BOLD, color=WHITE)
        self.play(Write(thanks), run_time=2)

        # 2. Contact Info / Project Link
        contact = Text("Questions?", font_size=32, color=YELLOW).next_to(thanks, DOWN, buff=1.5)
        docs = Text("Full Documentation & PR: [https://github.com/Long-form-AI-video-generation/long-v2v-custom-node]", font_size=20, color=LIGHT_GREY).next_to(contact, DOWN, buff=0.5)
        
        self.play(FadeIn(contact, shift=UP), FadeIn(docs, shift=UP))

        # Keep this on screen until you quit the presentation
        self.next_slide()
