"""
Phase 4 — Advanced PRIMUS (Layer 3 Additions)
Covers: Weakness Theory · Geodesic Control · MetaMo · SubRep
         TransWeave · Algorithmic Chemistry · Schrödinger Bridge Learning
"""
from manim import *
from manim_slides import Slide
import numpy as np


# ──────────────────────────────────────────────────────────────────────────────
# Shared helpers
# ──────────────────────────────────────────────────────────────────────────────

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


def section_header(title, color=BLUE_B, sub=None):
    hdr = Text(title, font_size=32, color=color)
    hdr.to_edge(UP, buff=0.35)
    if sub:
        tg = tag(sub, color=color).next_to(hdr, DOWN, buff=0.25)
        return hdr, tg
    return hdr


# ──────────────────────────────────────────────────────────────────────────────
# 4.1 Weakness Theory
# ──────────────────────────────────────────────────────────────────────────────

class Phase4WeaknessTheory(Slide):
    def construct(self):
        hdr = Text("Weakness Theory: The Mathematics of Simplicity",
                   font_size=28, color=PURPLE_B)
        hdr.to_edge(UP, buff=0.35)
        tg = tag("Quantale-based Occam's Razor", color=PURPLE_B).next_to(hdr, DOWN, buff=0.25)
        self.play(FadeIn(hdr), FadeIn(tg), run_time=0.7)

        # Core idea
        core = Text(
            "Weakness = how much two hypotheses FAIL to be distinguished.\n"
            "Weaker hypothesis → true in more possible worlds → generalizes better.",
            font_size=21, color=WHITE, line_spacing=1.35,
        ).next_to(tg, DOWN, buff=0.35)
        self.play(FadeIn(core), run_time=0.7)
        self.next_slide()

        # Venn diagram: hypothesis A (narrow) vs B (weak/broad)
        self.play(FadeOut(core), run_time=0.4)
        world_circle = Circle(radius=2.2, color=GRAY_B, fill_opacity=0.1)
        world_label = Text("All Possible Worlds", font_size=18, color=GRAY_B).next_to(world_circle, UP, buff=0.1)
        hyp_a = Circle(radius=0.7, color=RED_B, fill_opacity=0.28).move_to(RIGHT * 0.8)
        hyp_b = Circle(radius=1.6, color=GREEN_B, fill_opacity=0.18)
        ha_label = Text("H_A\n(strong)", font_size=17, color=RED_B).move_to(hyp_a)
        hb_label = Text("H_B\n(weak)", font_size=17, color=GREEN_B).move_to(LEFT * 0.9 + DOWN * 0.5)
        self.play(Create(world_circle), FadeIn(world_label), run_time=0.5)
        self.play(Create(hyp_b), FadeIn(hb_label), run_time=0.5)
        self.play(Create(hyp_a), FadeIn(ha_label), run_time=0.5)

        arrow_note = Text("H_B explains same data\nbut rules out less → weaker → preferred",
                          font_size=18, color=GREEN_B, line_spacing=1.2)
        arrow_note.to_edge(RIGHT, buff=0.3).shift(UP * 0.5)
        arr = Arrow(arrow_note.get_left(), hyp_b.get_right(), buff=0.1, color=GREEN_B, stroke_width=3)
        self.play(FadeIn(arrow_note), GrowArrow(arr), run_time=0.7)
        self.next_slide()

        # Cross-module table
        self.play(FadeOut(*self.mobjects[2:]), run_time=0.4)
        rows = [
            ("PLN logic",         "Prefer rules that leave more worlds open",         "Heyting ops in quantale"),
            ("SVM margins",       "Prefer larger safe margin",                         "Margin = weakness metric"),
            ("Neural networks",   "Commutativity + monotonicity of updates",           "Residuation penalty"),
            ("MOSES programs",    "Prefer shorter / more compositional programs",      "MDL + quantale length"),
            ("Schrödinger bridge","Follow path of minimum representational effort",    "Bridge quantale geodesic"),
        ]
        col_headers = ["Module", "What 'weakness' means", "Quantale instantiation"]
        header_row = VGroup(*[
            Text(h, font_size=19, color=YELLOW_B, weight=BOLD) for h in col_headers
        ]).arrange(RIGHT, buff=0.5)
        header_row.to_edge(UP, buff=2.0)
        self.play(FadeIn(header_row), run_time=0.5)

        table_vg = VGroup()
        colors_row = [PURPLE_B, TEAL_B, GREEN_B, ORANGE, BLUE_B]
        for i, (mod, meaning, quant) in enumerate(rows):
            row_vg = VGroup(
                Text(mod,     font_size=17, color=colors_row[i]),
                Text(meaning, font_size=17, color=WHITE),
                Text(quant,   font_size=17, color=GRAY_A),
            ).arrange(RIGHT, buff=0.5)
            row_vg.next_to(header_row, DOWN, buff=0.2 + i * 0.52)
            table_vg.add(row_vg)
        for row in table_vg:
            self.play(FadeIn(row, shift=RIGHT * 0.08), run_time=0.4)

        insight = lbox("Same 'prefer weakness' bias → uniform Occam's razor across all PRIMUS modules",
                        col=YELLOW_B, font=19, width=11.0, pad=0.22).to_edge(DOWN, buff=0.22)
        self.play(FadeIn(insight, shift=UP * 0.1), run_time=0.6)
        self.next_slide()


