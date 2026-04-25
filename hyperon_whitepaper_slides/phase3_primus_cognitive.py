"""
Phase 3 — PRIMUS: The Cognitive Architecture
Covers: Two-loop design · Goal Loop (MetaMo→SubRep→PLN→Execute→Feedback)
         Ambient Loop · Shared Atomspace · PLN · ECAN · MOSES/GEO-EVO
         WILLIAM · Pattern Mining · Concept Blending
"""
from manim import *
from manim_slides import Slide
import numpy as np


def panel(title, bullets, width=5.8, tc=BLUE_B, fc=21, ft=26):
    t = Text(title, font_size=ft, color=tc)
    rows = VGroup()
    for b in bullets:
        d = Dot(radius=0.045, color=tc)
        bt = Text(b, font_size=fc, color=WHITE, line_spacing=1.05)
        rows.add(VGroup(d, bt).arrange(RIGHT, buff=0.12, aligned_edge=UP))
    rows.arrange(DOWN, aligned_edge=LEFT, buff=0.15)
    content = VGroup(t, rows).arrange(DOWN, aligned_edge=LEFT, buff=0.18)
    bg = RoundedRectangle(corner_radius=0.12, width=width, height=content.height + 0.42,
                          stroke_color=tc, stroke_width=2, fill_color=BLACK, fill_opacity=0.22)
    content.move_to(bg).shift(LEFT * 0.05)
    return VGroup(bg, content)


def lbox(text, col=WHITE, font=20, width=3.2, pad=0.2):
    t = Text(text, font_size=font, color=col, line_spacing=1.1)
    bg = RoundedRectangle(corner_radius=0.1, width=width, height=t.height + 2 * pad,
                          stroke_color=col, stroke_width=2, fill_color=BLACK, fill_opacity=0.25)
    t.move_to(bg)
    return VGroup(bg, t)


def tag(text, color=TEAL_B):
    return lbox(text, col=color, font=24, width=max(len(text) * 0.17 + 0.8, 3.5))


# ──────────────────────────────────────────────────────────────────────────────
# 3.1 Two-Loop Design
# ──────────────────────────────────────────────────────────────────────────────

