"""
Phase 7 — Application Layer
Phase 8 — Master Plan (Execution Roadmap)
Phase 9 — System-Level Synthesis
Covers all application domains, quarterly roadmap visualization,
and the full system layered view + core unifying ideas.
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


def fit_width(mob, width):
    if mob.width > width:
        mob.scale_to_fit_width(width)
    return mob


# ──────────────────────────────────────────────────────────────────────────────
# 7. Application Layer — All Domains
# ──────────────────────────────────────────────────────────────────────────────

class Phase7Applications(Slide):
    def construct(self):
        hdr = Text("Application Layer", font_size=34, color=TEAL_B)
        hdr.to_edge(UP, buff=0.35)
        tg = tag("Real-world lighthouses that shape the system", color=TEAL_B).next_to(hdr, DOWN, buff=0.25)
        self.play(FadeIn(hdr), FadeIn(tg), run_time=0.7)

        # Six domain cards
        domains = [
            ("Qwestor",             "Research assistant\nPLN+LLM+long memory",       BLUE_B),
            ("Minecraft/\nSophiaverse", "Embodied cognition\nSkill transfer",        GREEN_B),
            ("Math Proving",        "Theorem proving\n& conjecturing",               PURPLE_B),
            ("Bioinformatics",      "Protein folding\nDrug discovery hypotheses",    TEAL_B),
            ("Robotics",            "Social humanoid robots\nPlanning + control",     ORANGE),
            ("Finance",             "Risk modeling\nNeurosymbolic inference",         YELLOW_B),
        ]
        cards = VGroup()
        positions = [
            LEFT * 4.5 + UP * 0.8, ORIGIN + UP * 0.8, RIGHT * 4.5 + UP * 0.8,
            LEFT * 4.5 + DOWN * 1.5, ORIGIN + DOWN * 1.5, RIGHT * 4.5 + DOWN * 1.5,
        ]
        for (title, desc, col), pos in zip(domains, positions):
            box = RoundedRectangle(corner_radius=0.14, width=3.6, height=1.6,
                                    stroke_color=col, fill_opacity=0.18).move_to(pos)
            t = Text(title, font_size=19, color=col, weight=BOLD).move_to(box).shift(UP * 0.45)
            d = Text(desc, font_size=15, color=WHITE, line_spacing=1.2).move_to(box).shift(DOWN * 0.2)
            cards.add(VGroup(box, t, d))

        for card in cards:
            self.play(FadeIn(card, scale=0.92), run_time=0.45)
        self.next_slide()

        # Shared infrastructure
        shared = lbox(
            "All domains share: Atomspace · PLN · ECAN · WILLIAM · TransWeave\n"
            "→ Improvements to one domain immediately benefit ALL others.",
            col=YELLOW_B, font=19, width=10.5, pad=0.28,
        ).to_edge(DOWN, buff=0.25)
        self.play(FadeIn(shared, shift=UP * 0.1), run_time=0.7)
        self.next_slide()


class Phase7QwestorDetail(Slide):
    def construct(self):
        hdr = Text("Qwestor: Interactive Research Assistant", font_size=30, color=BLUE_B)
        hdr.to_edge(UP, buff=0.35)
        tg = tag("LLMs + MORK-RAG + PLN + Long Memory", color=BLUE_B).next_to(hdr, DOWN, buff=0.25)
        self.play(FadeIn(hdr), FadeIn(tg), run_time=0.7)

        # User query flow
        flow = [
            ("User Query",          GRAY_A,   LEFT * 5.0 + UP * 0.5),
            ("MORK-RAG\n(retrieval)", TEAL_B, LEFT * 2.5 + UP * 0.5),
            ("PLN Backward\nChaining", GREEN_B, ORIGIN + UP * 0.5),
            ("Concept\nBlending",    PURPLE_B, RIGHT * 2.5 + UP * 0.5),
            ("Synthesized\nAnswer",  YELLOW_B, RIGHT * 5.0 + UP * 0.5),
        ]
        flow_boxes = VGroup(*[lbox(t, col=c, font=15, width=2.4) for t, c, _ in flow])
        for (_, _, pos), box in zip(flow, flow_boxes):
            box.move_to(pos)
        flow_arrows = VGroup(*[Arrow(flow_boxes[i].get_right(), flow_boxes[i+1].get_left(),
                                     buff=0.05, stroke_width=3.5) for i in range(4)])
        self.play(FadeIn(flow_boxes, lag_ratio=0.12), Create(flow_arrows, lag_ratio=0.12), run_time=1.0)

        # Memory layers
        working_mem = lbox("Working Memory\n(ECAN-guided STI)", YELLOW_B, 16, 2.8).move_to(LEFT * 3.0 + DOWN * 1.5)
        long_mem    = lbox("Long-Term Memory\n(MORK Atomspace)", BLUE_B, 16, 2.8).move_to(ORIGIN + DOWN * 1.5)
        prov        = lbox("Provenance\n(ASI-Chain CIDs)", PURPLE_B, 16, 2.8).move_to(RIGHT * 3.0 + DOWN * 1.5)
        self.play(FadeIn(VGroup(working_mem, long_mem, prov), lag_ratio=0.12), run_time=0.8)

        advantage = lbox(
            "Outperforms RAG baselines on multi-hop tasks by:\n"
            "  combining graph retrieval + uncertain reasoning + creative synthesis",
            col=GREEN_B, font=18, width=10.5, pad=0.25,
        ).to_edge(DOWN, buff=0.25)
        self.play(FadeIn(advantage, shift=UP * 0.1), run_time=0.7)
        self.next_slide()


class Phase7MinecraftBioMath(Slide):
    def construct(self):
        hdr = Text("Game AI · Bioinformatics · Mathematics", font_size=28, color=GREEN_B)
        hdr.to_edge(UP, buff=0.35)
        tg = tag("Three core application testbeds", color=GREEN_B).next_to(hdr, DOWN, buff=0.25)
        self.play(FadeIn(hdr), FadeIn(tg), run_time=0.7)

        sections = [
            ("Minecraft / Sophiaverse",
             ["Atomspace mirrors game state (voxels, entities, quests)",
              "SubRep-certified options: navigate, craft, trade",
              "PLN plans multi-step sequences under geodesic control",
              "PC waveformers for fast perception & control loops",
              "WILLIAM + ECAN focus attention on relevant subgraphs",
              "TransWeave transfers skills across worlds"],
             GREEN_B),
            ("Bioinformatics (Rejuve Bio)",
             ["BioSpace adapters: omics → Atoms with CIDs",
              "Pattern Miner: find gene-pathway-phenotype motifs",
              "PLN factor-graphs: uncertain causal inference",
              "MOSES evolves predictive programs for cohort responses",
              "Output: ranked hypothesis packs (mechanism + predictor)"],
             TEAL_B),
            ("Automated Mathematics",
             ["MathSpace: definitions, theorems, proofs as Atoms",
              "Conjecture engine: geodesic f·g over typed expressions",
              "PLN provides uncertain proof sketches",
              "LLM fills tactics; MM2 kernel verifies formally",
              "TransWeave: group theory lemmas → ring theory"],
             PURPLE_B),
        ]
        for i, (title, bullets, col) in enumerate(sections):
            p = panel(title, bullets, width=3.7, tc=col, fc=14, ft=17)
            p.move_to(LEFT * 3.8 + RIGHT * i * 3.85 + DOWN * 0.2)
            self.play(FadeIn(p, shift=UP * 0.08), run_time=0.7)
        self.next_slide()


# ──────────────────────────────────────────────────────────────────────────────
# 8. Master Plan — Quarterly Roadmap
# ──────────────────────────────────────────────────────────────────────────────

class Phase8MasterPlan(Slide):
    def construct(self):
        hdr = Text("Master Plan: 2026–2027 Roadmap", font_size=30, color=YELLOW_B)
        hdr.to_edge(UP, buff=0.35)
        tg = tag("4 Workstreams · 8 Quarters · AGI by Q4 2027", color=YELLOW_B).next_to(hdr, DOWN, buff=0.25)
        self.play(FadeIn(hdr), FadeIn(tg), run_time=0.7)

        # Timeline bar
        timeline = Line(LEFT * 5.5 + DOWN * 0.1, RIGHT * 5.5 + DOWN * 0.1, color=GRAY_B, stroke_width=3)
        self.play(Create(timeline), run_time=0.5)

        quarters = [
            ("Q1'26", "Cognitive algos\nin MeTTa · PC scaling",    BLUE_B,   LEFT * 5.0),
            ("Q2'26", "DAS scale-up\nfirst app experiments",        TEAL_B,   LEFT * 2.8),
            ("Q3'26", "Results from\nscaled Hyperon algos",         GREEN_B,  LEFT * 0.6),
            ("Q4'26", "Cognitive synergy\ndemonstrations",          YELLOW_B, RIGHT * 1.6),
            ("Q1'27", "Self-modification\nexperiments begin",       ORANGE,   RIGHT * 3.6),
            ("Q2'27", "Auto-tuning\nmeta-learning",                 RED_B,    RIGHT * 5.6),
        ]
        for label, desc, col, x_pos in quarters:
            dot = Dot(x_pos + DOWN * 0.1, radius=0.1, color=col)
            ql = Text(label, font_size=16, color=col, weight=BOLD).next_to(dot, UP, buff=0.1)
            dl = Text(desc, font_size=12, color=WHITE, line_spacing=1.1).next_to(dot, DOWN, buff=0.15)
            self.play(FadeIn(VGroup(dot, ql, dl)), run_time=0.4)
        self.next_slide()

        # Year labels
        y1 = Text("Year 1 (2026): First Cognitive-Synergetic PRIMUS Brain",
                  font_size=19, color=TEAL_B).to_edge(DOWN, buff=1.1)
        y2 = Text("Year 2 (2027): Scaling · Safety · Self-Modification · AGI",
                  font_size=19, color=ORANGE).to_edge(DOWN, buff=0.55)
        self.play(FadeIn(y1), FadeIn(y2), run_time=0.6)
        self.next_slide()


class Phase8Workstreams(Slide):
    def construct(self):
        hdr = Text("Workstreams & Success Criteria", font_size=30, color=BLUE_B)
        hdr.to_edge(UP, buff=0.35)
        tg = tag("Infrastructure · Cognition · Neural · Applications", color=BLUE_B).next_to(hdr, DOWN, buff=0.25)
        self.play(FadeIn(hdr), FadeIn(tg), run_time=0.7)

        workstreams = [
            ("Infrastructure", ["MORK / MM2 / DAS performance", "MeTTa-IL supercompiler", "ASI-Chain deployment"], ORANGE),
            ("Cognitive Algos", ["PLN factor-graph + geodesic", "MOSES/GEO-EVO + ECAN fluid", "WILLIAM + MetaMo + SubRep"], TEAL_B),
            ("Neural Integration", ["PC/CC transformers at scale", "QuantiMORK inside Atomspace", "Schrödinger bridge curricula"], PURPLE_B),
            ("Applications", ["Qwestor 0.1 → 1.0", "Minecraft + Sophiaverse", "Bio / Robotics / Finance"], GREEN_B),
        ]
        ws_vg = VGroup()
        for i, (name, items, col) in enumerate(workstreams):
            p = panel(name, items, width=2.9, tc=col, fc=14, ft=17)
            p.move_to(LEFT * 4.3 + RIGHT * i * 3.0 + DOWN * 0.3)
            ws_vg.add(p)
        for p in ws_vg:
            self.play(FadeIn(p, shift=UP * 0.08), run_time=0.5)
        self.next_slide()

        success = panel("Success Criteria (End of Year 2)",
                        ["Production-ready Hyperon stack: MORK · MeTTa-IL · DAS · ASI-Chain",
                         "PRIMUS running in real workloads: PLN · ECAN · MOSES · WILLIAM",
                         "Scalable PC/CC neural nets inside MORK Atomspace",
                         "Qwestor outperforms RAG baselines on multi-hop reasoning",
                         "Minecraft agents: sub-second decisions with certified option transfer",
                         "Safe self-modification pipeline with verifiable invariant preservation"],
                        width=10.5, tc=YELLOW_B).to_edge(DOWN, buff=0.22)
        self.play(FadeIn(success, shift=UP * 0.1), run_time=0.8)
        self.next_slide()


# ──────────────────────────────────────────────────────────────────────────────
# 9. System-Level Synthesis
# ──────────────────────────────────────────────────────────────────────────────

class Phase9FullSystemView(Slide):
    def construct(self):
        hdr = Text("System-Level Synthesis", font_size=33, color=WHITE)
        hdr.to_edge(UP, buff=0.35)
        tg = tag("Bottom-up full stack view", color=WHITE).next_to(hdr, DOWN, buff=0.25)
        self.play(FadeIn(hdr), FadeIn(tg), run_time=0.7)

        # Layered stack (bottom to top)
        stack_data = [
            ("Math Foundations",      "Sets→Metagraphs→Quantales→PLN TV→Predictive Coding",   "#1a2a3a", GRAY_A,    0.68),
            ("Atomspace",             "Typed content-addressed metagraph — universal substrate", "#0a2a4a", TEAL_B,   0.68),
            ("MORK",                  "PathMap/Merkle-DAG · WAS · ShardZipper · ByteFlow",      "#0a3a2a", GREEN_B,  0.68),
            ("MeTTa Stack",           "MeTTa · MeTTa-IL · PyMeTTa · PeTTa · MM2 · JeTTa",      "#3a2a0a", ORANGE,   0.68),
            ("PRIMUS Cognition",      "Goal Loop + Ambient Loop · PLN · ECAN · MOSES · WILLIAM","#2a0a3a", PURPLE_B, 0.68),
            ("QuantiMORK / Neural",   "PC waveformers inside MORK · Symbolic Heads · Commutativity","#3a0a2a", RED_B, 0.68),
            ("Governance",            "ASI-Chain · Shadow→Elevate → Rollback · DAO",           "#2a3a0a", YELLOW_B, 0.68),
            ("Applications",          "Qwestor · Minecraft · Math · Bio · Robotics · Finance",  "#1a3a1a", GREEN_A,  0.68),
        ]
        total_h = len(stack_data) * 0.68
        start_y = -total_h / 2 + 0.34 + 0.1
        for i, (name, desc, fill, stroke, h) in enumerate(stack_data):
            y = start_y + i * h
            rect = RoundedRectangle(corner_radius=0.07, width=11.0, height=h * 0.9,
                                     stroke_color=stroke, stroke_width=1.8,
                                     fill_color=fill, fill_opacity=0.42).move_to([0, y, 0])
            n_t = Text(name, font_size=17, color=stroke, weight=BOLD).move_to(rect).shift(LEFT * 3.2)
            d_t = Text(desc, font_size=13, color=WHITE).move_to(rect).shift(RIGHT * 1.5)
            self.play(FadeIn(VGroup(rect, n_t, d_t), shift=UP * 0.05), run_time=0.38)
        self.next_slide()


class Phase9CoreUnifyingIdeas(Slide):
    def construct(self):
        hdr = Text("Core Unifying Ideas", font_size=34, color=YELLOW_B)
        hdr.to_edge(UP, buff=0.35)
        tg = tag("The mathematical threads that run through everything", color=YELLOW_B).next_to(hdr, DOWN, buff=0.25)
        self.play(FadeIn(hdr), FadeIn(tg), run_time=0.7)

        ideas = [
            ("Shared substrate",         "One Atomspace — all modules share memory and control plane",         TEAL_B),
            ("Two-loop cognition",        "Goal-directed + Ambient → deliberate & exploratory together",       BLUE_B),
            ("Compression-driven",        "WILLIAM: compress = discover = focus = generalize",                 PURPLE_B),
            ("Geodesic optimization",     "f × g product — minimum effort toward goals at every step",         GREEN_B),
            ("Unified attention",         "ECAN + fluid dynamics — optimal transport of cognitive resources",   ORANGE),
            ("Auditable reasoning",       "CID provenance on every Atom — reasoning is always traceable",      YELLOW_B),
            ("Safe evolution",            "Invariant hierarchies + Shadow pipeline + ASI-Chain DAO",           RED_B),
        ]

        hub = Circle(radius=0.65, color=YELLOW_B, fill_opacity=0.22).move_to(ORIGIN)
        hub_t = Text("Hyperon\nPRIMUS", font_size=17, color=YELLOW_B, line_spacing=1.1).move_to(hub)
        self.play(Create(hub), FadeIn(hub_t), run_time=0.6)

        angles = np.linspace(0, 2 * np.pi, len(ideas), endpoint=False)
        for i, ((name, desc, col), angle) in enumerate(zip(ideas, angles)):
            radius = 3.3
            pos = np.array([radius * np.cos(angle), radius * np.sin(angle) * 0.75, 0])
            box = RoundedRectangle(corner_radius=0.1, width=3.0, height=0.7,
                                    stroke_color=col, fill_opacity=0.22).move_to(pos)
            nt = Text(name, font_size=15, color=col, weight=BOLD).move_to(box).shift(UP * 0.1)
            dt = Text(desc, font_size=10, color=WHITE, line_spacing=1.0).move_to(box).shift(DOWN * 0.22)
            line = Line(ORIGIN, pos, color=col, stroke_width=2, stroke_opacity=0.55)
            self.play(Create(line), FadeIn(VGroup(box, nt, dt)), run_time=0.45)
        self.next_slide()


# ──────────────────────────────────────────────────────────────────────────────
# HyperClaw — Cognitive Orchestration Layer
# ──────────────────────────────────────────────────────────────────────────────

class HyperClawOrchestrationLayer(Slide):
    def construct(self):
        hdr = Text("HyperClaw: Cognitive Orchestration Layer", font_size=32, color=TEAL_B)
        hdr.to_edge(UP, buff=0.35)
        tg = tag("The coordinator that turns many AI tools into one workflow", color=TEAL_B).next_to(hdr, DOWN, buff=0.22)
        self.play(FadeIn(hdr), FadeIn(tg), run_time=0.7)

        human = lbox("Human\nstrategy", GRAY_A, 17, 2.05).move_to(LEFT * 5.05 + UP * 0.75)
        context = lbox("Context Frame\nGoals · state · history", YELLOW_B, 16, 3.1).move_to(LEFT * 4.7 + DOWN * 1.0)
        hub = Circle(radius=1.0, color=TEAL_B, fill_opacity=0.22).move_to(LEFT * 0.55 + UP * 0.1)
        hub_label = Text("HyperClaw\nAttention\nMetaprotocol", font_size=18, color=TEAL_B, line_spacing=1.0).move_to(hub)

        modules = VGroup(
            lbox("Math LLM", BLUE_B, 16, 2.1).move_to(RIGHT * 4.75 + UP * 1.35),
            lbox("Code\nexecutor", GREEN_B, 16, 2.1).move_to(RIGHT * 4.75 + UP * 0.35),
            lbox("Critic LLM", ORANGE, 16, 2.1).move_to(RIGHT * 4.75 + DOWN * 0.65),
            lbox("Symbolic\nreasoner", PURPLE_B, 16, 2.1).move_to(RIGHT * 4.75 + DOWN * 1.65),
        )

        arrows = VGroup(
            Arrow(human.get_right(), hub.get_left(), buff=0.08, stroke_width=4, color=GRAY_A),
            Arrow(context.get_right(), hub.get_left(), buff=0.08, stroke_width=4, color=YELLOW_B),
        )
        for mod in modules:
            arrows.add(Arrow(hub.get_right(), mod.get_left(), buff=0.08, stroke_width=3.5, color=TEAL_B))

        takeaway = lbox(
            "Automates tool selection · handoff · integration · audit trail",
            GREEN_B, 18, 8.8,
        ).to_edge(DOWN, buff=0.25)

        self.play(FadeIn(human), Create(hub), FadeIn(hub_label), run_time=0.75)
        self.play(FadeIn(context), Create(arrows[:2]), run_time=0.65)
        self.play(FadeIn(modules, lag_ratio=0.1), Create(arrows[2:], lag_ratio=0.08), run_time=1.0)
        self.play(FadeIn(takeaway, shift=UP * 0.08), run_time=0.7)
        self.next_slide()


class HyperClawArchitecturePillars(Slide):
    def construct(self):
        hdr = Text("HyperClaw Architecture", font_size=34, color=BLUE_B)
        hdr.to_edge(UP, buff=0.35)
        tg = tag("MeTTaClaw becomes a scalable coordinator", color=BLUE_B).next_to(hdr, DOWN, buff=0.22)
        self.play(FadeIn(hdr), FadeIn(tg), run_time=0.7)

        foundation = lbox("MeTTaClaw\nsmall transparent agent\nmemory · tools · skills", BLUE_B, 17, 4.1).move_to(LEFT * 4.2 + UP * 0.3)
        upgrade = Text("wrapped by", font_size=20, color=GRAY_A).move_to(LEFT * 1.35 + UP * 0.3)
        upgrade_arrow = Arrow(foundation.get_right(), upgrade.get_left(), buff=0.08, stroke_width=4, color=GRAY_A)

        pillars = VGroup(
            panel("Context Frames",
                  ["Shared working memory",
                   "Active goals and hypotheses",
                   "Every module reads and writes state"],
                  width=3.35, tc=YELLOW_B, fc=13, ft=17),
            panel("Module Spaces",
                  ["One adapter interface",
                   "LLMs, code, data stores, robots",
                   "Different tools speak one protocol"],
                  width=3.35, tc=GREEN_B, fc=13, ft=17),
            panel("Attention Metaprotocol",
                  ["Chooses what matters next",
                   "Controls fast and slow loops",
                   "Integrates outputs into the frame"],
                  width=3.35, tc=PURPLE_B, fc=13, ft=17),
        ).arrange(DOWN, buff=0.18).move_to(RIGHT * 3.15 + DOWN * 0.5)

        braces = VGroup(
            Arrow(upgrade.get_right(), pillars[0].get_left(), buff=0.1, stroke_width=3, color=YELLOW_B),
            Arrow(upgrade.get_right(), pillars[1].get_left(), buff=0.1, stroke_width=3, color=GREEN_B),
            Arrow(upgrade.get_right(), pillars[2].get_left(), buff=0.1, stroke_width=3, color=PURPLE_B),
        )
        result = lbox("Result: a controllable multi-module mind", TEAL_B, 20, 7.2).to_edge(DOWN, buff=0.24)

        self.play(FadeIn(foundation, shift=RIGHT * 0.08), GrowArrow(upgrade_arrow), FadeIn(upgrade), run_time=0.8)
        for p, a in zip(pillars, braces):
            self.play(GrowArrow(a), FadeIn(p, shift=LEFT * 0.08), run_time=0.55)
        self.play(FadeIn(result, shift=UP * 0.08), run_time=0.65)
        self.next_slide()


class HyperClawAttentionLoops(Slide):
    def construct(self):
        hdr = Text("HyperClaw Attention Loops", font_size=34, color=YELLOW_B)
        hdr.to_edge(UP, buff=0.35)
        tg = tag("Execution runs fast; strategy changes slowly", color=YELLOW_B).next_to(hdr, DOWN, buff=0.22)
        self.play(FadeIn(hdr), FadeIn(tg), run_time=0.7)

        fast_box = RoundedRectangle(corner_radius=0.12, width=5.4, height=3.35,
                                    stroke_color=GREEN_B, stroke_width=2.2,
                                    fill_color=BLACK, fill_opacity=0.22).move_to(LEFT * 3.05 + DOWN * 0.25)
        slow_box = RoundedRectangle(corner_radius=0.12, width=5.4, height=3.35,
                                    stroke_color=ORANGE, stroke_width=2.2,
                                    fill_color=BLACK, fill_opacity=0.22).move_to(RIGHT * 3.05 + DOWN * 0.25)
        fast_title = Text("Fast Loop", font_size=25, color=GREEN_B, weight=BOLD).next_to(fast_box.get_top(), DOWN, buff=0.22)
        slow_title = Text("Slow Loop", font_size=25, color=ORANGE, weight=BOLD).next_to(slow_box.get_top(), DOWN, buff=0.22)

        fast_steps = VGroup(
            lbox("select module", GREEN_B, 15, 2.1),
            lbox("run action", GREEN_B, 15, 2.1),
            lbox("check result", GREEN_B, 15, 2.1),
            lbox("write frame", GREEN_B, 15, 2.1),
        ).arrange(DOWN, buff=0.13).move_to(fast_box.get_center() + DOWN * 0.18)
        fast_arrows = VGroup(*[
            Arrow(fast_steps[i].get_bottom(), fast_steps[i + 1].get_top(), buff=0.04, stroke_width=3, color=GREEN_B)
            for i in range(3)
        ])

        slow_steps = VGroup(
            lbox("evaluate progress", ORANGE, 15, 2.35),
            lbox("change mode", ORANGE, 15, 2.35),
            lbox("ask human\non major pivots", ORANGE, 15, 2.35),
        ).arrange(DOWN, buff=0.18).move_to(slow_box.get_center() + DOWN * 0.1)
        slow_arrows = VGroup(*[
            Arrow(slow_steps[i].get_bottom(), slow_steps[i + 1].get_top(), buff=0.04, stroke_width=3, color=ORANGE)
            for i in range(2)
        ])

        clock_fast = Text("seconds-minutes", font_size=18, color=GREEN_B).next_to(fast_box, DOWN, buff=0.16)
        clock_slow = Text("minutes-hours", font_size=18, color=ORANGE).next_to(slow_box, DOWN, buff=0.16)
        bridge = Arrow(fast_box.get_right(), slow_box.get_left(), buff=0.18, stroke_width=4, color=YELLOW_B)
        bridge_label = Text("attention budget", font_size=18, color=YELLOW_B).next_to(bridge, UP, buff=0.12)

        self.play(Create(VGroup(fast_box, slow_box)), FadeIn(VGroup(fast_title, slow_title)), run_time=0.65)
        self.play(FadeIn(fast_steps, lag_ratio=0.1), Create(fast_arrows), FadeIn(clock_fast), run_time=0.85)
        self.play(FadeIn(slow_steps, lag_ratio=0.1), Create(slow_arrows), FadeIn(clock_slow), run_time=0.85)
        self.play(GrowArrow(bridge), FadeIn(bridge_label), run_time=0.55)
        self.next_slide()


class HyperClawUseCasesAndEvolution(Slide):
    def construct(self):
        hdr = Text("HyperClaw: From Workflow Automation to AGI", font_size=32, color=GREEN_B)
        hdr.to_edge(UP, buff=0.35)
        tg = tag("v1 coordinates tools; v2 becomes PRIMUS-level cognition", color=GREEN_B).next_to(hdr, DOWN, buff=0.22)
        self.play(FadeIn(hdr), FadeIn(tg), run_time=0.7)

        lane = Line(LEFT * 5.2 + UP * 1.05, RIGHT * 5.2 + UP * 1.05, color=GRAY_B, stroke_width=3)
        v1_dot = Dot(LEFT * 3.8 + UP * 1.05, radius=0.11, color=BLUE_B)
        v2_dot = Dot(RIGHT * 0.2 + UP * 1.05, radius=0.11, color=PURPLE_B)
        safe_dot = Dot(RIGHT * 4.0 + UP * 1.05, radius=0.11, color=YELLOW_B)
        self.play(Create(lane), FadeIn(VGroup(v1_dot, v2_dot, safe_dot)), run_time=0.6)

        v1 = panel("HyperClaw v1",
                   ["Orchestrates LLMs and code executors",
                    "Automates bug-fix and experiment loops",
                    "Human still provides creative steering"],
                   width=3.55, tc=BLUE_B, fc=13, ft=17).move_to(LEFT * 3.8 + DOWN * 0.35)
        v2 = panel("HyperClaw v2",
                   ["Integrates PLN, MOSES, WILLIAM",
                    "Moves creative steering into cognition",
                    "Becomes HYPERON / PRIMUS scale"],
                   width=3.55, tc=PURPLE_B, fc=13, ft=17).move_to(RIGHT * 0.2 + DOWN * 0.35)
        safe = panel("Deployed Safely",
                     ["ASI:Chain provenance",
                      "Capability contracts per module",
                      "Shadow · elevate · rollback upgrades"],
                     width=3.55, tc=YELLOW_B, fc=13, ft=17).move_to(RIGHT * 4.0 + DOWN * 0.35)

        apps = VGroup(
            lbox("Finance\nmanaged experiments", GREEN_B, 17, 3.8),
            lbox("Social robotics\nsafe attention", ORANGE, 17, 3.8),
        ).arrange(RIGHT, buff=0.45).to_edge(DOWN, buff=0.28)

        self.play(FadeIn(v1, shift=UP * 0.08), run_time=0.55)
        self.play(FadeIn(v2, shift=UP * 0.08), run_time=0.55)
        self.play(FadeIn(safe, shift=UP * 0.08), run_time=0.55)
        self.play(FadeIn(apps, shift=UP * 0.08), run_time=0.75)
        self.next_slide()


class HyperClawQuoteBridge(Slide):
    def construct(self):
        hdr = Text("HyperClaw in One Sentence", font_size=34, color=TEAL_B)
        hdr.to_edge(UP, buff=0.45)
        self.play(FadeIn(hdr), run_time=0.7)

        rings = VGroup(
            Circle(radius=1.45, color=BLUE_B, stroke_width=2.2, stroke_opacity=0.45),
            Circle(radius=2.35, color=TEAL_B, stroke_width=2.2, stroke_opacity=0.35),
            Circle(radius=3.25, color=GREEN_B, stroke_width=2.2, stroke_opacity=0.25),
        )
        quote = Text(
            "\"Attention is no longer hidden inside one model;\n"
            "it becomes the explicit protocol that coordinates the whole mind.\"",
            font_size=31, color=YELLOW_B, line_spacing=1.25, slant=ITALIC,
        ).move_to(ORIGIN + UP * 0.15)
        fit_width(quote, 10.8)

        bridge = lbox("HyperClaw connects orchestration to Hyperon cognition", TEAL_B, 19, 8.2).next_to(quote, DOWN, buff=0.42)
        thanks = Text("Thank you", font_size=34, color=GRAY_A).to_edge(DOWN, buff=0.42)

        self.play(FadeIn(rings, scale=0.85), run_time=0.65)
        self.play(FadeIn(quote, shift=UP * 0.12), FadeIn(bridge, shift=UP * 0.08), run_time=0.9)
        self.play(FadeIn(thanks, shift=UP * 0.08), run_time=0.65)
        self.next_slide()


# ──────────────────────────────────────────────────────────────────────────────
# Final Slide — The Conclusion
# ──────────────────────────────────────────────────────────────────────────────

class FinalConclusion(Slide):
    def construct(self):
        title = Text("The Path to Beneficial AGI", font_size=50, weight=BOLD,
                     gradient=(BLUE_B, GREEN_B, YELLOW_B))
        title.to_edge(UP, buff=0.5)
        self.play(FadeIn(title, shift=UP * 0.2), run_time=1.0)

        path_steps = VGroup(
            lbox("Math: Metagraph + Quantale + Merkle-DAG", TEAL_B, 20, 7.5),
            lbox("Infrastructure: MORK + MeTTa + DAS + ASI-Chain", BLUE_B, 20, 7.5),
            lbox("Cognition: PRIMUS Two-Loop + PLN + ECAN + MOSES + WILLIAM", PURPLE_B, 20, 7.5),
            lbox("Integration: QuantiMORK PC inside Atomspace + Symbolic Heads", GREEN_B, 20, 7.5),
            lbox("Safety: Invariants + Shadow Pipeline + Governance + Auditable CIDs", ORANGE, 20, 7.5),
            lbox("Applications: Qwestor · Math · Bio · Robotics · Finance", YELLOW_B, 20, 7.5),
        ).arrange(DOWN, buff=0.16).next_to(title, DOWN, buff=0.35)

        arrows = VGroup(*[Arrow(path_steps[i].get_bottom() + RIGHT * 0.5,
                                path_steps[i+1].get_top() + RIGHT * 0.5,
                                buff=0.04, stroke_width=3, color=GRAY_B)
                          for i in range(len(path_steps) - 1)])

        for step in path_steps:
            self.play(FadeIn(step, shift=UP * 0.08), run_time=0.38)
        self.play(Create(arrows, lag_ratio=0.1), run_time=0.7)
        self.next_slide()

        # Final tagline
        self.play(FadeOut(path_steps, arrows), run_time=0.5)
        quote = Text(
            '"Not AGI with safety bolted on afterward —\n AGI that is beneficial by construction."',
            font_size=34, color=YELLOW_B, line_spacing=1.4, slant=ITALIC,
        ).move_to(ORIGIN + DOWN * 0.2)
        attr = Text("— Ben Goertzel, Hyperon Whitepaper 2025", font_size=20, color=GRAY_A).next_to(quote, DOWN, buff=0.4)
        thanks = Text("Thank you", font_size=32, color=WHITE).next_to(attr, DOWN, buff=0.35)

        ring1 = Circle(radius=1.5, color=BLUE_B, stroke_width=2, stroke_opacity=0.4)
        ring2 = Circle(radius=2.5, color=TEAL_B, stroke_width=2, stroke_opacity=0.3)
        ring3 = Circle(radius=3.5, color=GREEN_B, stroke_width=2, stroke_opacity=0.2)
        rings = VGroup(ring1, ring2, ring3)

        self.play(FadeIn(rings, scale=0.8), run_time=0.7)
        self.play(FadeIn(quote, shift=UP * 0.2), FadeIn(attr), FadeIn(thanks, shift=UP * 0.08), run_time=1.0)
        self.play(
            ring1.animate.scale(1.08).set_stroke(opacity=0.6),
            ring2.animate.scale(1.06).set_stroke(opacity=0.45),
            ring3.animate.scale(1.04).set_stroke(opacity=0.3),
            run_time=1.0,
        )
        self.next_slide()
