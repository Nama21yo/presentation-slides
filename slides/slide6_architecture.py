from manim import *
from manim_slides import Slide
import os

class ArchitectureSlide(Slide):
    def construct(self):
        # 1. Slide Title
        title = Text("Wan Animate Discovery & Core Architecture", font_size=36, weight=BOLD).to_edge(UP)
        self.play(FadeIn(title, shift=UP))

        # 2. Foundation Text (Top Left)
        foundation_text = Text(
            "• Foundation: Built upon Wan-I2V,\nenhanced with Mixture of Experts (MoE).", 
            font_size=20, line_spacing=1.2
        ).next_to(title, DOWN, buff=0.5).to_edge(LEFT, buff=0.5)
        
        self.play(FadeIn(foundation_text))

        # 3. Load the Image (Right Side)
        # Checking if image exists to prevent cryptic Manim crashes
        img_path = "media/images/wan-animate.png"
        if os.path.exists(img_path):
            arch_image = ImageMobject(img_path)
            # Scale it to fit the right half of the screen
            arch_image.scale_to_fit_width(7).to_edge(RIGHT, buff=0.5).shift(DOWN * 0.5)
            self.play(FadeIn(arch_image))
        else:
            # Fallback if the image isn't found
            error_text = Text("[Image missing: media/images/wan-animate.png]", color=RED).to_edge(RIGHT)
            self.play(FadeIn(error_text))
            arch_image = error_text

        self.next_slide()

        # 4. Unified Input Formulation Section
        input_title = Text("• Unified Input Formulation:", font_size=22, weight=BOLD, color=YELLOW).next_to(foundation_text, DOWN, buff=0.5).align_to(foundation_text, LEFT)
        self.play(FadeIn(input_title))

        # 5. Define the Latent Texts (Left Side)
        latent_font = 18
        target_text = Text("- Target Latent: Active denoised frame.", font_size=latent_font).next_to(input_title, DOWN, buff=0.3).align_to(input_title, LEFT).shift(RIGHT * 0.5)
        ref_text = Text("- Ref Latent: Identity anchor (Source Image).", font_size=latent_font).next_to(target_text, DOWN, buff=0.3).align_to(target_text, LEFT)
        tempo_text = Text("- Tempo Latent: Motion/physics guidance.", font_size=latent_font).next_to(ref_text, DOWN, buff=0.3).align_to(target_text, LEFT)
        env_text = Text("- Env Latent: Background spatial data.", font_size=latent_font).next_to(tempo_text, DOWN, buff=0.3).align_to(target_text, LEFT)

        # 6. Define highlight boxes directly in normalized image coordinates.
        # rx/ry are percentages inside wan-animate.png, where (0,0)=top-left and (1,1)=bottom-right.
        def image_point(rx: float, ry: float):
            return (
                arch_image.get_center()
                + RIGHT * ((rx - 0.5) * arch_image.width)
                + UP * ((0.5 - ry) * arch_image.height)
            )

        latent_box_w = arch_image.width * 0.10
        latent_box_h = arch_image.height * 0.10

        # Coordinates tuned to the latent region in wan-animate.png.
        box_target = Rectangle(width=latent_box_w, height=latent_box_h, color=RED, stroke_width=4).move_to(image_point(0.37, 0.42))
        box_ref = Rectangle(width=latent_box_w, height=latent_box_h, color=BLUE, stroke_width=4).move_to(image_point(0.29, 0.29))
        box_tempo = Rectangle(width=latent_box_w, height=latent_box_h, color=GREEN, stroke_width=4).move_to(image_point(0.37, 0.29))
        box_env = Rectangle(width=latent_box_w, height=latent_box_h, color=ORANGE, stroke_width=4).move_to(image_point(0.29, 0.42))

        # Animate Target Latent
        self.play(FadeIn(target_text), Create(box_target))
        self.next_slide()

        # Animate Ref Latent
        self.play(FadeIn(ref_text), Transform(box_target, box_ref)) # Box moves to the next item
        self.next_slide()

        # Animate Tempo Latent
        self.play(FadeIn(tempo_text), Transform(box_target, box_tempo))
        self.next_slide()

        # Animate Env Latent
        self.play(FadeIn(env_text), Transform(box_target, box_env))
        self.next_slide()

        # 7. Clean exit
        self.play(FadeOut(Group(*self.mobjects)))
