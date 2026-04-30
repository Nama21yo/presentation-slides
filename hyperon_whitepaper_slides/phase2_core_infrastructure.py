"""
Phase 2 — Hyperon Core Infrastructure
Covers: Atomspace · MORK (WAS, ShardZipper, ByteFlow) · MeTTa language stack
         Space Abstraction · Distributed Atomspace · State Management
"""
from manim import *
from manim_slides import Slide
import numpy as np


# ──────────────────────────────────────────────────────────────────────────────
# Shared helpers (copy-friendly subset)
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


def label_box(text, color=WHITE, font=22, width=4.0, padding=0.22):
    t = Text(text, font_size=font, color=color, line_spacing=1.1)
    bg = RoundedRectangle(corner_radius=0.1, width=width, height=t.height + 2 * padding,
                          stroke_color=color, stroke_width=2,
                          fill_color=BLACK, fill_opacity=0.25)
    t.move_to(bg)
    return VGroup(bg, t)


def tag(text, color=TEAL_B):
    return label_box(text, color=color, font=24, width=max(len(text) * 0.17 + 0.8, 3.5))


# ──────────────────────────────────────────────────────────────────────────────
# 2.1 Atomspace — Universal Substrate
# ──────────────────────────────────────────────────────────────────────────────

class Phase2AtomspaceSubstrate(Slide):
    def construct(self):
        hdr = Text("Atomspace: Universal Cognitive Substrate", font_size=31, color=BLUE_B)
        hdr.to_edge(UP, buff=0.35)
        tg = tag("Everything = Atom", color=BLUE_B).next_to(hdr, DOWN, buff=0.25)
        self.play(FadeIn(hdr), FadeIn(tg), run_time=0.7)

        # Central Atomspace disk
        atomspace = Circle(radius=1.8, color=BLUE_B, fill_opacity=0.12)
        atomspace_label = Text("Atomspace", font_size=26, color=BLUE_B, weight=BOLD)
        center_group = VGroup(atomspace, atomspace_label).move_to(ORIGIN)
        self.play(Create(atomspace), FadeIn(atomspace_label), run_time=0.7)
        self.next_slide()

        # What lives in Atomspace
        categories = [
            ("Facts",           TEAL_B,   UP * 1.8 + LEFT * 3.5),
            ("Rules",           GREEN_B,  UP * 1.8 + RIGHT * 3.5),
            ("Goals",           YELLOW_B, DOWN * 1.8 + LEFT * 3.5),
            ("Neural weights",  PURPLE_B, DOWN * 1.8 + RIGHT * 3.5),
            ("Programs",        ORANGE,   UP * 0.1 + LEFT * 4.5),
            ("Edit ops",        RED_B,    UP * 0.1 + RIGHT * 4.5),
        ]
        for name, col, pos in categories:
            box = RoundedRectangle(corner_radius=0.1, width=2.4, height=0.5,
                                   stroke_color=col, fill_opacity=0.2).move_to(pos)
            t = Text(name, font_size=18, color=col).move_to(box)
            line = Line(pos, ORIGIN, color=col, stroke_width=2.5, stroke_opacity=0.55)
            self.play(FadeIn(VGroup(box, t)), Create(line), run_time=0.4)

        self.next_slide()

        # Atom types
        type_panel = panel("Atom Types",
                           ["Node — leaf atom (ConceptNode, PredicateNode…)",
                            "Link — non-leaf with typed outgoing targets",
                            "TruthValue — (strength, confidence) attached",
                            "AttentionValue — (STI, LTI) set by ECAN"],
                           width=7.5, tc=BLUE_B).to_edge(DOWN, buff=0.22)
        self.play(FadeIn(type_panel, shift=UP * 0.1), run_time=0.8)
        self.next_slide()


# ──────────────────────────────────────────────────────────────────────────────
# 2.2 MORK — The High-Performance Engine
# ──────────────────────────────────────────────────────────────────────────────