# ──────────────────────────────────────────────────────────────────────────────
# 4.2 Geodesic Inference and Control
# ──────────────────────────────────────────────────────────────────────────────

class Phase4GeodesicControl(Slide):
    def construct(self):
        hdr = Text("Geodesic Inference and Control", font_size=32, color=TEAL_B)
        hdr.to_edge(UP, buff=0.35)
        tg = tag("Minimize Effort · Forward × Backward = Optimal Step", color=TEAL_B).next_to(hdr, DOWN, buff=0.25)
        self.play(FadeIn(hdr), FadeIn(tg), run_time=0.7)

        # Visual: two-ended search
        axes = Axes(
            x_range=[0, 10, 2], y_range=[0, 1, 0.5],
            x_length=9, y_length=3.0,
            axis_config={"color": GRAY_B},
        ).move_to(DOWN * 0.3)
        start_dot = Dot(axes.c2p(0.5, 0.5), color=BLUE_B, radius=0.14)
        goal_dot  = Dot(axes.c2p(9.5, 0.5), color=GREEN_B, radius=0.14)
        start_lbl = Text("Current State", font_size=16, color=BLUE_B).next_to(start_dot, DOWN, buff=0.1)
        goal_lbl  = Text("Goal State",    font_size=16, color=GREEN_B).next_to(goal_dot,  DOWN, buff=0.1)

        # f(x) forward factor, g(x) backward factor
        f_curve = axes.plot(lambda x: 0.85 * np.exp(-0.08 * (x - 0.5) ** 2), color=BLUE_B, stroke_width=3)
        g_curve = axes.plot(lambda x: 0.85 * np.exp(-0.08 * (x - 9.5) ** 2), color=GREEN_B, stroke_width=3)
        fg_curve = axes.plot(lambda x: 0.85 * np.exp(-0.08*(x-0.5)**2) * 0.85 * np.exp(-0.08*(x-9.5)**2) * 14,
                             color=YELLOW_B, stroke_width=4)

        self.play(Create(axes), FadeIn(start_dot), FadeIn(goal_dot),
                  FadeIn(start_lbl), FadeIn(goal_lbl), run_time=0.8)
        self.play(Create(f_curve), run_time=0.5)
        f_lbl = Text("f(x) forward reachability", font_size=16, color=BLUE_B).to_edge(LEFT, buff=0.5).shift(UP * 2.2)
        self.play(FadeIn(f_lbl), run_time=0.3)
        self.play(Create(g_curve), run_time=0.5)
        g_lbl = Text("g(x) backward usefulness", font_size=16, color=GREEN_B).to_edge(RIGHT, buff=0.4).shift(UP * 2.2)
        self.play(FadeIn(g_lbl), run_time=0.3)
        self.play(Create(fg_curve), run_time=0.6)
        fg_lbl = Text("f × g = geodesic optimal step", font_size=18, color=YELLOW_B, weight=BOLD).to_edge(UP, buff=1.7)
        self.play(FadeIn(fg_lbl), run_time=0.4)
        self.next_slide()

        # Formula box
        formula = lbox(
            "Select action a* = argmax_a  Delta log(f*g) / cost(a)",
            col=YELLOW_B, font=22, width=9.2, pad=0.24,
        ).to_edge(DOWN, buff=1.2)
        self.play(FadeIn(formula), run_time=0.6)
        self.next_slide()

        props = panel("Geodesic Control — Why it matters",
                      ["Eliminates wasteful oscillation between forward/backward chaining",
                       "Evidence conservation: no hallucination, no information loss (Noether)",
                       "Same selection rule governs PLN, MOSES, planning, self-modification",
                       "Constant effort per step → predictable compute budget",
                       "Schrödinger bridge provides mathematical foundation (entropic OT)"],
                      width=10.5, tc=TEAL_B).to_edge(DOWN, buff=0.22)
        self.play(FadeOut(formula), FadeIn(props, shift=UP * 0.1), run_time=0.8)
        self.next_slide()


