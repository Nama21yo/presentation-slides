from manim import *
from manim_slides import Slide

class TitleSlide(Slide):
    def construct(self):
        # 1. Define the text elements
        # Using a bold weight for the main architectural focus
        main_title = Text("Long-Form Reference-to-Video Generation", font_size=40, weight=BOLD)
        
        # Subtitle to give context
        subtitle = Text("Wan Animate Progress Report", font_size=32, color=BLUE)
        
        # Presenter name
        name = Text("By: Natnael.Y", font_size=24, color=LIGHT_GREY)

        # 2. Position the elements on the screen
        main_title.shift(UP * 0.5)
        subtitle.next_to(main_title, DOWN, buff=0.4)
        name.next_to(subtitle, DOWN, buff=1.0)

        # 3. Animate them into the scene
        self.play(Write(main_title), run_time=1.5)
        self.play(FadeIn(subtitle, shift=UP * 0.2), run_time=1)
        self.play(FadeIn(name))

        # 4. PAUSE: Wait for you to press the Spacebar during the presentation
        self.next_slide()

        # 5. Animate them out to cleanly transition to Slide 2
        self.play(
            FadeOut(main_title, shift=UP),
            FadeOut(subtitle, shift=UP),
            FadeOut(name, shift=UP)
        )