class Phase2MORKEngine(Slide):
    def construct(self):
        hdr = Text("MORK: MeTTa Optimal Reduction Kernel", font_size=30, color=ORANGE)
        hdr.to_edge(UP, buff=0.35)
        tg = tag("PathMap · Lock-Free · GPU-Ready", color=ORANGE).next_to(hdr, DOWN, buff=0.25)
        self.play(FadeIn(hdr), FadeIn(tg), run_time=0.7)

        # Architecture layers
        layers_data = [
            ("PathMap / Merkle-DAG", "Content-addressed prefix trie — near-O(1) lookup",  ORANGE),
            ("Weighted Atom Sweeps (WAS)", "Scheduler: sample atoms by importance, recency, uncertainty", YELLOW_B),
            ("ShardZipper",          "Extract sub-graph shard → run GPU kernel → zip back", TEAL_B),
            ("ByteFlow",             "Pack hot sub-tries into contiguous memory for kernels", GREEN_B),
        ]
        layer_vg = VGroup()
        for i, (name, desc, col) in enumerate(layers_data):
            rect = RoundedRectangle(corner_radius=0.1, width=10.5, height=0.75,
                                    stroke_color=col, stroke_width=2.2,
                                    fill_color=BLACK, fill_opacity=0.25).move_to(DOWN * (0.3 + i * 0.9))
            n_t = Text(name, font_size=20, color=col, weight=BOLD).move_to(rect).shift(LEFT * 2.5)
            d_t = Text(desc, font_size=16, color=WHITE).move_to(rect).shift(RIGHT * 1.8)
            layer_vg.add(VGroup(rect, n_t, d_t))

        for l in layer_vg:
            self.play(FadeIn(l, shift=UP * 0.08), run_time=0.5)
        self.next_slide()

        # WAS detail
        was_detail = panel("Weighted Atom Sweeps (WAS) — How it works",
                           ["Each PathMap node carries aggregate weight from children",
                            "Weight = recency + relevance + uncertainty + goal alignment",
                            "Weighted random walk: descend by probability ∝ weight",
                            "Lock-free: many cognitive processes sweep simultaneously",
                            "Acts as cognitive scheduler — urgent tasks get compute first"],
                           width=10.0, tc=YELLOW_B)
        was_detail.to_edge(DOWN, buff=0.18)
        self.play(FadeOut(layer_vg), FadeIn(was_detail, shift=UP * 0.08), run_time=0.7)
        self.next_slide()

        # ShardZipper detail
        self.play(FadeOut(was_detail), run_time=0.4)
        shz_flow = VGroup(
            label_box("MORK\nAtomspace", color=ORANGE, font=16, width=2.35).move_to(LEFT * 5.0 + DOWN * 0.5),
            label_box("Extract\nshard", color=TEAL_B, font=16, width=2.35).move_to(LEFT * 1.75 + DOWN * 0.5),
            label_box("GPU\nkernel", color=GREEN_B, font=16, width=2.35).move_to(RIGHT * 1.45 + DOWN * 0.5),
            label_box("Zip back\nverified", color=ORANGE, font=16, width=2.35).move_to(RIGHT * 4.65 + DOWN * 0.5),
        )
        arrows_shz = VGroup(*[
            Arrow(shz_flow[i].get_right(), shz_flow[i+1].get_left(), buff=0.06, stroke_width=4)
            for i in range(3)
        ])
        shz_title = Text("ShardZipper pipeline", font_size=22, color=TEAL_B).to_edge(UP, buff=2.8)
        self.play(FadeIn(shz_title), FadeIn(shz_flow, lag_ratio=0.15), Create(arrows_shz), run_time=1.0)
        self.next_slide()


# ──────────────────────────────────────────────────────────────────────────────
# 2.3 MeTTa Language Stack
# ──────────────────────────────────────────────────────────────────────────────