# ──────────────────────────────────────────────────────────────────────────────
# 4.3 MetaMo — Motivational Architecture
# ──────────────────────────────────────────────────────────────────────────────

class Phase4MetaMo(Slide):
    def construct(self):
        hdr = Text("MetaMo: Compositional Motivation Architecture", font_size=28, color=YELLOW_B)
        hdr.to_edge(UP, buff=0.35)
        tg = tag("Multi-Objective · Auditable · Beyond Single Reward", color=YELLOW_B).next_to(hdr, DOWN, buff=0.25)
        self.play(FadeIn(hdr), FadeIn(tg), run_time=0.7)

        # Old reward vs MetaMo
        old = lbox("Old: scalar reward r ∈ ℝ\n→ single objective, brittle", col=RED_B, font=19, width=5.0)
        old.move_to(LEFT * 3.2 + UP * 0.6)
        new = lbox("MetaMo: motive geometry\n→ family of goals + constraints", col=YELLOW_B, font=19, width=5.5)
        new.move_to(RIGHT * 2.8 + UP * 0.6)
        vs = Text("vs", font_size=30, color=GRAY_A).move_to(ORIGIN + UP * 0.6)
        self.play(FadeIn(old), FadeIn(vs), FadeIn(new), run_time=0.8)
        self.next_slide()

        # Pseudo-bimonad explanation
        math_box = RoundedRectangle(corner_radius=0.14, width=10.5, height=2.2,
                                    stroke_color=YELLOW_B, stroke_width=2,
                                    fill_color=BLACK, fill_opacity=0.28).move_to(DOWN * 0.8)
        appraisal = Text("Appraisal  Ψ  (comonad) — extracts context & meaning from situation",
                         font_size=18, color=TEAL_B).move_to(math_box).shift(UP * 0.55)
        decision  = Text("Decision   D  (monad)  — constructs action sequences",
                         font_size=18, color=GREEN_B).move_to(math_box).shift(UP * 0.0)
        combined  = Text("F = D ∘ Ψ   (pseudo-bimonad)  — coupled: feel-then-choose ≈ choose-then-feel",
                         font_size=17, color=YELLOW_B).move_to(math_box).shift(DOWN * 0.55)
        self.play(FadeIn(math_box), FadeIn(appraisal), FadeIn(decision), FadeIn(combined), run_time=0.9)
        self.next_slide()

        # Five principles
        principles = panel("MetaMo's 5 Key Principles",
                           ["1. Modular appraisal & decision — separated but coordinated",
                            "2. Homeostatic stability — resists runaway dynamics",
                            "3. Reciprocal state simulation — models how actions affect others",
                            "4. Motivational compositionality — goals decompose & recombine",
                            "5. Incremental embodiment — abstract values → concrete actions"],
                           width=10.5, tc=YELLOW_B).to_edge(DOWN, buff=0.22)
        self.play(FadeOut(math_box, appraisal, decision, combined, old, vs, new),
                  FadeIn(principles, shift=UP * 0.1), run_time=0.9)
        self.next_slide()

        # MetaMo flow diagram
        flow = VGroup(
            lbox("MetaMo\n(goal arbitration)", YELLOW_B, 17, 2.6).move_to(LEFT * 4.5),
            lbox("SubRep\n(refine goals)", ORANGE, 17, 2.2).move_to(LEFT * 1.5),
            lbox("PLN / MOSES /\nPC-Transformers", TEAL_B, 17, 2.6).move_to(RIGHT * 1.8),
            lbox("Execute\naction", GREEN_B, 17, 2.0).move_to(RIGHT * 4.6),
        )
        flow_arrows = VGroup(*[Arrow(flow[i].get_right(), flow[i+1].get_left(), buff=0.05, stroke_width=4)
                               for i in range(3)])
        self.play(FadeOut(principles), FadeIn(flow, lag_ratio=0.12), Create(flow_arrows), run_time=1.0)
        self.next_slide()