class Phase3TwoLoopDesign(Slide):
    def construct(self):
        hdr = Text("3.1 — PRIMUS: Two Loops Over One Memory", font_size=31, color=BLUE_B)
        hdr.to_edge(UP, buff=0.35)
        tg = tag("Goal-Directed Loop  +  Ambient Loop", color=BLUE_B).next_to(hdr, DOWN, buff=0.25)
        self.play(FadeIn(hdr), FadeIn(tg), run_time=0.7)

        # Shared Atomspace background
        atomspace_rect = RoundedRectangle(
            corner_radius=0.2, width=11.5, height=1.2,
            stroke_color=GRAY_C, stroke_width=2, fill_color=DARK_BROWN, fill_opacity=0.35,
        ).move_to(ORIGIN)
        as_label = Text("Shared Atomspace — One Memory & Control Plane",
                        font_size=20, color=GRAY_A).move_to(atomspace_rect)
        self.play(Create(atomspace_rect), FadeIn(as_label), run_time=0.7)
        self.next_slide()

        # Left: Goal-Directed Loop
        goal_rect = RoundedRectangle(
            corner_radius=0.14, width=5.2, height=3.4,
            stroke_color=BLUE_B, stroke_width=2.5, fill_opacity=0.14,
        ).move_to(LEFT * 3.5 + UP * 0.0)

        goal_steps = ["MetaMo: choose motive", "SubRep: decompose goal",
                      "PLN/MOSES: build procedure", "Execute", "Feedback"]
        goal_items = VGroup()
        for i, s in enumerate(goal_steps):
            num = Text(f"{i+1}.", font_size=16, color=BLUE_B)
            txt = Text(s, font_size=16, color=WHITE)
            row = VGroup(num, txt).arrange(RIGHT, buff=0.1)
            goal_items.add(row)
        goal_items.arrange(DOWN, aligned_edge=LEFT, buff=0.14)
        goal_title = Text("GOAL-DIRECTED LOOP", font_size=18, color=BLUE_B, weight=BOLD)
        goal_content = VGroup(goal_title, goal_items).arrange(DOWN, aligned_edge=LEFT, buff=0.18)
        goal_content.move_to(goal_rect).shift(LEFT * 0.05)

        self.play(Create(goal_rect), FadeIn(goal_content, lag_ratio=0.1), run_time=0.9)
        self.next_slide()

        # Right: Ambient Loop
        ambient_rect = RoundedRectangle(
            corner_radius=0.14, width=5.2, height=3.4,
            stroke_color=PURPLE_B, stroke_width=2.5, fill_opacity=0.14,
        ).move_to(RIGHT * 3.5 + UP * 0.0)
        ambient_comps = ["ECAN: diffuse attention", "Pattern mining", "Concept blending",
                         "Background PLN", "WILLIAM compression"]
        ambient_items = VGroup()
        for c in ambient_comps:
            d = Dot(radius=0.04, color=PURPLE_B)
            t = Text(c, font_size=16, color=WHITE)
            ambient_items.add(VGroup(d, t).arrange(RIGHT, buff=0.1))
        ambient_items.arrange(DOWN, aligned_edge=LEFT, buff=0.14)
        ambient_title = Text("AMBIENT LOOP  (continuous)", font_size=18, color=PURPLE_B, weight=BOLD)
        ambient_content = VGroup(ambient_title, ambient_items).arrange(DOWN, aligned_edge=LEFT, buff=0.18)
        ambient_content.move_to(ambient_rect).shift(LEFT * 0.05)

        self.play(Create(ambient_rect), FadeIn(ambient_content, lag_ratio=0.1), run_time=0.9)
        self.next_slide()

        # Bidirectional coupling arrows through Atomspace
        left_arrow = Arrow(goal_rect.get_right(), ambient_rect.get_left(), buff=0.08,
                           color=YELLOW_B, stroke_width=3)
        right_arrow = Arrow(ambient_rect.get_left(), goal_rect.get_right(), buff=0.08,
                            color=YELLOW_B, stroke_width=3)
        coupling_label = Text("indirect coupling\nthrough shared Atomspace",
                              font_size=16, color=YELLOW_B, line_spacing=1.2).next_to(atomspace_rect, DOWN, buff=0.2)
        self.play(Create(left_arrow), Create(right_arrow), FadeIn(coupling_label), run_time=0.8)
        self.next_slide()


# ──────────────────────────────────────────────────────────────────────────────
# 3.2 PLN — Reasoning Engine
# ──────────────────────────────────────────────────────────────────────────────