class Phase2MeTTaLanguageStack(Slide):
    def construct(self):
        hdr = Text("MeTTa Language & Execution Stack", font_size=32, color=PURPLE_B)
        hdr.to_edge(UP, buff=0.35)
        tg = tag("Homoiconic · Multi-backend · Cognitive Code", color=PURPLE_B).next_to(hdr, DOWN, buff=0.25)
        self.play(FadeIn(hdr), FadeIn(tg), run_time=0.7)

        # Stack diagram
        stack = [
            ("MeTTa",           "High-level pattern-rewrite language · Programs = Atoms",     "#4a1a6a", PURPLE_B),
            ("PyMeTTa",         "Python-syntax dialect → transpiles to MeTTa-IL",              "#1a3a5a", BLUE_B),
            ("MeTTa-IL",        "Intermediate lang · typed · compiles to all backends",        "#1a4a3a", TEAL_B),
            ("PeTTa / JeTTa",   "Prolog-based (PeTTa) or JVM/Android (JeTTa) compilers",      "#3a4a1a", GREEN_B),
            ("MM2 / MORKL",     "Low-level hot-loop kernels on PathMap · factor-graph PLN",    "#5a3a1a", ORANGE),
        ]
        stack_vg = VGroup()
        for i, (name, desc, fill, stroke) in enumerate(stack):
            rect = RoundedRectangle(corner_radius=0.1, width=10.5, height=0.76,
                                    stroke_color=stroke, stroke_width=2.2,
                                    fill_color=fill, fill_opacity=0.38).move_to(DOWN * (0.3 + i * 0.88))
            n_t = Text(name, font_size=20, color=stroke, weight=BOLD).move_to(rect).shift(LEFT * 2.8)
            d_t = Text(desc, font_size=15, color=WHITE).move_to(rect).shift(RIGHT * 1.8)
            stack_vg.add(VGroup(rect, n_t, d_t))

        for l in stack_vg:
            self.play(FadeIn(l, shift=UP * 0.07), run_time=0.45)
        self.next_slide()

        # Homoiconic highlight
        homo = label_box(
            "Homoiconic: MeTTa programs ARE graph rewrites stored in Atomspace\n"
            "  → Self-referential · Enables meta-reasoning & self-modification",
            color=YELLOW_B, font=19, width=10.5, padding=0.28,
        ).to_edge(DOWN, buff=0.22)
        self.play(FadeIn(homo, shift=UP * 0.08), run_time=0.7)
        self.next_slide()

        # Multi-target compilation
        self.play(FadeOut(stack_vg[3:]), FadeOut(homo), run_time=0.4)
        targets = VGroup(
            label_box("MORK\n(in-RAM)", color=ORANGE, font=18, width=2.2).move_to(LEFT * 4.0 + DOWN * 1.5),
            label_box("Rholang\n(blockchain)", color=TEAL_B, font=18, width=2.2).move_to(LEFT * 1.5 + DOWN * 1.5),
            label_box("JAX / XLA\n(GPU arrays)", color=GREEN_B, font=18, width=2.2).move_to(RIGHT * 1.0 + DOWN * 1.5),
            label_box("Android\n(JeTTa/JVM)", color=BLUE_B, font=18, width=2.2).move_to(RIGHT * 3.5 + DOWN * 1.5),
        )
        compile_label = label_box("MeTTa-IL  →  Compiles to:", color=PURPLE_B, font=20, width=5.5).move_to(UP * 0.0)
        t_arrows = VGroup(*[Arrow(compile_label[0].get_bottom(), t.get_top(), buff=0.06, color=GRAY_B, stroke_width=3) for t in targets])
        self.play(FadeIn(compile_label), FadeIn(targets, lag_ratio=0.12), Create(t_arrows), run_time=1.0)
        self.next_slide()


# ──────────────────────────────────────────────────────────────────────────────
# 2.4 Space Abstraction
# ──────────────────────────────────────────────────────────────────────────────