# ──────────────────────────────────────────────────────────────────────────────
# 4.4 SubRep — Goal Decomposition
# ──────────────────────────────────────────────────────────────────────────────

class Phase4SubRep(Slide):
    def construct(self):
        hdr = Text("SubRep: Certificate-Driven Subgoal Decomposition", font_size=27, color=ORANGE)
        hdr.to_edge(UP, buff=0.35)
        tg = tag("CDS · PDS · Motive Decomposition Network", color=ORANGE).next_to(hdr, DOWN, buff=0.25)
        self.play(FadeIn(hdr), FadeIn(tg), run_time=0.7)

        # CDS vs PDS
        cds = RoundedRectangle(corner_radius=0.12, width=5.0, height=2.6,
                                stroke_color=GREEN_B, fill_opacity=0.16).move_to(LEFT * 3.2 + DOWN * 0.2)
        cds_title = Text("CDS — Cone Dominant Subtask", font_size=19, color=GREEN_B, weight=BOLD).move_to(cds).shift(UP * 0.9)
        cds_desc = Text("Candidate option improves\nplanner value for ALL\nmotive-cone weights",
                        font_size=17, color=WHITE, line_spacing=1.2).move_to(cds).shift(DOWN * 0.1)
        cds_cert = Text("→ CDS certificate issued", font_size=15, color=GREEN_B).move_to(cds).shift(DOWN * 0.95)

        pds = RoundedRectangle(corner_radius=0.12, width=5.0, height=2.6,
                                stroke_color=TEAL_B, fill_opacity=0.16).move_to(RIGHT * 3.2 + DOWN * 0.2)
        pds_title = Text("PDS — Pareto Dominant Subtask", font_size=19, color=TEAL_B, weight=BOLD).move_to(pds).shift(UP * 0.9)
        pds_desc = Text("Improves at least ONE weight\nwithout hurting others beyond\nacceptable tolerance",
                        font_size=17, color=WHITE, line_spacing=1.2).move_to(pds).shift(DOWN * 0.1)
        pds_cert = Text("→ PDS certificate issued", font_size=15, color=TEAL_B).move_to(pds).shift(DOWN * 0.95)

        self.play(FadeIn(VGroup(cds, cds_title, cds_desc, cds_cert)), run_time=0.8)
        self.play(FadeIn(VGroup(pds, pds_title, pds_desc, pds_cert)), run_time=0.8)
        self.next_slide()

        insight = panel("SubRep — Why it changes everything",
                        ["Admits options only when they provably serve declared goals",
                         "Works uniformly for neural controllers, logic macros, evolved programs",
                         "Certificates survive composition — safe reuse guaranteed",
                         "MDN (Motive Decomposition Network) co-learns motive geometry",
                         "Fills the gap between 'we can learn skills' and 'we can justify them'"],
                        width=10.5, tc=ORANGE).to_edge(DOWN, buff=0.22)
        self.play(FadeIn(insight, shift=UP * 0.1), run_time=0.8)
        self.next_slide()


