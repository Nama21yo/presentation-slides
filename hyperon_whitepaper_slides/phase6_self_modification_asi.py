"""
Phase 6 — Self-Modification & AGI → ASI Transition
Covers: Why self-modification is needed · Risks · Invariant Hierarchies
         Stability types (strong/weak) · Shadow→Elevate→Primary pipeline
         Rollback & Governance (ASI-Chain) · Auditable Cognition
         Theorem Proving as Benchmark
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
# 6.1 Why Self-Modification is Needed
# ──────────────────────────────────────────────────────────────────────────────

class Phase6WhySelfModification(Slide):
    def construct(self):
        hdr = Text("Why Self-Modification is Needed", font_size=32, color=RED_B)
        hdr.to_edge(UP, buff=0.35)
        tg = tag("Fixed Systems Plateau · AGI Must Improve Itself", color=RED_B).next_to(hdr, DOWN, buff=0.25)
        self.play(FadeIn(hdr), FadeIn(tg), run_time=0.7)

        # Capability plateau diagram
        axes = Axes(x_range=[0, 10, 2], y_range=[0, 1, 0.5],
                    x_length=9, y_length=3.2,
                    axis_config={"color": GRAY_B}).move_to(DOWN * 0.5)
        x_lbl = Text("Time →", font_size=17, color=GRAY_A).next_to(axes, DOWN, buff=0.15)
        y_lbl = Text("Capability", font_size=17, color=GRAY_A).rotate(PI/2).next_to(axes, LEFT, buff=0.15)

        fixed_curve = axes.plot(lambda x: 0.7 * (1 - np.exp(-0.6 * x)), color=RED_B, stroke_width=3)
        selfmod_curve = axes.plot(lambda x: min(0.95, 0.3 * x / (1 + 0.01 * x**2) + 0.05 * x),
                                   color=GREEN_B, stroke_width=3, x_range=[0, 9.5])

        fixed_lbl  = Text("Fixed system — plateau", font_size=17, color=RED_B).to_edge(RIGHT, buff=0.3).shift(UP * 0.6)
        selfmod_lbl = Text("Self-improving system", font_size=17, color=GREEN_B).to_edge(RIGHT, buff=0.3).shift(DOWN * 0.3)

        self.play(Create(axes), FadeIn(x_lbl), FadeIn(y_lbl), run_time=0.7)
        self.play(Create(fixed_curve), FadeIn(fixed_lbl), run_time=0.6)
        self.play(Create(selfmod_curve), FadeIn(selfmod_lbl), run_time=0.6)
        self.next_slide()

        # The key question
        question = lbox(
            "KEY QUESTION: How can an AGI improve itself\nwithout losing its values, purpose, or safety guarantees?",
            col=YELLOW_B, font=20, width=10.5, pad=0.28,
        ).to_edge(DOWN, buff=0.35)
        self.play(FadeIn(question, scale=1.03), run_time=0.7)
        self.next_slide()

        risks = panel("Risks of uncontrolled self-modification",
                      ["Value drift — goals silently change across versions",
                       "Instability — cascading changes break core functions",
                       "Opacity — cannot audit what changed or why",
                       "Goal replacement — instrumental goals displace terminal goals"],
                      width=10.5, tc=RED_B).to_edge(DOWN, buff=0.22)
        self.play(FadeOut(question), FadeIn(risks, shift=UP * 0.1), run_time=0.8)
        self.next_slide()


# ──────────────────────────────────────────────────────────────────────────────
# 6.3 Invariant Hierarchies
# ──────────────────────────────────────────────────────────────────────────────

class Phase6InvariantHierarchies(Slide):
    def construct(self):
        hdr = Text("Invariant Hierarchies: Layered Goal Constraints", font_size=27, color=YELLOW_B)
        hdr.to_edge(UP, buff=0.35)
        tg = tag("Higher layers constrain how lower layers evolve", color=YELLOW_B).next_to(hdr, DOWN, buff=0.25)
        self.play(FadeIn(hdr), FadeIn(tg), run_time=0.7)

        # Pyramid of invariants
        levels = [
            ("Meta-values: 'remain open to growth while preserving identity'", 0.55, PURPLE_B, 5.0),
            ("Core values: 'preserve human dignity and safety'",               0.55, RED_B,    6.8),
            ("Persistent objectives: 'maintain health, maintain coherence'",   0.55, ORANGE,   8.5),
            ("Immediate goals: 'finish this reasoning task'",                  0.55, GREEN_B,  10.5),
        ]

        pyramid = VGroup()
        for i, (text, h, col, w) in enumerate(reversed(levels)):
            rect = RoundedRectangle(corner_radius=0.08, width=w, height=0.65,
                                    stroke_color=col, stroke_width=2,
                                    fill_color=col, fill_opacity=0.25).move_to(DOWN * (0.5 + i * 0.78))
            t = Text(text, font_size=15, color=col).move_to(rect)
            pyramid.add(VGroup(rect, t))

        for layer in pyramid:
            self.play(FadeIn(layer, shift=UP * 0.08), run_time=0.5)

        # Label: constraints flow downward
        constraint_arrow = Arrow(pyramid[3].get_left() + RIGHT * 0.3, pyramid[0].get_left() + RIGHT * 0.3,
                                  buff=0.05, color=YELLOW_B, stroke_width=3)
        constraint_label = Text("constraints", font_size=16, color=YELLOW_B).next_to(constraint_arrow, LEFT, buff=0.1)
        self.play(GrowArrow(constraint_arrow), FadeIn(constraint_label), run_time=0.6)
        self.next_slide()

        # Formal fixed-point
        fp = lbox(
            "T(mech, I) ~= (mech', I')   with   I' subset band(I)",
            col=WHITE, font=21, width=10.2, pad=0.22,
        ).to_edge(DOWN, buff=0.55)
        fp_note = Text("T = self-modification operator · ℐ = invariant family",
                       font_size=18, color=GRAY_A).next_to(fp, DOWN, buff=0.15)
        self.play(FadeIn(fp), FadeIn(fp_note), run_time=0.7)
        self.next_slide()


# ──────────────────────────────────────────────────────────────────────────────
# 6.4 Stability Types
# ──────────────────────────────────────────────────────────────────────────────

class Phase6StabilityTypes(Slide):
    def construct(self):
        hdr = Text("Stability Types: Strong vs Weak", font_size=32, color=TEAL_B)
        hdr.to_edge(UP, buff=0.35)
        tg = tag("Banach Fixed-Point · Schauder · Drift Budgets", color=TEAL_B).next_to(hdr, DOWN, buff=0.25)
        self.play(FadeIn(hdr), FadeIn(tg), run_time=0.7)

        # Strong stability
        strong_box = RoundedRectangle(corner_radius=0.14, width=5.2, height=3.2,
                                       stroke_color=GREEN_B, fill_opacity=0.14).move_to(LEFT * 3.2)
        strong_title = Text("Strong Stability", font_size=22, color=GREEN_B, weight=BOLD).move_to(strong_box).shift(UP * 1.2)
        strong_math  = Text("T is contractive", font_size=22, color=GREEN_B).move_to(strong_box).shift(UP * 0.4)
        strong_thm   = Text("Banach fixed-point theorem\nguarantees unique stable point",
                            font_size=17, color=WHITE, line_spacing=1.2).move_to(strong_box).shift(DOWN * 0.2)
        strong_when  = Text("When: modifications follow a\ncore playbook of principles",
                            font_size=15, color=GRAY_A, line_spacing=1.2).move_to(strong_box).shift(DOWN * 1.0)

        # Weak stability
        weak_box = RoundedRectangle(corner_radius=0.14, width=5.2, height=3.2,
                                     stroke_color=ORANGE, fill_opacity=0.14).move_to(RIGHT * 3.2)
        weak_title = Text("Weak Stability", font_size=22, color=ORANGE, weight=BOLD).move_to(weak_box).shift(UP * 1.2)
        weak_math  = Text("T continuous, compact domain", font_size=19, color=ORANGE).move_to(weak_box).shift(UP * 0.4)
        weak_thm   = Text("Schauder theorem:\nstable points exist (not unique)",
                          font_size=17, color=WHITE, line_spacing=1.2).move_to(weak_box).shift(DOWN * 0.2)
        weak_when  = Text("When: open-ended modification\nwith bounded complexity growth",
                          font_size=15, color=GRAY_A, line_spacing=1.2).move_to(weak_box).shift(DOWN * 1.0)

        self.play(FadeIn(VGroup(strong_box, strong_title, strong_math, strong_thm, strong_when)), run_time=0.8)
        self.play(FadeIn(VGroup(weak_box, weak_title, weak_math, weak_thm, weak_when)), run_time=0.8)
        self.next_slide()

        drift = lbox("Drift Budget: supermartingale Φₖ must decrease in expectation.\n"
                     "If Φₖ rises → scheduler reduces step size or triggers rollback.",
                     col=YELLOW_B, font=18, width=10.5, pad=0.28).to_edge(DOWN, buff=0.25)
        self.play(FadeIn(drift, shift=UP * 0.1), run_time=0.7)
        self.next_slide()


# ──────────────────────────────────────────────────────────────────────────────
# 6.5 Safe Self-Modification Pipeline
# ──────────────────────────────────────────────────────────────────────────────

class Phase6SafePipeline(Slide):
    def construct(self):
        hdr = Text("Safe Self-Modification Pipeline", font_size=32, color=GREEN_B)
        hdr.to_edge(UP, buff=0.35)
        tg = tag("Shadow → Dual-Run → Primary → Rollback", color=GREEN_B).next_to(hdr, DOWN, buff=0.25)
        self.play(FadeIn(hdr), FadeIn(tg), run_time=0.7)

        # Five-stage pipeline
        stages = [
            ("1. Propose",    "Generate candidate change\n(new algorithm / data structure)",  BLUE_B),
            ("2. Analyze",    "Type-check · dependency\ngraph · lens law verification",        TEAL_B),
            ("3. Simulate",   "Run in digital twin with\nbounded geodesic budget",             YELLOW_B),
            ("4. Certify",    "Check: invariants in band?\nWeakness ≥ 0? Evidence conserved?", ORANGE),
            ("5. Deploy",     "Shadow → Dual-Run →\nPrimary · CID audit trail",                GREEN_B),
        ]
        boxes = VGroup(*[
            VGroup(
                RoundedRectangle(corner_radius=0.12, width=2.1, height=2.0,
                                 stroke_color=col, fill_opacity=0.2),
                Text(name, font_size=17, color=col, weight=BOLD),
                Text(desc, font_size=13, color=WHITE, line_spacing=1.15),
            ) for name, desc, col in stages
        ])

        for i, (box_vg, (name, desc, col)) in enumerate(zip(boxes, stages)):
            box_vg[0].move_to(LEFT * 4.5 + RIGHT * i * 2.35 + DOWN * 0.3)
            box_vg[1].move_to(box_vg[0]).shift(UP * 0.65)
            box_vg[2].move_to(box_vg[0]).shift(DOWN * 0.2)
            self.play(FadeIn(box_vg, shift=UP * 0.08), run_time=0.45)

        arrows = VGroup(*[
            Arrow(boxes[i][0].get_right(), boxes[i+1][0].get_left(), buff=0.04, stroke_width=3.5)
            for i in range(4)
        ])
        self.play(Create(arrows, lag_ratio=0.15), run_time=0.7)
        self.next_slide()

        # Shadow → Elevate detail
        shadow_detail = panel("Shadow → Dual-Run → Primary protocol",
                              ["Shadow: new system runs in isolation, no real-world effect",
                               "Dual-Run: runs alongside primary, outputs compared continuously",
                               "Primary: promoted only after all KPIs stable (≥ 24h shadow)",
                               "Last-good CID checkpoint available for instant rollback",
                               "Banach fixed-point convergence ideas underpin this protocol"],
                              width=10.5, tc=GREEN_B).to_edge(DOWN, buff=0.22)
        self.play(FadeIn(shadow_detail, shift=UP * 0.1), run_time=0.8)
        self.next_slide()


# ──────────────────────────────────────────────────────────────────────────────
# 6.6 Rollback & Governance — ASI-Chain
# ──────────────────────────────────────────────────────────────────────────────

class Phase6GovernanceASIChain(Slide):
    def construct(self):
        hdr = Text("Governance Layer: ASI-Chain", font_size=32, color=PURPLE_B)
        hdr.to_edge(UP, buff=0.35)
        tg = tag("Decentralized · Auditable · DAO Governance", color=PURPLE_B).next_to(hdr, DOWN, buff=0.25)
        self.play(FadeIn(hdr), FadeIn(tg), run_time=0.7)

        # Chain visualization
        blocks = VGroup()
        for i in range(5):
            block = RoundedRectangle(corner_radius=0.1, width=2.0, height=1.4,
                                      stroke_color=PURPLE_B, fill_opacity=0.22).move_to(LEFT * 4.0 + RIGHT * i * 2.4 + DOWN * 0.1)
            n = Text(f"Block {i+1}", font_size=15, color=PURPLE_B, weight=BOLD).move_to(block).shift(UP * 0.35)
            cid = Text("CID: 9c7b..", font_size=12, color=TEAL_B).move_to(block).shift(UP * -0.05)
            cert = Text("cert✓", font_size=12, color=GREEN_B).move_to(block).shift(DOWN * 0.4)
            blocks.add(VGroup(block, n, cid, cert))
        chain_arrows = VGroup(*[
            Arrow(blocks[i][0].get_right(), blocks[i+1][0].get_left(), buff=0.04, stroke_width=3.5, color=PURPLE_B)
            for i in range(4)
        ])
        self.play(FadeIn(blocks, lag_ratio=0.12), Create(chain_arrows, lag_ratio=0.12), run_time=1.0)
        self.next_slide()

        # Governance layers
        gov_items = [
            ("Capability scopes",   "Rholang ocap guards — each process specifies exact permissions",  TEAL_B),
            ("Content addressing",  "Every edit: CID + Merkle proof — cryptographically verifiable",   GREEN_B),
            ("FireNode execution",  "F1R3FLY posts proof-of-execution summaries to ASI-Chain",          BLUE_B),
            ("DAO governance",      "k-of-n approval for major upgrades · slashing for unsafe rollouts",ORANGE),
            ("Rollback MTTR ≤ 2min","ShardZipper + CheckpointRef for instant state recovery",           RED_B),
        ]
        gov_vg = VGroup()
        for i, (name, desc, col) in enumerate(gov_items):
            row = VGroup(
                Text(name, font_size=18, color=col, weight=BOLD),
                Text(desc, font_size=16, color=WHITE),
            ).arrange(RIGHT, buff=0.35)
            row.to_edge(LEFT, buff=0.6).shift(DOWN * (1.0 + i * 0.58))
            gov_vg.add(row)
        self.play(FadeIn(gov_vg, lag_ratio=0.12), run_time=1.0)
        self.next_slide()

        quote = lbox(
            '"Intelligence evolution is not hidden — it is publicly auditable\n'
            ' and collectively governed."',
            col=YELLOW_B, font=20, width=10.5, pad=0.28,
        ).to_edge(DOWN, buff=0.25)
        self.play(FadeIn(quote, scale=1.03), run_time=0.7)
        self.next_slide()


# ──────────────────────────────────────────────────────────────────────────────
# 6.7 Auditable Cognition
# ──────────────────────────────────────────────────────────────────────────────

class Phase6AuditableCognition(Slide):
    def construct(self):
        hdr = Text("Auditable Cognition: No Hidden Steps", font_size=31, color=GREEN_B)
        hdr.to_edge(UP, buff=0.35)
        tg = tag("Traceable Reasoning · Evidence Capsules · CID Provenance", color=GREEN_B).next_to(hdr, DOWN, buff=0.25)
        self.play(FadeIn(hdr), FadeIn(tg), run_time=0.7)

        # Reasoning chain with provenance
        chain_boxes = [
            lbox("Premise A\nTV=(0.9,0.95)", TEAL_B, 16, 2.5),
            lbox("Premise B\nTV=(0.8,0.90)", TEAL_B, 16, 2.5),
            lbox("PLN Deduction\nRule: Modus Ponens", GREEN_B, 16, 2.8),
            lbox("Conclusion C\nTV=(0.72, 0.85)", YELLOW_B, 16, 2.5),
        ]
        chain = VGroup(*chain_boxes)
        # Layout: A and B merge into rule, rule produces C
        chain_boxes[0].move_to(LEFT * 4.5 + UP * 0.5)
        chain_boxes[1].move_to(LEFT * 4.5 + DOWN * 0.8)
        chain_boxes[2].move_to(LEFT * 1.2 + DOWN * 0.15)
        chain_boxes[3].move_to(RIGHT * 2.5 + DOWN * 0.15)

        arr1 = Arrow(chain_boxes[0].get_right(), chain_boxes[2].get_left() + UP * 0.15, buff=0.06, stroke_width=3, color=TEAL_B)
        arr2 = Arrow(chain_boxes[1].get_right(), chain_boxes[2].get_left() + DOWN * 0.15, buff=0.06, stroke_width=3, color=TEAL_B)
        arr3 = Arrow(chain_boxes[2].get_right(), chain_boxes[3].get_left(), buff=0.06, stroke_width=3.5, color=YELLOW_B)

        self.play(FadeIn(chain_boxes[0], chain_boxes[1]), run_time=0.6)
        self.play(FadeIn(chain_boxes[2]), GrowArrow(arr1), GrowArrow(arr2), run_time=0.7)
        self.play(FadeIn(chain_boxes[3]), GrowArrow(arr3), run_time=0.6)
        self.next_slide()

        # CID labels on everything
        for box in chain_boxes:
            cid_t = Text("CID: 0x…", font_size=11, color=PURPLE_B).next_to(box, DOWN, buff=0.08)
            self.play(FadeIn(cid_t), run_time=0.2)

        props = panel("Why auditable cognition matters for AGI safety",
                      ["Every inference step carries a CID — immutable, traceable",
                       "Evidence capsules track what evidence was used (no double-counting)",
                       "Rollback: revert to any prior certified state in < 2 minutes",
                       "Multi-party validation: external teams can verify reasoning chains",
                       "Weakness + geodesic certificates attached to every decision"],
                      width=10.5, tc=GREEN_B).to_edge(DOWN, buff=0.22)
        self.play(FadeIn(props, shift=UP * 0.1), run_time=0.8)
        self.next_slide()


# ──────────────────────────────────────────────────────────────────────────────
# 6.8 Theorem Proving as Benchmark
# ──────────────────────────────────────────────────────────────────────────────

class Phase6TheoremProvingBenchmark(Slide):
    def construct(self):
        hdr = Text("Theorem Proving as AGI Benchmark", font_size=31, color=BLUE_B)
        hdr.to_edge(UP, buff=0.35)
        tg = tag("High Rigor · Crisp Correctness · Automated Conjecturing", color=BLUE_B).next_to(hdr, DOWN, buff=0.25)
        self.play(FadeIn(hdr), FadeIn(tg), run_time=0.7)

        # Math pipeline
        pipeline = [
            ("MathSpace\n(Atoms: defs, lemmas, proofs)", TEAL_B, 2.8),
            ("Pattern Miner +\nWILLIAM → proof motifs", PURPLE_B, 2.8),
            ("Conjecture Engine\n(PLN + geodesic f·g)", GREEN_B, 2.8),
            ("PLN sketch →\nExternal ATP verify", ORANGE, 2.8),
            ("MM2 kernel\n(fast local proof check)", YELLOW_B, 2.8),
        ]
        pipe_boxes = VGroup(*[lbox(t, col=c, font=15, width=w) for t, c, w in pipeline])
        pipe_boxes.arrange(RIGHT, buff=0.15).move_to(UP * 0.4)
        pipe_arrows = VGroup(*[Arrow(pipe_boxes[i].get_right(), pipe_boxes[i+1].get_left(),
                                     buff=0.04, stroke_width=3) for i in range(4)])
        self.play(FadeIn(pipe_boxes, lag_ratio=0.12), Create(pipe_arrows, lag_ratio=0.12), run_time=1.0)
        self.next_slide()

        # Why theorem proving validates the architecture
        insight = panel("Why theorem proving is the ultimate AGI test",
                        ["Proofs require precise definitions, lemmas, and valid reasoning chains",
                         "Success criterion is binary: proof checks or it does not",
                         "Creative conjecturing tests hypothesis formation capability",
                         "Combines PLN backward chaining + LLM pattern + ITP checking",
                         "TransWeave transfers lemmas from group theory → ring theory etc.",
                         "MM2 proof kernel runs inside MORK — no serialization boundary"],
                        width=10.5, tc=BLUE_B).to_edge(DOWN, buff=0.22)
        self.play(FadeIn(insight, shift=UP * 0.1), run_time=0.8)
        self.next_slide()
