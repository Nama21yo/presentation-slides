from manim import *
from manim_slides import Slide
import numpy as np # Needed for generating realistic waveform points

class QualitySyncSlide(Slide):
    def construct(self):
        # 1. Slide Title
        title = Text("Enhancing Tracking, Audio & Lip-Sync", font_size=36, weight=BOLD).to_edge(UP)
        self.play(FadeIn(title, shift=UP))

        # Layout anchors
        right_panel_anchor = RIGHT * 3 + UP * 1.2

        # 2. Visual Tracking Visualization (Top-Right)
        # Representing a stylized face
        face_circle = Circle(radius=0.7, color=WHITE).move_to(right_panel_anchor)
        left_eye = Dot(color=BLUE).move_to(face_circle.get_center() + LEFT*0.25 + UP*0.2)
        right_eye = Dot(color=BLUE).move_to(face_circle.get_center() + RIGHT*0.25 + UP*0.2)
        # The mouth we will pulsate later
        mouth_ellipse = Ellipse(width=0.3, height=0.1, color=RED).move_to(face_circle.get_center() + DOWN*0.2)
        
        face_group = VGroup(face_circle, left_eye, right_eye, mouth_ellipse)
        self.play(Create(face_group))

        # The Green Tracking UI Overlay
        tracking_box = Rectangle(height=1.8, width=1.8, color=GREEN).move_to(face_circle.get_center())
        corners = VGroup(
            Line(ORIGIN, RIGHT*0.2).next_to(tracking_box.get_corner(UL), DR, buff=0),
            Line(ORIGIN, DOWN*0.2).next_to(tracking_box.get_corner(UL), DR, buff=0),
            Line(ORIGIN, LEFT*0.2).next_to(tracking_box.get_corner(UR), DL, buff=0),
            Line(ORIGIN, DOWN*0.2).next_to(tracking_box.get_corner(UR), DL, buff=0),
            # (Adding corner brackets for a more 'tracking' feel)
        ).move_to(tracking_box)
        tracking_ui = VGroup(tracking_box, corners)

        self.play(Create(tracking_ui))
        # Bullet 1 appears on spacebar click
        self.next_slide()
        
        bullet1 = Text("• Refactored face detection: Replaced DWpose\nwith ViTPose + YOLO (via Onnx).", font_size=18, line_spacing=1.2).next_to(face_group, DOWN, buff=1.0).align_to(face_group, LEFT)
        self.play(FadeIn(bullet1))

        # 3. Audio Waveform and Sync Visualization
        self.next_slide()

        # Generating a complex looking wave using a sine wave multiplied by random variations
        x = np.linspace(-2.4, 2.4, 200)
        y = np.sin(x * 10) * np.random.uniform(0.1, 0.4, 200)

        # Creating a series of lines to represent points centered under the face panel
        waveform_center = face_group.get_center() + DOWN * 2.2
        waveform_points = [
            waveform_center + RIGHT * val_x + UP * val_y
            for val_x, val_y in zip(x, y)
        ]
        audio_waveform = VGroup(*[Line(waveform_points[i], waveform_points[i+1], color=YELLOW) for i in range(len(waveform_points)-1)])
        
        self.play(Create(audio_waveform, run_time=1.5))

        bullet2 = Text("• Lip-Sync: Integrated MultiTalk model\nfor coherent mouth synchronization.", font_size=18, line_spacing=1.2).next_to(bullet1, DOWN, buff=0.4).align_to(bullet1, LEFT)
        self.play(FadeIn(bullet2))

        # The Synchronization Animation Loop
        # Pulsate the mouth ellipse and slightly shake the waveform to simulate live audio
        for _ in range(3):
            self.play(
                mouth_ellipse.animate.scale(1.5).set_color(ORANGE),
                audio_waveform.animate.shift(UP*0.05),
                run_time=0.3
            )
            self.play(
                mouth_ellipse.animate.scale(1/1.5).set_color(RED),
                audio_waveform.animate.shift(DOWN*0.05),
                run_time=0.3
            )

        # 4. Audio Coherence Fix
        self.next_slide()

        # Visualizing a sound wave with a pop, then a smooth wave
        pop_wave_center = LEFT * 4 + UP * 1
        pop_wave = VGroup(
            Text("POP!", font_size=24, color=RED).move_to(pop_wave_center),
            Line(pop_wave_center + LEFT * 1 + DOWN * 0.5, pop_wave_center + RIGHT * 1 + UP * 0.5, color=RED),
            Line(pop_wave_center + LEFT * 1 + UP * 0.5, pop_wave_center + RIGHT * 1 + DOWN * 0.5, color=RED)
        )
        
        smooth_wave = VGroup(
            Text("Smooth Audio", font_size=24, color=GREEN).move_to(pop_wave_center),
            FunctionGraph(lambda x: np.sin(x*5) * 0.3, x_range=(-1.0, 1.0), color=GREEN).move_to(pop_wave_center + DOWN * 0.5)
        )

        self.play(Create(pop_wave))
        self.play(ReplacementTransform(pop_wave, smooth_wave))

        bullet3 = Text("• Audio Coherence: Fixed spikes/pops\nby deferring audio merging to final step.", font_size=18, line_spacing=1.2).next_to(bullet2, DOWN, buff=0.4).align_to(bullet1, LEFT)
        self.play(FadeIn(bullet3))

        self.next_slide()

        # 5. Clean exit
        self.play(FadeOut(Group(*self.mobjects)))
