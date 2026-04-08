from manim import *
from manim_slides import Slide
import os

class EvaluationMetricsSlide(Slide):
    def construct(self):
        # 1. Slide Title
        title = Text("Mathematical Validation & Consistency", font_size=36, weight=BOLD).to_edge(UP)
        self.play(FadeIn(title, shift=UP))

        # 2. Text Area (Left Side)
        bullet_font = 20
        bullet = Text(
            "• Incorporated LLIPS (Low-Level\nImage Processing and Similarity)\nevaluation metrics to rigorously\nmeasure output consistency.", 
            font_size=bullet_font, line_spacing=1.5
        )
        # Position on the left edge
        bullet.to_edge(LEFT, buff=0.8).shift(UP * 0.5)
        
        self.play(FadeIn(bullet))

        self.next_slide()

        # 3. Image Insertion Area (Right Side)
        # Checking if image exists to prevent cryptic Manim crashes
        img_path = "media/images/llips.png"
        if os.path.exists(img_path):
            evaluation_image = ImageMobject(img_path)
            # Scale it to fit the right half of the screen
            evaluation_image.scale_to_fit_width(6).to_edge(RIGHT, buff=0.8).shift(DOWN * 0.5)
            # Add a thin white border to make it pop
            border = SurroundingRectangle(evaluation_image, color=WHITE, stroke_width=2)
            
            self.play(FadeIn(evaluation_image), Create(border))
        else:
            # Fallback if the image isn't found
            error_text = Text("[Image missing: media/images/llips.png]", color=RED).to_edge(RIGHT, buff=1.0)
            self.play(FadeIn(error_text))

        self.next_slide()

        # 4. Clean exit
        self.play(FadeOut(Group(*self.mobjects)))