class Phase2SpaceAbstraction(Slide):
    def construct(self):
        hdr = Text("Space Abstraction", font_size=34, color=TEAL_B)
        hdr.to_edge(UP, buff=0.35)
        tg = tag("One API · Many Backends", color=TEAL_B).next_to(hdr, DOWN, buff=0.25)
        self.play(FadeIn(hdr), FadeIn(tg), run_time=0.7)

        # API box in center
        api = RoundedRectangle(corner_radius=0.15, width=3.5, height=1.2,
                               stroke_color=TEAL_B, stroke_width=3, fill_opacity=0.15).move_to(ORIGIN + UP * 0.4)
        api_t = Text("Space API\n(match · bind · rewrite)", font_size=20, color=TEAL_B,
                     line_spacing=1.2).move_to(api)
        self.play(Create(api), FadeIn(api_t), run_time=0.7)

        spaces = [
            ("MORK Atomspace",       ORANGE,   LEFT  * 4.5 + DOWN * 0.8),
            ("Distributed DAS",      BLUE_B,   LEFT  * 4.5 + DOWN * 2.0),
            ("Rholang Space",        GREEN_B,  RIGHT * 4.5 + DOWN * 0.8),
            ("Neural Space (LLM)",   PURPLE_B, RIGHT * 4.5 + DOWN * 2.0),
            ("Android / JeTTa",      YELLOW_B, ORIGIN + DOWN * 2.2),
        ]
        for name, col, pos in spaces:
            box = RoundedRectangle(corner_radius=0.1, width=3.0, height=0.55,
                                   stroke_color=col, fill_opacity=0.18).move_to(pos)
            t = Text(name, font_size=17, color=col).move_to(box)
            line = Line(api[0].get_bottom(), pos, color=col, stroke_width=2.2, stroke_opacity=0.6)
            self.play(FadeIn(VGroup(box, t)), Create(line), run_time=0.4)

        insight = Text(
            "MeTTa code is Space-independent:\n"
            "pattern-match works identically on local RAM, a cluster, or a blockchain node.",
            font_size=20, color=WHITE, line_spacing=1.25,
        ).to_edge(DOWN, buff=0.28)
        self.play(FadeIn(insight), run_time=0.7)
        self.next_slide()


# ──────────────────────────────────────────────────────────────────────────────
# 2.5 Distributed Atomspace (DAS)
# ──────────────────────────────────────────────────────────────────────────────

class Phase2DistributedAtomspace(Slide):
    def construct(self):
        hdr = Text("Distributed Atomspace (DAS)", font_size=34, color=BLUE_B)
        hdr.to_edge(UP, buff=0.35)
        tg = tag("Multi-Node · Sharding · Decentralized", color=BLUE_B).next_to(hdr, DOWN, buff=0.25)
        self.play(FadeIn(hdr), FadeIn(tg), run_time=0.7)

        # Show nodes
        node_positions = [
            LEFT * 4.5 + UP * 0.5,
            LEFT * 1.5 + UP * 1.5,
            RIGHT * 1.5 + UP * 0.5,
            LEFT * 3.0 + DOWN * 1.5,
            RIGHT * 3.5 + DOWN * 0.5,
        ]
        node_circles = VGroup(*[
            Circle(radius=0.55, color=BLUE_B, fill_opacity=0.2).move_to(p)
            for p in node_positions
        ])
        node_labels = VGroup(*[
            Text(f"Node {i+1}", font_size=16, color=BLUE_B).move_to(node_positions[i])
            for i in range(5)
        ])
        self.play(FadeIn(node_circles, lag_ratio=0.1), FadeIn(node_labels, lag_ratio=0.1), run_time=0.9)

        # Edges between nodes
        edges = VGroup(*[
            Line(node_positions[i], node_positions[j], color=GRAY_B, stroke_width=2.0)
            for i, j in [(0,1),(1,2),(2,4),(0,3),(3,4),(1,3)]
        ])
        self.play(Create(edges, lag_ratio=0.08), run_time=0.8)

        # Shard labels
        shards = [
            (LEFT * 5.5 + UP * 1.4, "Shard: bio-genes", TEAL_B),
            (RIGHT * 4.8 + UP * 1.4, "Shard: reasoning", GREEN_B),
            (LEFT * 2.0 + DOWN * 2.5, "Shard: goals",    YELLOW_B),
        ]
        for pos, lbl, col in shards:
            box = RoundedRectangle(corner_radius=0.1, width=2.5, height=0.45,
                                   stroke_color=col, fill_opacity=0.18).move_to(pos)
            t = Text(lbl, font_size=15, color=col).move_to(box)
            self.play(FadeIn(VGroup(box, t)), run_time=0.4)

        props = panel("DAS Properties",
                      ["MongoDB/Redis shard back-end",
                       "Space API is transparent — code unaware of distribution",
                       "MettaCycle + Rholang for capability-secured execution",
                       "ASI-Chain: cryptographic provenance for all changes",
                       "Rollback via CheckpointRef in ≤ 2 min MTTR"],
                      width=7.5, tc=BLUE_B).to_edge(DOWN, buff=0.22)
        self.play(FadeIn(props, shift=UP * 0.08), run_time=0.8)
        self.next_slide()