# ──────────────────────────────────────────────────────────────────────────────
# 4.5 TransWeave — Knowledge Transfer
# ──────────────────────────────────────────────────────────────────────────────

class Phase4TransWeave(Slide):
    def construct(self):
        hdr = Text("TransWeave: Intelligence Through Intertwining", font_size=27, color=GREEN_B)
        hdr.to_edge(UP, buff=0.35)
        tg = tag("Algebraic Transfer · Commutativity · Braid Laws", color=GREEN_B).next_to(hdr, DOWN, buff=0.25)
        self.play(FadeIn(hdr), FadeIn(tg), run_time=0.7)

        # Core commutativity principle
        comm = lbox(
            "learn o transfer  ~=  transfer o learn",
            col=YELLOW_B, font=28, width=8.4, pad=0.24,
        ).next_to(tg, DOWN, buff=0.4)
        comm_sub = Text("(bounded commutator gap — not exact, but controlled)",
                        font_size=20, color=GRAY_A).next_to(comm, DOWN, buff=0.2)
        self.play(FadeIn(comm), FadeIn(comm_sub), run_time=0.8)
        self.next_slide()

        # H-ICA: when transfer is impossible
        hica = lbox("H-ICA (Hierarchical ICA)\nDecomposes knowledge into:\n"
                    "  ✓ Transferable components\n  ✗ Non-transferable (impossibility flag)",
                    col=TEAL_B, font=18, width=6.5, pad=0.3).move_to(DOWN * 0.6)
        self.play(FadeIn(hica), run_time=0.7)
        self.next_slide()

        # Braid analogy
        self.play(FadeOut(comm, comm_sub, hica), run_time=0.4)

        # Simple braid strands visualization
        def braid_strand(points, color):
            path = VMobject()
            path.set_points_smoothly([np.array([x, y, 0]) for x, y in points])
            path.set_stroke(color=color, width=5)
            return path

        strand1 = braid_strand([(-4.5, 1.5), (-2, 0.5), (0, 1.5), (2, 0.5), (4.5, 1.5)], BLUE_B)
        strand2 = braid_strand([(-4.5, 0.5), (-2, 1.5), (0, 0.5), (2, 1.5), (4.5, 0.5)], GREEN_B)
        strand3 = braid_strand([(-4.5, -0.5), (-2, -0.5), (0, -0.5), (2, -0.5), (4.5, -0.5)], PURPLE_B)

        step_labels = VGroup(
            Text("PLN\nstep", font_size=16, color=BLUE_B).move_to(LEFT * 3.5 + DOWN * 1.5),
            Text("MOSES\nstep", font_size=16, color=GREEN_B).move_to(LEFT * 1.0 + DOWN * 1.5),
            Text("Transfer\nstep", font_size=16, color=YELLOW_B).move_to(RIGHT * 1.5 + DOWN * 1.5),
            Text("PC\nstep", font_size=16, color=PURPLE_B).move_to(RIGHT * 4.0 + DOWN * 1.5),
        )
        braid_title = Text("Braid view: cognitive steps can be re-ordered with bounded error",
                           font_size=19, color=YELLOW_B).to_edge(DOWN, buff=0.6)
        self.play(Create(strand1), Create(strand2), Create(strand3), run_time=1.0)
        self.play(FadeIn(step_labels, lag_ratio=0.12), FadeIn(braid_title), run_time=0.8)
        self.next_slide()

        detail = panel("TransWeave — Practical payoff",
                       ["Pipelines learn→transfer or transfer→learn without derailing",
                        "MORK stores H-ICA components as Merkle-DAG objects",
                        "SubRep admission certificates ride the same transfer machinery",
                        "Geodesic and weakness properties preserved across task transfer",
                        "Impossibility flags prevent brittle negative transfer"],
                       width=10.5, tc=GREEN_B).to_edge(DOWN, buff=0.22)
        self.play(FadeOut(strand1, strand2, strand3, step_labels, braid_title),
                  FadeIn(detail, shift=UP * 0.1), run_time=0.9)
        self.next_slide()


