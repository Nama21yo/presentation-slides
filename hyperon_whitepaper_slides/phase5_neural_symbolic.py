"""
Phase 5 — Neural-Symbolic Integration
Covers: Outside Mode (Symbolic Heads) · Inside Mode (QuantiMORK)
         Wavelet representation · Predictive Coding without backprop
         Commutativity regularization · Selective Refinement · WILLIAM neural efficiency
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
# 5.1 Integration Problem Overview
# ──────────────────────────────────────────────────────────────────────────────

class Phase5IntegrationProblem(Slide):
    def construct(self):
        hdr = Text("The Neural-Symbolic Integration Problem", font_size=29, color=BLUE_B)
        hdr.to_edge(UP, buff=0.35)
        tg = tag("Two worlds that must become one", color=BLUE_B).next_to(hdr, DOWN, buff=0.25)
        self.play(FadeIn(hdr), FadeIn(tg), run_time=0.7)

        # Two columns
        sym_box = RoundedRectangle(corner_radius=0.14, width=4.8, height=4.0,
                                    stroke_color=TEAL_B, fill_opacity=0.14).move_to(LEFT * 3.2)
        sym_title = Text("Symbolic Systems", font_size=22, color=TEAL_B, weight=BOLD).move_to(sym_box).shift(UP * 1.6)
        sym_pros = VGroup(*[
            Text("✓ " + s, font_size=17, color=WHITE) for s in
            ["Explicit reasoning", "Auditable steps", "Compositional", "Structured memory"]
        ]).arrange(DOWN, aligned_edge=LEFT, buff=0.18).move_to(sym_box).shift(UP * 0.4)
        sym_cons = VGroup(*[
            Text("✗ " + s, font_size=17, color=RED_B) for s in
            ["Brittle rules", "Cannot generalize", "No perception"]
        ]).arrange(DOWN, aligned_edge=LEFT, buff=0.18).move_to(sym_box).shift(DOWN * 1.1)

        neu_box = RoundedRectangle(corner_radius=0.14, width=4.8, height=4.0,
                                    stroke_color=PURPLE_B, fill_opacity=0.14).move_to(RIGHT * 3.2)
        neu_title = Text("Neural Networks", font_size=22, color=PURPLE_B, weight=BOLD).move_to(neu_box).shift(UP * 1.6)
        neu_pros = VGroup(*[
            Text("✓ " + s, font_size=17, color=WHITE) for s in
            ["Pattern recognition", "Robust to noise", "Learns from data", "Fluent generation"]
        ]).arrange(DOWN, aligned_edge=LEFT, buff=0.18).move_to(neu_box).shift(UP * 0.4)
        neu_cons = VGroup(*[
            Text("✗ " + s, font_size=17, color=RED_B) for s in
            ["Black box", "No structure", "Hallucination"]
        ]).arrange(DOWN, aligned_edge=LEFT, buff=0.18).move_to(neu_box).shift(DOWN * 1.1)

        self.play(FadeIn(sym_box), FadeIn(sym_title, sym_pros, sym_cons), run_time=0.8)
        self.play(FadeIn(neu_box), FadeIn(neu_title, neu_pros, neu_cons), run_time=0.8)
        self.next_slide()

        # Hyperon solution
        solution = lbox("Hyperon: share the SAME Atomspace substrate\n"
                        "→ neural activations = Atoms  ·  rules orchestrate neural compute",
                        col=YELLOW_B, font=20, width=10.5, pad=0.28).to_edge(DOWN, buff=0.25)
        self.play(FadeIn(solution, shift=UP * 0.1), run_time=0.7)
        self.next_slide()


# ──────────────────────────────────────────────────────────────────────────────
# 5.2 Outside Mode — Symbolic Heads
# ──────────────────────────────────────────────────────────────────────────────

class Phase5OutsideMode(Slide):
    def construct(self):
        hdr = Text("Outside Mode: Symbolic Heads on Transformers", font_size=27, color=GREEN_B)
        hdr.to_edge(UP, buff=0.35)
        tg = tag("Wrap existing LLMs · Extract outputs as Atoms", color=GREEN_B).next_to(hdr, DOWN, buff=0.25)
        self.play(FadeIn(hdr), FadeIn(tg), run_time=0.7)

        # Transformer diagram with Symbolic Head
        # Transformer tower
        layers_t = VGroup(*[
            RoundedRectangle(corner_radius=0.08, width=2.5, height=0.6,
                             stroke_color=GRAY_B, fill_opacity=0.2).move_to(LEFT * 2.5 + UP * (1.5 - i * 0.72))
            for i in range(5)
        ])
        layer_labels = VGroup(*[
            Text(f"Attn+FFN {5-i}", font_size=14, color=GRAY_A).move_to(layers_t[i])
            for i in range(5)
        ])
        self.play(FadeIn(layers_t, lag_ratio=0.1), FadeIn(layer_labels, lag_ratio=0.1), run_time=0.8)

        # Symbolic Head module
        sym_head = RoundedRectangle(corner_radius=0.12, width=3.5, height=2.4,
                                     stroke_color=GREEN_B, stroke_width=2.5,
                                     fill_color=GREEN_E, fill_opacity=0.14).move_to(RIGHT * 2.8 + UP * 0.3)
        sh_title = Text("Symbolic Head", font_size=19, color=GREEN_B, weight=BOLD).move_to(sym_head).shift(UP * 0.8)
        sh_steps = VGroup(
            Text("1. Project h_i → query q_i", font_size=14, color=WHITE),
            Text("2. Retrieve top-m templates", font_size=14, color=WHITE),
            Text("   from MORK Atomspace", font_size=14, color=GRAY_A),
            Text("3. Attention over templates", font_size=14, color=WHITE),
            Text("4. Inject into hidden state", font_size=14, color=WHITE),
        ).arrange(DOWN, aligned_edge=LEFT, buff=0.1).move_to(sym_head).shift(DOWN * 0.2)
        self.play(FadeIn(sym_head, sh_title, sh_steps), run_time=0.8)

        # Arrow from transformer to symbolic head
        link_arrow = Arrow(layers_t[2].get_right(), sym_head.get_left(),
                           buff=0.08, color=GREEN_B, stroke_width=3)
        self.play(GrowArrow(link_arrow), run_time=0.5)

        # MORK template source
        mork_box = lbox("MORK\nTemplate Store\n(WILLIAM-mined patterns)", GREEN_B, 16, 3.0).move_to(RIGHT * 4.5 + DOWN * 2.0)
        mork_arrow = Arrow(mork_box.get_top(), sym_head.get_bottom(), buff=0.08, color=GREEN_B, stroke_width=3)
        self.play(FadeIn(mork_box), GrowArrow(mork_arrow), run_time=0.6)
        self.next_slide()

        props = panel("Symbolic Heads — benefits",
                      ["No modification to existing LLM weights required",
                       "Adds structured memory (templates, rules) to continuous attention",
                       "Templates sourced from WILLIAM pattern mining — keeps fresh",
                       "LLM output automatically grounded in Atomspace knowledge",
                       "Weakness regularization prevents destabilizing existing model"],
                      width=10.5, tc=GREEN_B).to_edge(DOWN, buff=0.22)
        self.play(FadeIn(props, shift=UP * 0.1), run_time=0.8)
        self.next_slide()


# ──────────────────────────────────────────────────────────────────────────────
# 5.3 Inside Mode — QuantiMORK
# ──────────────────────────────────────────────────────────────────────────────

class Phase5QuantiMORK(Slide):
    def construct(self):
        hdr = Text("Inside Mode: QuantiMORK Architecture", font_size=29, color=PURPLE_B)
        hdr.to_edge(UP, buff=0.35)
        tg = tag("Wavelet Atoms · Neural Nets INSIDE Atomspace", color=PURPLE_B).next_to(hdr, DOWN, buff=0.25)
        self.play(FadeIn(hdr), FadeIn(tg), run_time=0.7)

        # Wavelet decomposition hierarchy ↔ PathMap hierarchy
        comparison = Text(
            "Key insight: Discrete Wavelet Transform produces a hierarchy.\n"
            "MORK PathMap IS a hierarchy (prefix trie).\n"
            "→ Wavelet coefficients map naturally to PathMap nodes!",
            font_size=21, color=YELLOW_B, line_spacing=1.35,
        ).next_to(tg, DOWN, buff=0.35)
        self.play(FadeIn(comparison), run_time=0.7)
        self.next_slide()

        # Side-by-side: wavelet tree vs PathMap tree
        self.play(FadeOut(comparison), run_time=0.4)

        # Wavelet tree (left)
        wt_nodes = {
            "L0": np.array([-5.0, 1.5, 0]),
            "L1a": np.array([-6.0, 0.5, 0]),
            "L1b": np.array([-4.0, 0.5, 0]),
            "L2a": np.array([-6.5, -0.5, 0]),
            "L2b": np.array([-5.5, -0.5, 0]),
            "L2c": np.array([-4.5, -0.5, 0]),
            "L2d": np.array([-3.5, -0.5, 0]),
        }
        colors_wt = {"L0": WHITE, "L1a": TEAL_B, "L1b": TEAL_B,
                     "L2a": BLUE_B, "L2b": BLUE_B, "L2c": BLUE_B, "L2d": BLUE_B}
        wt_labels = {"L0": "coarse", "L1a": "mid A", "L1b": "mid B",
                     "L2a": "fine 1", "L2b": "fine 2", "L2c": "fine 3", "L2d": "fine 4"}
        wt_group = VGroup()
        for key, pos in wt_nodes.items():
            c = Circle(radius=0.28, color=colors_wt[key], fill_opacity=0.22).move_to(pos)
            t = Text(wt_labels[key], font_size=12, color=colors_wt[key]).move_to(c)
            wt_group.add(VGroup(c, t))
        for parent, child in [("L0","L1a"),("L0","L1b"),("L1a","L2a"),("L1a","L2b"),
                               ("L1b","L2c"),("L1b","L2d")]:
            wt_group.add(Line(wt_nodes[parent], wt_nodes[child], color=GRAY_B, stroke_width=2.0))
        wt_title = Text("Wavelet Hierarchy", font_size=18, color=TEAL_B).move_to([-5.0, 2.1, 0])

        # PathMap (right)
        pm_nodes = {
            "r": np.array([2.0, 1.5, 0]),
            "0": np.array([1.0, 0.5, 0]),
            "1": np.array([3.0, 0.5, 0]),
            "00": np.array([0.5, -0.5, 0]),
            "01": np.array([1.5, -0.5, 0]),
            "10": np.array([2.5, -0.5, 0]),
            "11": np.array([3.5, -0.5, 0]),
        }
        colors_pm = {"r": WHITE, "0": PURPLE_B, "1": PURPLE_B,
                     "00": GREEN_B, "01": GREEN_B, "10": GREEN_B, "11": GREEN_B}
        pm_group = VGroup()
        for key, pos in pm_nodes.items():
            c = Circle(radius=0.28, color=colors_pm[key], fill_opacity=0.22).move_to(pos)
            t = Text(key, font_size=12, color=colors_pm[key]).move_to(c)
            pm_group.add(VGroup(c, t))
        for parent, child in [("r","0"),("r","1"),("0","00"),("0","01"),
                               ("1","10"),("1","11")]:
            pm_group.add(Line(pm_nodes[parent], pm_nodes[child], color=GRAY_B, stroke_width=2.0))
        pm_title = Text("MORK PathMap", font_size=18, color=PURPLE_B).move_to([2.0, 2.1, 0])

        self.play(FadeIn(wt_group, lag_ratio=0.04), FadeIn(wt_title), run_time=0.9)
        self.play(FadeIn(pm_group, lag_ratio=0.04), FadeIn(pm_title), run_time=0.9)

        # Bidirectional mapping arrow
        map_arrow = DoubleArrow(np.array([-3.0, 0.5, 0]), np.array([0.5, 0.5, 0]),
                                 color=YELLOW_B, stroke_width=4)
        map_label = Text("natural\nmapping", font_size=16, color=YELLOW_B, line_spacing=1.1)
        map_label.move_to(np.array([-1.2, 0.9, 0]))
        self.play(Create(map_arrow), FadeIn(map_label), run_time=0.6)
        self.next_slide()

        detail = panel("QuantiMORK Architecture",
                       ["Tensors encoded as wavelet-structured multiresolution DAGs in MORK",
                        "gpu-conv / gpu-attn / gpu-backprop work on PathMap subtrees directly",
                        "MeTTa rules schedule: where to refine, when to consolidate",
                        "Intra-scale attention + sparse cross-scale fusion",
                        "Pattern mining discovers features → immediate attention targets"],
                       width=10.5, tc=PURPLE_B).to_edge(DOWN, buff=0.22)
        self.play(FadeIn(detail, shift=UP * 0.1), run_time=0.8)
        self.next_slide()


# ──────────────────────────────────────────────────────────────────────────────
# 5.6 Predictive Coding Without Backprop
# ──────────────────────────────────────────────────────────────────────────────

class Phase5PCNoBprop(Slide):
    def construct(self):
        hdr = Text("Predictive Coding in QuantiMORK", font_size=31, color=TEAL_B)
        hdr.to_edge(UP, buff=0.35)
        tg = tag("Local updates · Asynchronous · No global backward pass", color=TEAL_B).next_to(hdr, DOWN, buff=0.25)
        self.play(FadeIn(hdr), FadeIn(tg), run_time=0.7)

        # Wavelet layer animation: top-down predictions + bottom-up error
        layer_names = ["Level 3 (coarse)", "Level 2", "Level 1", "Level 0 (fine)"]
        layer_ys = [1.8, 0.8, -0.2, -1.2]
        layer_rects = VGroup(*[
            RoundedRectangle(corner_radius=0.1, width=8.0, height=0.65,
                             stroke_color=TEAL_B, fill_opacity=0.18).move_to(UP * y)
            for y in layer_ys
        ])
        layer_labels = VGroup(*[
            Text(n, font_size=16, color=TEAL_B).move_to(UP * layer_ys[i]).shift(LEFT * 3.2)
            for i, n in enumerate(layer_names)
        ])
        self.play(FadeIn(layer_rects, lag_ratio=0.1), FadeIn(layer_labels, lag_ratio=0.1), run_time=0.8)

        # Prediction arrows (top-down, blue)
        for i in range(3):
            arr = Arrow(layer_rects[i].get_bottom() + RIGHT * 1.0,
                       layer_rects[i+1].get_top() + RIGHT * 1.0,
                       buff=0.05, color=BLUE_B, stroke_width=3.5,
                       max_tip_length_to_length_ratio=0.18)
            self.add(arr)
        pred_lbl = Text("prediction ↓", font_size=16, color=BLUE_B).to_edge(RIGHT, buff=0.4).shift(UP * 0.4)
        self.play(FadeIn(pred_lbl), run_time=0.3)

        # Error arrows (bottom-up, orange)
        for i in range(3):
            arr = Arrow(layer_rects[i+1].get_top() + LEFT * 1.0,
                       layer_rects[i].get_bottom() + LEFT * 1.0,
                       buff=0.05, color=ORANGE, stroke_width=3.5,
                       max_tip_length_to_length_ratio=0.18)
            self.add(arr)
        err_lbl = Text("error ↑", font_size=16, color=ORANGE).to_edge(RIGHT, buff=0.4).shift(DOWN * 0.4)
        self.play(FadeIn(err_lbl), run_time=0.3)

        # Local update annotation
        for i, y in enumerate(layer_ys):
            dot = Dot([3.5, y, 0], radius=0.1, color=GREEN_B)
            update_t = Text(f"Local Δw_{i}", font_size=12, color=GREEN_B).next_to(dot, RIGHT, buff=0.1)
            self.play(FadeIn(VGroup(dot, update_t)), run_time=0.25)
        self.next_slide()

        # Commutativity regularization
        comm_box = lbox(
            "Commutativity Regularization (2025 addition)\n"
            "  If update A then B ≈ B then A  →  disentangled representations\n"
            "  Penalty: L_comm = ||A∘B - B∘A||²  added to training loss",
            col=YELLOW_B, font=18, width=10.5, pad=0.28,
        ).to_edge(DOWN, buff=0.35)
        self.play(FadeIn(comm_box, shift=UP * 0.1), run_time=0.7)
        self.next_slide()

        props = panel("PC in QuantiMORK — advantages",
                      ["Selective refinement: expand only where error is high",
                       "Different layers update asynchronously — no synchronization lock",
                       "Symbolic rules intervene at any wavelet level",
                       "Memory scales with active regions, not total model size",
                       "Naturally supports continual learning (no catastrophic forgetting)"],
                      width=10.5, tc=TEAL_B).to_edge(DOWN, buff=0.22)
        self.play(FadeOut(comm_box), FadeIn(props, shift=UP * 0.1), run_time=0.8)
        self.next_slide()


# ──────────────────────────────────────────────────────────────────────────────
# 5.7 Selective Refinement + WILLIAM Neural Efficiency
# ──────────────────────────────────────────────────────────────────────────────

class Phase5SelectiveRefinementWILLIAM(Slide):
    def construct(self):
        hdr = Text("Selective Refinement & WILLIAM Neural Efficiency",
                   font_size=26, color=PURPLE_B)
        hdr.to_edge(UP, buff=0.35)
        tg = tag("Sparsity · Pruning · Heavy-Hitter Selection", color=PURPLE_B).next_to(hdr, DOWN, buff=0.25)
        self.play(FadeIn(hdr), FadeIn(tg), run_time=0.7)

        # Dense vs Selective compute grid
        grid_title_d = Text("Dense (Standard):", font_size=20, color=RED_B).move_to(LEFT * 3.5 + UP * 1.5)
        grid_title_s = Text("Selective (QuantiMORK):", font_size=20, color=GREEN_B).move_to(RIGHT * 2.8 + UP * 1.5)
        self.play(FadeIn(grid_title_d), FadeIn(grid_title_s), run_time=0.5)

        # Dense grid: all cells lit
        dense_cells = VGroup()
        for row in range(4):
            for col in range(4):
                c = Square(side_length=0.38, color=RED_B, fill_opacity=0.4)
                c.move_to(LEFT * 4.8 + RIGHT * col * 0.42 + DOWN * row * 0.42)
                dense_cells.add(c)
        self.play(FadeIn(dense_cells, lag_ratio=0.02), run_time=0.7)

        # Selective grid: only high-error regions lit
        selective_cells = VGroup()
        highlight = {(0,0),(0,1),(1,0),(2,3),(3,2),(3,3)}
        for row in range(4):
            for col in range(4):
                is_active = (row, col) in highlight
                c = Square(side_length=0.38,
                           color=GREEN_B if is_active else GRAY_E,
                           fill_opacity=0.55 if is_active else 0.1)
                c.move_to(RIGHT * 1.4 + RIGHT * col * 0.42 + DOWN * row * 0.42)
                selective_cells.add(c)
        self.play(FadeIn(selective_cells, lag_ratio=0.02), run_time=0.7)

        savings = Text("Compute only where error > threshold → 25–50% FLOP savings",
                       font_size=20, color=GREEN_B).to_edge(DOWN, buff=1.5)
        self.play(FadeIn(savings), run_time=0.5)
        self.next_slide()

        # WILLIAM + neural
        self.play(FadeOut(*self.mobjects[2:]), run_time=0.4)
        william_flow = VGroup(
            lbox("MORK trie nodes\ntrack compression stats", PURPLE_B, 17, 3.0).move_to(LEFT * 4.5 + UP * 0.3),
            lbox("iter_prefix_topk(k)\nHeavy-hitter iterator", TEAL_B, 17, 3.0).move_to(LEFT * 0.8 + UP * 0.3),
            lbox("→ Active attention\nheads identified", GREEN_B, 17, 3.0).move_to(RIGHT * 3.0 + UP * 0.3),
        )
        w_arrows = VGroup(*[Arrow(william_flow[i].get_right(), william_flow[i+1].get_left(),
                                  buff=0.06, stroke_width=4) for i in range(2)])
        w_title = Text("WILLIAM-guided neural efficiency pipeline", font_size=21, color=PURPLE_B).to_edge(UP, buff=2.2)
        self.play(FadeIn(w_title), FadeIn(william_flow, lag_ratio=0.12), Create(w_arrows), run_time=1.0)

        outcomes = VGroup(
            lbox("Prune low-value\nfrequency bands", ORANGE, 16, 2.8).move_to(LEFT * 3.8 + DOWN * 1.6),
            lbox("Boost high-info\nattention heads", GREEN_B, 16, 2.8).move_to(ORIGIN + DOWN * 1.6),
            lbox("Trigger on-demand\nrefinement", YELLOW_B, 16, 2.8).move_to(RIGHT * 3.8 + DOWN * 1.6),
        )
        self.play(FadeIn(outcomes, lag_ratio=0.12), run_time=0.8)
        self.next_slide()

        summary = panel("Neural-Symbolic Synergy Summary",
                        ["Outside: LLMs wrapped as Spaces + Symbolic Heads add structure",
                         "Inside: QuantiMORK — tensors live IN the Atomspace natively",
                         "PC updates locally; WAS schedules; rules orchestrate refinement",
                         "WILLIAM compresses → finds what matters → guides neural sparsity",
                         "Commutativity regularization → stable continual learning",
                         "Both modes share same Atoms, evaluation metrics, control signals"],
                        width=10.5, tc=BLUE_B).to_edge(DOWN, buff=0.22)
        self.play(FadeIn(summary, shift=UP * 0.1), run_time=0.8)
        self.next_slide()