# ──────────────────────────────────────────────────────────────────────────────
# 2.6 State Management System
# ──────────────────────────────────────────────────────────────────────────────

class Phase2StateManagement(Slide):
    def construct(self):
        hdr = Text("State Management System (SMS)", font_size=33, color=GREEN_B)
        hdr.to_edge(UP, buff=0.35)
        tg = tag("Versioning · Rollback · Provenance", color=GREEN_B).next_to(hdr, DOWN, buff=0.25)
        self.play(FadeIn(hdr), FadeIn(tg), run_time=0.7)

        # Four artifacts
        artifacts = [
            ("CheckpointRef",  "Full state snapshot ID",                 TEAL_B,  LEFT * 4.0 + UP * 0.6),
            ("UpdatePatch",    "Incremental delta since checkpoint",      GREEN_B, RIGHT * 0.5 + UP * 0.6),
            ("ChangeDigest",   "Quick difference summary",                YELLOW_B,LEFT * 4.0 + DOWN * 0.8),
            ("InfluenceSketch","Approx. impact for optimization",         ORANGE,  RIGHT * 0.5 + DOWN * 0.8),
        ]
        for name, desc, col, pos in artifacts:
            box = RoundedRectangle(corner_radius=0.12, width=4.2, height=1.0,
                                   stroke_color=col, fill_opacity=0.2).move_to(pos)
            n = Text(name, font_size=20, color=col, weight=BOLD).move_to(box).shift(UP * 0.22)
            d = Text(desc, font_size=16, color=WHITE).move_to(box).shift(DOWN * 0.2)
            self.play(FadeIn(VGroup(box, n, d)), run_time=0.5)

        self.next_slide()

        # CRDT + rollback
        crdt = Text("CRDT G-counters for edge weights → clean merges across replicas (no locks)",
                    font_size=20, color=TEAL_B).to_edge(DOWN, buff=0.75)
        rollback = Text("Rholang lens contracts provide capability-controlled access + rollback",
                        font_size=20, color=GREEN_B).to_edge(DOWN, buff=0.38)
        self.play(FadeIn(crdt), FadeIn(rollback), run_time=0.7)
        self.next_slide()

        # Full system view
        full = panel("Why this matters for AGI safety",
                     ["Every thought, learning event, code edit is cryptographically trackable",
                      "AGI can prove it has not corrupted core values (Merkle root check)",
                      "Shadow→Elevate→Rollback: safe self-modification protocol",
                      "Multi-party DAOs can audit and approve system upgrades"],
                     width=10.5, tc=GREEN_B).to_edge(DOWN, buff=0.22)
        self.play(FadeOut(crdt, rollback), FadeIn(full, shift=UP * 0.1), run_time=0.8)
        self.next_slide()