class Phase3PLNReasoningEngine(Slide):
    def construct(self):
        hdr = Text("3.5 — PLN: Probabilistic Logic Networks", font_size=32, color=GREEN_B)
        hdr.to_edge(UP, buff=0.35)
        tg = tag("Deduction · Induction · Abduction", color=GREEN_B).next_to(hdr, DOWN, buff=0.25)
        self.play(FadeIn(hdr), FadeIn(tg), run_time=0.7)

        # PLN modes
        modes = [
            ("Deduction",  "A→B, B→C  ⊢  A→C  (with propagated TV)",  GREEN_B,  LEFT * 4.0 + UP * 0.6),
            ("Induction",  "Observe A→C, A→B  ⊢  B→C  (generalize)",   TEAL_B,   RIGHT * 1.0 + UP * 0.6),
            ("Abduction",  "B→C, observe C  ⊢  B likely (hypothesis)", YELLOW_B, LEFT * 1.5 + DOWN * 0.8),
        ]
        for name, formula, col, pos in modes:
            box = RoundedRectangle(corner_radius=0.12, width=5.0, height=1.15,
                                   stroke_color=col, fill_opacity=0.18).move_to(pos)
            n = Text(name, font_size=22, color=col, weight=BOLD).move_to(box).shift(UP * 0.3)
            f = Text(formula, font_size=16, color=WHITE).move_to(box).shift(DOWN * 0.22)
            self.play(FadeIn(VGroup(box, n, f)), run_time=0.6)
        self.next_slide()

        # Factor graph PLN
        self.play(FadeOut(*self.mobjects[2:]), run_time=0.4)
        fg_title = Text("PLN on Quantale-Annotated Factor Graphs (2025)", font_size=22, color=GREEN_B)
        fg_title.next_to(tg, DOWN, buff=0.35)
        self.play(FadeIn(fg_title), run_time=0.5)

        # Variable nodes and factor nodes
        var_positions = [LEFT * 4.5 + DOWN * 0.4, LEFT * 1.8 + DOWN * 0.4,
                         RIGHT * 0.8 + DOWN * 0.4, RIGHT * 3.5 + DOWN * 0.4]
        factor_positions = [LEFT * 3.2 + DOWN * 1.5, LEFT * 0.5 + DOWN * 1.5, RIGHT * 2.2 + DOWN * 1.5]

        vars_vg = VGroup(*[
            Circle(radius=0.38, color=TEAL_B, fill_opacity=0.22).move_to(p)
            for p in var_positions
        ])
        var_labels = VGroup(*[
            Text(f"TV{i+1}", font_size=15, color=TEAL_B).move_to(var_positions[i])
            for i in range(4)
        ])
        factors_vg = VGroup(*[
            Square(side_length=0.55, color=GREEN_B, fill_opacity=0.22).move_to(p)
            for p in factor_positions
        ])
        factor_labels = VGroup(*[
            Text(f"f{i+1}", font_size=14, color=GREEN_B).move_to(factor_positions[i])
            for i in range(3)
        ])
        fg_lines = VGroup(
            Line(var_positions[0], factor_positions[0], color=GRAY_B, stroke_width=2),
            Line(var_positions[1], factor_positions[0], color=GRAY_B, stroke_width=2),
            Line(var_positions[1], factor_positions[1], color=GRAY_B, stroke_width=2),
            Line(var_positions[2], factor_positions[1], color=GRAY_B, stroke_width=2),
            Line(var_positions[2], factor_positions[2], color=GRAY_B, stroke_width=2),
            Line(var_positions[3], factor_positions[2], color=GRAY_B, stroke_width=2),
        )
        self.play(FadeIn(vars_vg, lag_ratio=0.1), FadeIn(var_labels, lag_ratio=0.1),
                  FadeIn(factors_vg, lag_ratio=0.1), FadeIn(factor_labels, lag_ratio=0.1),
                  Create(fg_lines, lag_ratio=0.08), run_time=1.0)

        msg = Text("Messages (TV pairs) propagate locally via ⊕ and ⊗ — parallelizable!",
                   font_size=19, color=YELLOW_B).to_edge(DOWN, buff=0.5)
        self.play(FadeIn(msg), run_time=0.6)

        # Message traveling animation
        msg_dot = Dot(var_positions[0], radius=0.1, color=YELLOW_B)
        self.play(FadeIn(msg_dot), run_time=0.2)
        self.play(msg_dot.animate.move_to(factor_positions[0]), run_time=0.4)
        self.play(msg_dot.animate.move_to(var_positions[1]), run_time=0.4)
        self.play(msg_dot.animate.move_to(factor_positions[1]), run_time=0.4)
        self.play(msg_dot.animate.move_to(var_positions[2]), Flash(var_positions[2], color=YELLOW_B), run_time=0.4)
        self.next_slide()


# ──────────────────────────────────────────────────────────────────────────────
# 3.3 ECAN — Attention System
# ──────────────────────────────────────────────────────────────────────────────