# ──────────────────────────────────────────────────────────────────────────────
# 4.6 Algorithmic Chemistry
# ──────────────────────────────────────────────────────────────────────────────

class Phase4AlgorithmicChemistry(Slide):
    def construct(self):
        hdr = Text("Algorithmic Chemistry: Computation as Reaction", font_size=28, color=TEAL_B)
        hdr.to_edge(UP, buff=0.35)
        tg = tag("ActPC-Chem · Emergent Programs · Natural Gradient", color=TEAL_B).next_to(hdr, DOWN, buff=0.25)
        self.play(FadeIn(hdr), FadeIn(tg), run_time=0.7)

        # Chemical soup metaphor
        soup = Circle(radius=2.4, color=TEAL_B, fill_opacity=0.08).move_to(LEFT * 1.5 + DOWN * 0.3)
        soup_label = Text("Computational Soup\n(MeTTa rewrite rules)", font_size=19, color=TEAL_B,
                          line_spacing=1.2).move_to(soup).shift(DOWN * 1.6)
        self.play(Create(soup), FadeIn(soup_label), run_time=0.7)

        # Molecules (rules) floating
        rng = np.random.default_rng(42)
        molecules = VGroup()
        for i in range(12):
            pos = soup.get_center() + np.array([rng.uniform(-1.8, 1.8), rng.uniform(-1.4, 1.4), 0])
            size = rng.uniform(0.12, 0.24)
            c = Circle(radius=size, color=[BLUE_B, GREEN_B, ORANGE, PURPLE_B][i % 4], fill_opacity=0.35).move_to(pos)
            molecules.add(c)
        self.play(FadeIn(molecules, lag_ratio=0.06), run_time=0.9)
        self.next_slide()

        # Reaction: two rules combine → new rule
        r1 = molecules[2].copy().set_color(BLUE_B)
        r2 = molecules[5].copy().set_color(GREEN_B)
        product = Circle(radius=0.35, color=YELLOW_B, fill_opacity=0.5).move_to(RIGHT * 3.2 + DOWN * 0.3)
        product_t = Text("New\nRule", font_size=14, color=YELLOW_B).move_to(product)
        react_label = Text("Successful rule → higher activation weight\nFailed rule → decays",
                           font_size=18, color=WHITE, line_spacing=1.3).to_edge(RIGHT, buff=0.3).shift(UP * 1.2)
        self.play(r1.animate.move_to(RIGHT * 2.5 + DOWN * 0.3),
                  r2.animate.move_to(RIGHT * 2.5 + DOWN * 0.3), run_time=0.7)
        self.play(FadeOut(r1, r2), FadeIn(product, product_t), FadeIn(react_label), run_time=0.6)
        self.next_slide()

        detail = panel("ActPC-Chem integration with PRIMUS",
                       ["Rules (rewrite patterns) compete like molecules in an abstract chemistry",
                        "Activation weight updated via discrete Active Predictive Coding (ActPC)",
                        "Natural gradient (optimal transport geometry) → stable learning",
                        "AIRIS uses discovered structures as raw material for causal models",
                        "PLN adds logical constraints — not all reactions are allowed",
                        "WILLIAM-guided WAS focuses compute on highest-gain reactions"],
                       width=10.5, tc=TEAL_B).to_edge(DOWN, buff=0.22)
        self.play(FadeIn(detail, shift=UP * 0.1), run_time=0.8)
        self.next_slide()