class Phase3ECANAttentionSystem(Slide):
    def construct(self):
        hdr = Text("3.7 — ECAN: Economic Attention Network", font_size=32, color=YELLOW_B)
        hdr.to_edge(UP, buff=0.35)
        tg = tag("STI · LTI · Wages · Rent · Diffusion", color=YELLOW_B).next_to(hdr, DOWN, buff=0.25)
        self.play(FadeIn(hdr), FadeIn(tg), run_time=0.7)

        # Economy metaphor
        analogy = Text(
            "ECAN treats attention as currency: atoms earn wages, pay rent,\n"
            "and diffuse wealth to neighbors — a cognitive economy.",
            font_size=22, color=WHITE, line_spacing=1.3,
        ).next_to(tg, DOWN, buff=0.35)
        self.play(FadeIn(analogy), run_time=0.7)
        self.next_slide()

        # STI / LTI diagram
        self.play(FadeOut(analogy), run_time=0.4)
        sti_box = RoundedRectangle(corner_radius=0.12, width=4.5, height=2.0,
                                    stroke_color=YELLOW_B, fill_opacity=0.18).move_to(LEFT * 3.2 + DOWN * 0.2)
        sti_t = Text("STI\nShort-Term Importance", font_size=20, color=YELLOW_B,
                     line_spacing=1.2, weight=BOLD).move_to(sti_box).shift(UP * 0.4)
        sti_d = Text("Fast-changing · set by recent activity\nDrives immediate computation",
                     font_size=16, color=WHITE, line_spacing=1.2).move_to(sti_box).shift(DOWN * 0.35)

        lti_box = RoundedRectangle(corner_radius=0.12, width=4.5, height=2.0,
                                    stroke_color=ORANGE, fill_opacity=0.18).move_to(RIGHT * 3.2 + DOWN * 0.2)
        lti_t = Text("LTI\nLong-Term Importance", font_size=20, color=ORANGE,
                     line_spacing=1.2, weight=BOLD).move_to(lti_box).shift(UP * 0.4)
        lti_d = Text("Slow-changing · accumulated value\nDetermines memory persistence",
                     font_size=16, color=WHITE, line_spacing=1.2).move_to(lti_box).shift(DOWN * 0.35)

        self.play(FadeIn(sti_box), FadeIn(sti_t), FadeIn(sti_d), run_time=0.7)
        self.play(FadeIn(lti_box), FadeIn(lti_t), FadeIn(lti_d), run_time=0.7)
        self.next_slide()

        # Fluid-dynamic ECAN (2025 upgrade)
        fluid_panel = panel(
            "2025 Upgrade: Fluid-Dynamic ECAN",
            ["Attention modeled as incompressible fluid  ρ(t,x)",
             "Governed by Navier-Stokes + Hamilton-Jacobi-Bellman",
             "∇·u = 0  (budget conservation as incompressibility)",
             "ShardZipper extracts sub-tries for GPU advection kernels",
             "Result: optimal transport of cognitive resources"],
            width=10.5, tc=TEAL_B,
        ).to_edge(DOWN, buff=0.22)
        self.play(FadeIn(fluid_panel, shift=UP * 0.1), run_time=0.8)
        self.next_slide()


# ──────────────────────────────────────────────────────────────────────────────
# 3.4 MOSES / GEO-EVO — Program Learning
# ──────────────────────────────────────────────────────────────────────────────

class Phase3MOSESGeoEvo(Slide):
    def construct(self):
        hdr = Text("3.6 — MOSES / GEO-EVO: Evolutionary Program Learning", font_size=28, color=ORANGE)
        hdr.to_edge(UP, buff=0.35)
        tg = tag("EDA · Demes · Geodesic Two-Ended Search", color=ORANGE).next_to(hdr, DOWN, buff=0.25)
        self.play(FadeIn(hdr), FadeIn(tg), run_time=0.7)

        # Program space with evolutionary landscape
        axes = Axes(
            x_range=[-3, 3, 1], y_range=[0, 1, 0.5],
            x_length=8, y_length=3.5,
            axis_config={"color": GRAY_B},
        ).move_to(DOWN * 0.5)
        fitness_curve = axes.plot(lambda x: 0.8 * np.exp(-0.5 * (x - 1.2) ** 2) + 0.1 * np.exp(-0.5 * (x + 2) ** 2),
                                  color=ORANGE, stroke_width=3)
        xlabel = Text("Program Space", font_size=18, color=GRAY_A).next_to(axes, DOWN, buff=0.2)
        ylabel = Text("Fitness", font_size=18, color=GRAY_A).rotate(PI / 2).next_to(axes, LEFT, buff=0.2)

        self.play(Create(axes), Create(fitness_curve), FadeIn(xlabel), FadeIn(ylabel), run_time=1.0)
        self.next_slide()

        # Population demes
        deme_positions = [axes.c2p(-2.0, 0.18), axes.c2p(0.0, 0.45), axes.c2p(1.2, 0.88)]
        deme_colors = [BLUE_B, TEAL_B, GREEN_B]
        for pos, col in zip(deme_positions, deme_colors):
            for _ in range(5):
                offset = np.array([np.random.uniform(-0.3, 0.3), np.random.uniform(-0.1, 0.1), 0])
                d = Dot(pos + offset, radius=0.07, color=col)
                self.add(d)

        # GEO-EVO bidirectional arrows
        forward = Arrow(axes.c2p(-2.0, 0.5), axes.c2p(1.2, 0.5), color=GREEN_B, stroke_width=4)
        backward = Arrow(axes.c2p(1.2, 0.65), axes.c2p(-2.0, 0.65), color=YELLOW_B, stroke_width=4)
        fwd_t = Text("forward (reachability)", font_size=15, color=GREEN_B).next_to(forward, UP, buff=0.08)
        bwd_t = Text("backward (goal)", font_size=15, color=YELLOW_B).next_to(backward, DOWN, buff=0.08)
        self.play(GrowArrow(forward), GrowArrow(backward), FadeIn(fwd_t), FadeIn(bwd_t), run_time=0.8)
        self.next_slide()

        detail = panel("MOSES / GEO-EVO mechanics",
                       ["EDA: estimation of distribution algorithms for smart mutation",
                        "Demes: local 'islands' of similar programs in program space",
                        "GEO-EVO: forward f(x) + backward g(x) guidance → meet at minimum effort",
                        "Programs stored as Atoms in MORK — deduplicated automatically",
                        "PLN subgoals bias evolutionary search direction"],
                       width=10.5, tc=ORANGE).to_edge(DOWN, buff=0.22)
        self.play(FadeIn(detail, shift=UP * 0.08), run_time=0.8)
        self.next_slide()


# ──────────────────────────────────────────────────────────────────────────────
# 3.5 WILLIAM — Compression Intelligence
# ──────────────────────────────────────────────────────────────────────────────

class Phase3WILLIAMCompression(Slide):
    def construct(self):
        hdr = Text("3.8 — WILLIAM: Compression-Driven Learning", font_size=32, color=PURPLE_B)
        hdr.to_edge(UP, buff=0.35)
        tg = tag("MDL Principle · Pattern Extraction · Template Formation", color=PURPLE_B).next_to(hdr, DOWN, buff=0.25)
        self.play(FadeIn(hdr), FadeIn(tg), run_time=0.7)

        # MDL intuition
        mdl = Text(
            "MDL (Minimum Description Length):\n"
            "  The best model = the shortest encoding of data + model.",
            font_size=23, color=WHITE, line_spacing=1.3,
        ).next_to(tg, DOWN, buff=0.35)
        self.play(FadeIn(mdl), run_time=0.7)
        self.next_slide()

        # WILLIAM pipeline
        boxes = VGroup(
            lbox("Raw Atom Stream\n(Atomspace)", WHITE, 17, 2.8),
            lbox("Find frequent\nsub-patterns", PURPLE_B, 17, 2.8),
            lbox("Measure\ncompression gain", TEAL_B, 17, 2.8),
            lbox("Promote to\nTemplate Atom", GREEN_B, 17, 2.8),
        ).arrange(RIGHT, buff=0.3).move_to(DOWN * 0.5)
        arrows = VGroup(*[Arrow(boxes[i].get_right(), boxes[i+1].get_left(), buff=0.05, stroke_width=4)
                          for i in range(3)])
        self.play(FadeOut(mdl), FadeIn(boxes, lag_ratio=0.12), Create(arrows), run_time=1.0)
        self.next_slide()

        # What WILLIAM unlocks
        unlocks = panel("WILLIAM on MORK — What it unlocks",
                        ["Heavy-hitter iterators: O(1) find top-k patterns globally",
                         "Guides PLN: prioritize inference on high-compression subgraphs",
                         "Guides ECAN: compress = importance → focus compute there",
                         "Neural acceleration: identify which attention heads matter",
                         "MOSES EDA: use compression patterns as mutation bias"],
                        width=10.5, tc=PURPLE_B).to_edge(DOWN, buff=0.22)
        self.play(FadeIn(unlocks, shift=UP * 0.1), run_time=0.8)
        self.next_slide()