# ──────────────────────────────────────────────────────────────────────────────
# 4.7 Schrödinger Bridge Learning
# ──────────────────────────────────────────────────────────────────────────────

class Phase4SchrodingerBridge(Slide):
    def construct(self):
        hdr = Text("Schrödinger Bridge Learning", font_size=32, color=BLUE_B)
        hdr.to_edge(UP, buff=0.35)
        tg = tag("Entropic Optimal Transport · Abstract → Detailed Curriculum",
                 color=BLUE_B).next_to(hdr, DOWN, buff=0.25)
        self.play(FadeIn(hdr), FadeIn(tg), run_time=0.7)

        # Simple to complex arc
        axes = Axes(x_range=[0, 10, 2], y_range=[0, 1, 0.5],
                    x_length=9, y_length=2.8, axis_config={"color": GRAY_B}).move_to(DOWN * 0.4)
        x_lbl = Text("Learning Progress →", font_size=17, color=GRAY_A).next_to(axes, DOWN, buff=0.15)
        y_lbl = Text("Model\nComplexity", font_size=15, color=GRAY_A, line_spacing=1.1).rotate(PI/2).next_to(axes, LEFT, buff=0.1)

        # Start distribution (simple) and end distribution (complex)
        simple = Circle(radius=0.35, color=TEAL_B, fill_opacity=0.4).move_to(axes.c2p(0.5, 0.2))
        complex_m = Circle(radius=0.55, color=GREEN_B, fill_opacity=0.4).move_to(axes.c2p(9.5, 0.85))
        simple_t = Text("Simple\nAbstract Model", font_size=14, color=TEAL_B).next_to(simple, DOWN, buff=0.1)
        complex_t = Text("Accurate\nDetailed Model", font_size=14, color=GREEN_B).next_to(complex_m, DOWN, buff=0.1)

        # Bridge path (smooth interpolating curve)
        bridge_pts = [(0.5, 0.2), (2, 0.22), (4, 0.45), (6, 0.62), (8, 0.78), (9.5, 0.85)]
        bridge_path = axes.plot_line_graph(
            [p[0] for p in bridge_pts], [p[1] for p in bridge_pts],
            line_color=YELLOW_B, stroke_width=4, add_vertex_dots=False,
        )
        bridge_label = Text("Schrödinger Bridge — optimal curriculum path", font_size=17, color=YELLOW_B)
        bridge_label.next_to(axes, UP, buff=0.15)

        self.play(Create(axes), FadeIn(x_lbl), FadeIn(y_lbl), run_time=0.7)
        self.play(FadeIn(simple, simple_t), FadeIn(complex_m, complex_t), run_time=0.6)
        self.play(Create(bridge_path), FadeIn(bridge_label), run_time=0.9)
        self.next_slide()

        # Traveling dot
        travel = Dot(axes.c2p(0.5, 0.2), radius=0.1, color=YELLOW_B)
        self.play(FadeIn(travel), run_time=0.2)
        for x, y in bridge_pts[1:]:
            self.play(travel.animate.move_to(axes.c2p(x, y)), run_time=0.35)
        self.next_slide()

        props = panel("Schrödinger Bridge Learning — key properties",
                      ["Automatically discovers coarse→fine curriculum (no hand-design)",
                       "Entropic regularization provides robustness along the path",
                       "For PC networks: same forward/backward factorization as bridge",
                       "For MOSES: biased mutations toward optimal transport kernel K*",
                       "Most effective when structure is multi-scale and compositional"],
                      width=10.5, tc=BLUE_B).to_edge(DOWN, buff=0.22)
        self.play(FadeIn(props, shift=UP * 0.1), run_time=0.8)
        self.next_slide()