# ──────────────────────────────────────────────────────────────────────────────
# 3.6 Pattern Mining & Concept Blending
# ──────────────────────────────────────────────────────────────────────────────

class Phase3PatternMiningBlending(Slide):
    def construct(self):
        hdr = Text("3.9 — Pattern Mining & Concept Blending", font_size=31, color=TEAL_B)
        hdr.to_edge(UP, buff=0.35)
        tg = tag("Creativity via Structural Merging", color=TEAL_B).next_to(hdr, DOWN, buff=0.25)
        self.play(FadeIn(hdr), FadeIn(tg), run_time=0.7)

        # Pattern mining pipeline
        pm_steps = ["Generate abstract\ntemplates", "Specialize\n(add constraints)", "Filter by\nsupport count",
                    "Rank by\nI-surprisingness", "Store as\nTemplate Atom"]
        pm_boxes = VGroup(*[lbox(s, TEAL_B, 16, 2.2) for s in pm_steps]).arrange(RIGHT, buff=0.2).move_to(UP * 0.5)
        pm_arrows = VGroup(*[Arrow(pm_boxes[i].get_right(), pm_boxes[i+1].get_left(), buff=0.05, stroke_width=3)
                             for i in range(4)])
        pm_title = Text("Pattern Mining stream pipeline", font_size=20, color=TEAL_B).next_to(pm_boxes, UP, buff=0.2)
        self.play(FadeIn(pm_title), FadeIn(pm_boxes, lag_ratio=0.1), Create(pm_arrows), run_time=1.0)
        self.next_slide()

        # Concept blending
        src_a = lbox("Garden\n(plants, growth, beauty)", col=GREEN_B, font=16, width=3.0).move_to(LEFT * 3.8 + DOWN * 1.2)
        src_b = lbox("Sky / Aerial\n(height, aviation, view)", col=BLUE_B, font=16, width=3.0).move_to(LEFT * 0.5 + DOWN * 1.2)
        blend = lbox("🌿 Sky-Garden\n(aerial botanical platform!)", col=YELLOW_B, font=16, width=3.2).move_to(RIGHT * 3.0 + DOWN * 1.2)
        a1 = Arrow(src_a.get_right(), blend.get_left(), buff=0.08, color=YELLOW_B, stroke_width=3)
        a2 = Arrow(src_b.get_right(), blend.get_left(), buff=0.08, color=YELLOW_B, stroke_width=3)
        blend_title = Text("Concept Blending: transport path in concept space", font_size=18, color=YELLOW_B).next_to(src_a, DOWN, buff=1.2).shift(RIGHT * 1.5)
        self.play(FadeIn(src_a, src_b, blend), GrowArrow(a1), GrowArrow(a2), FadeIn(blend_title), run_time=1.0)
        self.next_slide()

        detail = panel("Pattern Mining + Blending",
                       ["I-surprisingness = frequent yet not obvious from sub-patterns",
                        "Streaming — never materializes full result set (trillion-edge OK)",
                        "Output feeds PLN (inference templates) and neural Symbolic Heads",
                        "Concept blending: TransWeave finds minimum-cost merge path",
                        "Results = first-class Atoms → auditable, reusable"],
                       width=10.5, tc=TEAL_B).to_edge(DOWN, buff=0.22)
        self.play(FadeIn(detail, shift=UP * 0.1), run_time=0.8)
        self.next_slide()
