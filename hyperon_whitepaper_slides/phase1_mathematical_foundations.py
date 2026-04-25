"""
Phase 1 — Mathematical & Representational Foundations
Covers: Sets→Relations→Graphs → Hypergraphs → Metagraphs (CRITICAL)
         Content Addressing → Merkle DAG → Trie → Quantales
         Uncertainty / PLN Truth Values → Predictive Coding
"""
from manim import *
from manim_slides import Slide
import numpy as np


# ──────────────────────────────────────────────────────────────────────────────
# Shared helpers
# ──────────────────────────────────────────────────────────────────────────────

def panel(title, bullets, width=5.8, tc=BLUE_B, fc=22, ft=27):
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


def label_box(text, color=WHITE, font=24, width=4.5, padding=0.22):
    t = Text(text, font_size=font, color=color)
    bg = RoundedRectangle(corner_radius=0.1, width=width, height=t.height + 2 * padding,
                          stroke_color=color, stroke_width=2,
                          fill_color=BLACK, fill_opacity=0.25)
    t.move_to(bg)
    return VGroup(bg, t)


def tag(text, color=TEAL_B):
    return label_box(text, color=color, font=26, width=max(len(text) * 0.18 + 0.8, 3.5))


def node_circle(label, color=BLUE_B, radius=0.45):
    c = Circle(radius=radius, color=color, fill_opacity=0.2)
    t = Text(label, font_size=20, color=color).move_to(c)
    return VGroup(c, t)


def x_mark(pos, col=RED_B, s=0.32):
    return VGroup(
        Line(pos + UL * s, pos + DR * s, color=col, stroke_width=7),
        Line(pos + UR * s, pos + DL * s, color=col, stroke_width=7),
    )


# ──────────────────────────────────────────────────────────────────────────────
# 1.1 Sets → Relations → Graphs
# ──────────────────────────────────────────────────────────────────────────────

class Phase1SetsRelationsGraphs(Slide):
    def construct(self):
        hdr = Text("1.1 — Sets → Relations → Graphs", font_size=34, color=BLUE_B)
        hdr.to_edge(UP, buff=0.35)
        tg = tag("Mathematical Foundations").next_to(hdr, DOWN, buff=0.25)
        self.play(FadeIn(hdr), FadeIn(tg), run_time=0.7)
        self.next_slide()

        # SET
        set_box = RoundedRectangle(corner_radius=0.25, width=5.5, height=1.4,
                                   stroke_color=BLUE_B, fill_opacity=0.15).move_to(LEFT * 3.2 + UP * 1.1)
        set_label = Text("Set  S = { apple, 7, cat }", font_size=22, color=BLUE_B).move_to(set_box)
        s_note = Text("Unordered · No duplicates · No relationships", font_size=17, color=GRAY_A).next_to(set_box, DOWN, buff=0.12)
        self.play(Create(set_box), FadeIn(set_label), FadeIn(s_note), run_time=0.8)
        self.next_slide()

        # ORDERED PAIR → RELATION
        pair = Text("Ordered pair:  (Alice, Bob) ≠ (Bob, Alice)", font_size=22, color=TEAL_B)
        pair.next_to(set_box, RIGHT, buff=0.8).shift(UP * 0.2)
        rel = Text("Relation R ⊆ V × V\n= { (Alice,Bob), (Bob,Carol) }", font_size=20,
                   color=TEAL_B, line_spacing=1.2).next_to(pair, DOWN, buff=0.2)
        self.play(FadeIn(pair), FadeIn(rel), run_time=0.7)
        self.next_slide()

        # GRAPH
        positions = [LEFT * 3.5 + DOWN * 0.9, LEFT * 1.5 + DOWN * 0.9, LEFT * 2.5 + DOWN * 2.1]
        names = ["Alice", "Bob", "Carol"]
        nodes_g = VGroup(*[node_circle(n, BLUE_B, 0.42).move_to(p)
                           for n, p in zip(names, positions)])
        edges_g = VGroup(
            Arrow(positions[0] + RIGHT * 0.45, positions[1] + LEFT * 0.45, buff=0, stroke_width=4, color=WHITE),
            Arrow(positions[1] + DOWN * 0.42 + LEFT * 0.15, positions[2] + UP * 0.42 + RIGHT * 0.1,
                  buff=0, stroke_width=4, color=WHITE),
        )
        g_label = Text("Directed Graph G = (V, E)", font_size=22, color=WHITE).move_to(LEFT * 2.5 + DOWN * 2.9)
        self.play(FadeIn(nodes_g, lag_ratio=0.15), Create(edges_g), FadeIn(g_label), run_time=1.0)
        self.next_slide()

        # limitation annotation
        limit = Text("⚠  Edges are anonymous — carry no metadata!", font_size=22, color=RED_B)
        limit.to_edge(DOWN, buff=0.45)
        self.play(FadeIn(limit, scale=1.05), run_time=0.6)
        self.next_slide()


# ──────────────────────────────────────────────────────────────────────────────
# 1.2 Hypergraphs
# ──────────────────────────────────────────────────────────────────────────────

class Phase1Hypergraphs(Slide):
    def construct(self):
        hdr = Text("1.2 — Hypergraphs", font_size=34, color=GREEN_B)
        hdr.to_edge(UP, buff=0.35)
        tg = tag("Multi-Node Edges", color=GREEN_B).next_to(hdr, DOWN, buff=0.25)
        self.play(FadeIn(hdr), FadeIn(tg), run_time=0.7)

        # Problem: binary edges for group
        problem = Text(
            "Gene A + Gene B + Gene C bind together\nas a single protein complex.",
            font_size=24, color=WHITE, line_spacing=1.2,
        ).move_to(UP * 1.6)
        self.play(FadeIn(problem), run_time=0.6)
        self.next_slide()

        # Binary attempt — messy
        positions = [LEFT * 3.5 + DOWN * 0.5, LEFT * 1.2 + DOWN * 0.0, LEFT * 2.4 + DOWN * 1.6]
        genes = ["Gene A", "Gene B", "Gene C"]
        nodes = VGroup(*[node_circle(g, BLUE_B, 0.48).move_to(p) for g, p in zip(genes, positions)])
        binary_edges = VGroup(
            Line(positions[0], positions[1], color=GRAY_B, stroke_width=3),
            Line(positions[1], positions[2], color=GRAY_B, stroke_width=3),
            Line(positions[0], positions[2], color=GRAY_B, stroke_width=3),
        )
        wrong_label = Text("3 binary edges → semantically wrong!", font_size=20, color=RED_B)
        wrong_label.move_to(RIGHT * 2.2 + DOWN * 0.4)
        self.play(FadeIn(nodes, lag_ratio=0.12), Create(binary_edges), FadeIn(wrong_label), run_time=0.9)

        xm = x_mark(ORIGIN + DOWN * 1.1)
        self.play(FadeIn(xm), run_time=0.4)
        self.next_slide()

        # Hyperedge solution
        self.play(FadeOut(VGroup(binary_edges, wrong_label, xm)), run_time=0.5)
        hyperedge = RoundedRectangle(
            corner_radius=0.75, width=3.6, height=2.6,
            stroke_color=GREEN_B, stroke_width=6,
            fill_color=GREEN_E, fill_opacity=0.14,
        ).move_to(VGroup(*nodes).get_center())
        h_label = Text("Hyperedge = one unified\nA+B+C protein complex", font_size=20,
                       color=GREEN_B, line_spacing=1.2).next_to(hyperedge, RIGHT, buff=0.4)
        self.play(Create(hyperedge), FadeIn(h_label), run_time=0.9)

        key = panel("Hypergraph advantage",
                    ["One edge connects N nodes simultaneously",
                     "Biologically / logically accurate",
                     "Still: edges have no identity (next problem)"],
                    width=5.5, tc=GREEN_B).to_edge(DOWN, buff=0.25)
        self.play(FadeIn(key, shift=UP * 0.1), run_time=0.7)
        self.next_slide()


# ──────────────────────────────────────────────────────────────────────────────
# 1.3 Metagraphs — CRITICAL
# ──────────────────────────────────────────────────────────────────────────────

class Phase1MetagraphsCritical(Slide):
    def construct(self):
        hdr = Text("1.3 — Metagraphs  ★ CRITICAL ★", font_size=33, color=PURPLE_B)
        hdr.to_edge(UP, buff=0.35)
        tg = tag("Links are First-Class Atoms", color=PURPLE_B).next_to(hdr, DOWN, buff=0.25)
        self.play(FadeIn(hdr), FadeIn(tg), run_time=0.7)

        insight = Text(
            "Nodes and Links are both Atoms.\nLinks can connect Links.",
            font_size=26, color=YELLOW_B, line_spacing=1.3, weight=BOLD,
        ).next_to(tg, DOWN, buff=0.4)
        self.play(FadeIn(insight), run_time=0.6)
        self.next_slide()

        # Build the example step by step
        gene_a = label_box("Gene A", color=BLUE_B, font=20, width=2.0).move_to(LEFT * 5.2 + DOWN * 0.1)
        gene_b = label_box("Gene B", color=BLUE_B, font=20, width=2.0).move_to(LEFT * 2.6 + DOWN * 0.1)
        self.play(FadeIn(gene_a), FadeIn(gene_b), run_time=0.6)

        # Step 1: base edge becomes atom
        reg_link = label_box("RegulationLink", color=PURPLE_B, font=18, width=2.8).move_to(LEFT * 3.9 + DOWN * 1.3)
        la = Arrow(gene_a[0].get_bottom(), reg_link[0].get_top() + LEFT * 0.5,
                   buff=0.06, color=PURPLE_B, stroke_width=3)
        lb = Arrow(gene_b[0].get_bottom(), reg_link[0].get_top() + RIGHT * 0.5,
                   buff=0.06, color=PURPLE_B, stroke_width=3)
        step1 = Text("Step 1: Edge is itself an Atom", font_size=20, color=PURPLE_B).to_edge(RIGHT, buff=0.5).shift(UP * 1.0)
        self.play(FadeIn(reg_link), GrowArrow(la), GrowArrow(lb), FadeIn(step1), run_time=0.9)
        self.next_slide()

        # Step 2: EvaluationLink attaches truth value to the link
        eval_link = label_box("EvaluationLink\n(strength=0.8, conf=0.9)", color=GREEN_B,
                              font=16, width=3.4).move_to(RIGHT * 0.8 + UP * 0.4)
        e_arrow = Arrow(eval_link[0].get_left(), reg_link[0].get_right(),
                        buff=0.06, color=GREEN_B, stroke_width=3)
        step2 = Text("Step 2: Confidence attaches to the relation itself", font_size=19, color=GREEN_B)
        step2.to_edge(RIGHT, buff=0.3).shift(DOWN * 0.1)
        self.play(FadeIn(eval_link), GrowArrow(e_arrow), FadeIn(step2), run_time=0.9)
        self.next_slide()

        # Step 3: InhibitionLink from Drug X → RegulationLink
        drug_x = label_box("Drug X", color=ORANGE, font=18, width=1.9).move_to(RIGHT * 1.8 + DOWN * 1.4)
        inhib = label_box("InhibitionLink", color=ORANGE, font=16, width=2.5).move_to(RIGHT * 1.2 + DOWN * 2.4)
        i1 = Arrow(drug_x[0].get_bottom(), inhib[0].get_top(), buff=0.06, color=ORANGE, stroke_width=3)
        i2 = Arrow(inhib[0].get_left(), reg_link[0].get_right() + DOWN * 0.15,
                   buff=0.06, color=ORANGE, stroke_width=3)
        step3 = Text("Step 3: Drug X inhibits the relationship, not the genes!", font_size=18, color=ORANGE)
        step3.to_edge(DOWN, buff=0.6)
        self.play(FadeIn(drug_x), FadeIn(inhib), GrowArrow(i1), GrowArrow(i2), FadeIn(step3), run_time=1.0)
        self.next_slide()

        summary = panel("Metagraph = Atomspace Foundation",
                        ["Every node and link = Atom",
                         "Infinite compositional structure",
                         "Facts · rules · goals · neural weights in ONE fabric"],
                        width=6.5, tc=PURPLE_B)
        summary.to_edge(DOWN, buff=0.22)
        self.play(FadeOut(step1, step2, step3), FadeIn(summary, shift=UP * 0.1), run_time=0.8)
        self.next_slide()


# ──────────────────────────────────────────────────────────────────────────────
# 1.4 Content Addressing
# ──────────────────────────────────────────────────────────────────────────────

class Phase1ContentAddressing(Slide):
    def construct(self):
        hdr = Text("1.4 — Content Addressing & CIDs", font_size=34, color=YELLOW_B)
        hdr.to_edge(UP, buff=0.35)
        tg = tag("Hash = Identity", color=YELLOW_B).next_to(hdr, DOWN, buff=0.25)
        self.play(FadeIn(hdr), FadeIn(tg), run_time=0.7)

        question = Text("A billion Atoms — how do we find one specific thought?",
                        font_size=26, color=WHITE).next_to(tg, DOWN, buff=0.35)
        self.play(FadeIn(question), run_time=0.6)
        self.next_slide()

        # Two identity systems
        loc = label_box("Location-based ID\n'Row 483, Column B'", color=GRAY_A, font=20, width=4.0)
        loc.move_to(LEFT * 3.5 + DOWN * 0.5)
        content_id = label_box("Content-based ID (CID)\nHash(structure) = 0x9c7b2f…a31d", color=YELLOW_B, font=20, width=4.8)
        content_id.move_to(RIGHT * 2.5 + DOWN * 0.5)
        vs = Text("vs", font_size=30, color=GRAY_A).move_to(ORIGIN + DOWN * 0.5)
        self.play(FadeIn(loc), FadeIn(vs), FadeIn(content_id), run_time=0.9)
        self.next_slide()

        # Hash pipeline
        atom = label_box("Atom Structure", color=BLUE_B, font=18, width=2.5).move_to(LEFT * 4.5 + DOWN * 1.8)
        sha = label_box("SHA-256", color=TEAL_B, font=18, width=2.2).move_to(LEFT * 1.8 + DOWN * 1.8)
        cid_box = label_box("CID: 0x9c7b2f…", color=YELLOW_B, font=18, width=2.8).move_to(RIGHT * 1.5 + DOWN * 1.8)
        a1 = Arrow(atom.get_right(), sha.get_left(), buff=0.06, stroke_width=4)
        a2 = Arrow(sha.get_right(), cid_box.get_left(), buff=0.06, stroke_width=4)
        self.play(FadeIn(atom), GrowArrow(a1), FadeIn(sha), GrowArrow(a2), FadeIn(cid_box), run_time=1.0)
        self.play(Flash(cid_box.get_center(), color=YELLOW_B), run_time=0.4)

        props = panel("CID Properties",
                      ["Same structure ⟹ same CID (deduplication)",
                       "Change one character ⟹ completely new CID",
                       "Multiple modules automatically share same Atom",
                       "No location needed — structure IS the address"],
                      width=7.5, tc=YELLOW_B).to_edge(DOWN, buff=0.2)
        self.play(FadeIn(props, shift=UP * 0.1), run_time=0.7)
        self.next_slide()


# ──────────────────────────────────────────────────────────────────────────────
# 1.4.2 Merkle Structures
# ──────────────────────────────────────────────────────────────────────────────

class Phase1MerkleStructures(Slide):
    def construct(self):
        hdr = Text("1.4.2 — Merkle Tree & Merkle-DAG", font_size=34, color=GREEN_B)
        hdr.to_edge(UP, buff=0.35)
        tg = tag("Immutability + Verifiable Updates", color=GREEN_B).next_to(hdr, DOWN, buff=0.25)
        self.play(FadeIn(hdr), FadeIn(tg), run_time=0.7)

        # Build a small Merkle tree
        LEAF_Y = -2.2
        leaf_labels = ["h(GeneA)", "h(GeneB)", "h(RegLink)", "h(Context)"]
        leaf_xs = [-5.0, -2.5, 0.0, 2.5]
        leaves = VGroup()
        leaf_boxes = []
        for lbl, x in zip(leaf_labels, leaf_xs):
            b = RoundedRectangle(corner_radius=0.06, width=1.9, height=0.48,
                                 stroke_color=GRAY_A, stroke_width=1.8,
                                 fill_color=BLACK, fill_opacity=0.22).move_to([x, LEAF_Y, 0])
            t = Text(lbl, font_size=16, color=GRAY_A).move_to(b)
            leaves.add(VGroup(b, t))
            leaf_boxes.append(b)

        MID_Y = -1.15
        mid_xs = [-3.75, 1.25]
        mid_labels = ["H(AB)", "H(CD)"]
        mids = VGroup()
        mid_boxes = []
        for lbl, x in zip(mid_labels, mid_xs):
            b = RoundedRectangle(corner_radius=0.06, width=2.0, height=0.48,
                                 stroke_color=TEAL_B, stroke_width=2,
                                 fill_color=BLACK, fill_opacity=0.22).move_to([x, MID_Y, 0])
            t = Text(lbl, font_size=17, color=TEAL_B).move_to(b)
            mids.add(VGroup(b, t))
            mid_boxes.append(b)

        ROOT_Y = -0.0
        root_box = RoundedRectangle(corner_radius=0.08, width=2.4, height=0.52,
                                    stroke_color=YELLOW_B, stroke_width=2.5,
                                    fill_color=BLACK, fill_opacity=0.22).move_to([-1.25, ROOT_Y, 0])
        root_t = Text("Merkle Root", font_size=18, color=YELLOW_B).move_to(root_box)

        connectors = VGroup(
            Line(leaf_boxes[0].get_top(), mid_boxes[0].get_bottom() + LEFT * 0.3, color=TEAL_B, stroke_width=2.2),
            Line(leaf_boxes[1].get_top(), mid_boxes[0].get_bottom() + RIGHT * 0.3, color=TEAL_B, stroke_width=2.2),
            Line(leaf_boxes[2].get_top(), mid_boxes[1].get_bottom() + LEFT * 0.3, color=TEAL_B, stroke_width=2.2),
            Line(leaf_boxes[3].get_top(), mid_boxes[1].get_bottom() + RIGHT * 0.3, color=TEAL_B, stroke_width=2.2),
            Line(mid_boxes[0].get_top(), root_box.get_bottom() + LEFT * 0.4, color=YELLOW_B, stroke_width=2.5),
            Line(mid_boxes[1].get_top(), root_box.get_bottom() + RIGHT * 0.4, color=YELLOW_B, stroke_width=2.5),
        )

        self.play(FadeIn(leaves, lag_ratio=0.1), run_time=0.8)
        self.play(Create(connectors[:4]), FadeIn(mids), run_time=0.8)
        self.play(Create(connectors[4:]), FadeIn(root_box), FadeIn(root_t), run_time=0.7)
        self.play(Flash(root_box.get_center(), color=YELLOW_B), run_time=0.4)
        self.next_slide()

        # Merkle proof path
        proof_path = VGroup(
            leaf_boxes[2].copy().set_stroke(color=GREEN_B, width=4),
            mid_boxes[1].copy().set_stroke(color=GREEN_B, width=4),
            root_box.copy().set_stroke(color=GREEN_B, width=4),
        )
        proof_label = Text("O(log n) Merkle proof — verifies one Atom in a billion",
                           font_size=20, color=GREEN_B).to_edge(RIGHT, buff=0.25).shift(UP * 0.5)
        self.play(FadeIn(proof_path, lag_ratio=0.2), FadeIn(proof_label), run_time=0.9)
        self.next_slide()

        # DAG sharing
        shared_note = Text("Merkle-DAG: shared sub-structures → no duplicates → lock-free writes",
                           font_size=20, color=ORANGE).to_edge(DOWN, buff=0.45)
        shared_arrow = Arrow(leaf_boxes[1].get_center(), leaf_boxes[2].get_center() + LEFT * 0.5,
                              buff=0, color=ORANGE, stroke_width=3)
        share_label = Text("shared", font_size=16, color=ORANGE).next_to(shared_arrow, DOWN, buff=0.08)
        self.play(FadeIn(shared_note), Create(shared_arrow), FadeIn(share_label), run_time=0.8)
        self.next_slide()


# ──────────────────────────────────────────────────────────────────────────────
# 1.5 Trie / PathMap
# ──────────────────────────────────────────────────────────────────────────────

class Phase1TriePathMap(Slide):
    def construct(self):
        hdr = Text("1.5 — Trie & PathMap (MORK's Core)", font_size=34, color=ORANGE)
        hdr.to_edge(UP, buff=0.35)
        tg = tag("Prefix-based Address Space", color=ORANGE).next_to(hdr, DOWN, buff=0.25)
        self.play(FadeIn(hdr), FadeIn(tg), run_time=0.7)

        question = Text("MORK stores Atoms in a compressed prefix trie = PathMap",
                        font_size=24, color=WHITE).next_to(tg, DOWN, buff=0.35)
        self.play(FadeIn(question), run_time=0.5)
        self.next_slide()

        # Trie visualization
        trie_data = {
            "root":  np.array([0.0,  1.6, 0]),
            "0":     np.array([-2.5, 0.6, 0]),
            "1":     np.array([ 2.5, 0.6, 0]),
            "00":    np.array([-3.5,-0.4, 0]),
            "01":    np.array([-1.5,-0.4, 0]),
            "10":    np.array([ 1.5,-0.4, 0]),
            "11":    np.array([ 3.5,-0.4, 0]),
            "010":   np.array([-2.5,-1.5, 0]),
            "011":   np.array([-0.5,-1.5, 0]),
        }
        node_colors = {"root": WHITE, "0": BLUE_B, "1": TEAL_B,
                       "00": BLUE_B, "01": BLUE_B, "10": TEAL_B, "11": TEAL_B,
                       "010": GREEN_B, "011": YELLOW_B}
        trie_group = VGroup()
        trie_nodes = {}
        for key, pos in trie_data.items():
            c = Circle(radius=0.26, color=node_colors[key], fill_opacity=0.22).move_to(pos)
            t = Text(key, font_size=16, color=node_colors[key]).move_to(c)
            trie_nodes[key] = c
            trie_group.add(VGroup(c, t))
            if key != "root":
                parent = key[:-1] if key[:-1] != "" else "root"
                trie_group.add(Line(trie_data[parent], pos, color=GRAY_B, stroke_width=2.2))

        self.play(FadeIn(trie_group, lag_ratio=0.04), run_time=1.2)
        self.next_slide()

        # Traversal highlight
        path = ["root", "0", "01", "011"]
        trail = Dot(trie_data["root"], radius=0.1, color=YELLOW_B)
        self.play(FadeIn(trail), run_time=0.3)
        for key in path[1:]:
            self.play(trail.animate.move_to(trie_data[key]), run_time=0.4)
        self.play(Flash(trie_data["011"], color=YELLOW_B), run_time=0.4)

        label_found = Text("O(depth) lookup — near constant time!", font_size=22, color=YELLOW_B)
        label_found.to_edge(RIGHT, buff=0.4).shift(UP * 0.2)
        self.play(FadeIn(label_found), run_time=0.5)
        self.next_slide()

        props = panel("PathMap Properties",
                      ["Near-constant-time neighborhood lookups",
                       "Lock-free updates (immutable nodes)",
                       "Memory layouts support symbolic + dense numeric",
                       "Weighted Atom Sweeps (WAS) traverse by importance"],
                      width=6.5, tc=ORANGE).to_edge(DOWN, buff=0.25)
        self.play(FadeIn(props, shift=UP * 0.1), run_time=0.7)
        self.next_slide()


# ──────────────────────────────────────────────────────────────────────────────
# 1.6 Quantales — Algebra of Reasoning
# ──────────────────────────────────────────────────────────────────────────────

class Phase1Quantales(Slide):
    def construct(self):
        hdr = Text("1.6 — Quantales: Algebra of Reasoning", font_size=34, color=TEAL_B)
        hdr.to_edge(UP, buff=0.35)
        tg = tag("Lattice + Multiplication", color=TEAL_B).next_to(hdr, DOWN, buff=0.25)
        self.play(FadeIn(hdr), FadeIn(tg), run_time=0.7)
        self.next_slide()

        # Lattice diagram
        top = label_box("⊤  (True / Certain)", TEAL_B, 18, 3.0).move_to(UP * 1.5)
        a = label_box("A", BLUE_B, 18, 1.4).move_to(LEFT * 1.8 + UP * 0.2)
        b = label_box("B", BLUE_B, 18, 1.4).move_to(RIGHT * 1.8 + UP * 0.2)
        bot = label_box("⊥  (False / Unknown)", RED_B, 18, 3.2).move_to(DOWN * 1.1)
        lat_lines = VGroup(
            Line(top.get_bottom(), a.get_top(), color=TEAL_B, stroke_width=2.5),
            Line(top.get_bottom(), b.get_top(), color=TEAL_B, stroke_width=2.5),
            Line(a.get_bottom(), bot.get_top(), color=TEAL_B, stroke_width=2.5),
            Line(b.get_bottom(), bot.get_top(), color=TEAL_B, stroke_width=2.5),
        )
        join_label = Text("Join ⊕ = least upper bound", font_size=18, color=GREEN_B).to_edge(RIGHT, buff=0.3).shift(UP * 1.0)
        meet_label = Text("Meet = greatest lower bound", font_size=18, color=ORANGE).to_edge(RIGHT, buff=0.3).shift(UP * 0.3)
        self.play(FadeIn(VGroup(top, a, b, bot)), Create(lat_lines),
                  FadeIn(join_label), FadeIn(meet_label), run_time=1.0)
        self.next_slide()

        # Quantale adds multiplication
        mult_box = RoundedRectangle(corner_radius=0.14, width=10.5, height=1.1,
                                    stroke_color=PURPLE_B, stroke_width=2.5,
                                    fill_color=BLACK, fill_opacity=0.25).to_edge(DOWN, buff=1.8)
        mult_text = Text(
            "Quantale = Lattice  ⊕ (join)  +  Multiplication ⊗ (composition)\n"
            "  Supports:  uncertainty  ·  composition  ·  reasoning paths",
            font_size=20, color=PURPLE_B, line_spacing=1.2,
        ).move_to(mult_box)
        self.play(FadeIn(mult_box), FadeIn(mult_text), run_time=0.8)
        self.next_slide()

        # Usage across PRIMUS
        usage = panel("Where quantales appear in Hyperon",
                      ["PLN truth-value propagation uses quantale products",
                       "Weakness prior: 'simplicity' defined per quantale",
                       "Geodesic control: f·g measured in quantale",
                       "Factor-graph message passing uses ⊕ and ⊗"],
                      width=8.5, tc=PURPLE_B).to_edge(DOWN, buff=0.22)
        self.play(FadeIn(usage, shift=UP * 0.1), run_time=0.8)
        self.next_slide()


# ──────────────────────────────────────────────────────────────────────────────
# 1.7 Uncertainty — PLN Truth Values
# ──────────────────────────────────────────────────────────────────────────────

class Phase1PLNTruthValues(Slide):
    def construct(self):
        hdr = Text("1.7 — Uncertainty: PLN Truth Values", font_size=34, color=GREEN_B)
        hdr.to_edge(UP, buff=0.35)
        tg = tag("(strength, confidence)", color=GREEN_B).next_to(hdr, DOWN, buff=0.25)
        self.play(FadeIn(hdr), FadeIn(tg), run_time=0.7)

        # Why classical logic fails
        classical = Text(
            "Classical logic: statements are TRUE or FALSE.\n"
            "Reality: 'Gene A regulates Gene B' — observed in 12 of 14 experiments.",
            font_size=22, color=WHITE, line_spacing=1.3,
        ).next_to(tg, DOWN, buff=0.35)
        self.play(FadeIn(classical), run_time=0.7)
        self.next_slide()

        # PLN truth value pair
        tv_box = RoundedRectangle(corner_radius=0.2, width=6.5, height=2.0,
                                  stroke_color=GREEN_B, stroke_width=2.5,
                                  fill_color=BLACK, fill_opacity=0.25).move_to(DOWN * 0.4)
        tv_formula = MathTex(
            r"\text{TruthValue} = \langle s, c \rangle",
            font_size=36, color=GREEN_B,
        ).move_to(tv_box).shift(UP * 0.4)
        tv_explain = Text(
            "s = strength (how often true?)    c = confidence (how much data?)",
            font_size=20, color=WHITE,
        ).move_to(tv_box).shift(DOWN * 0.35)
        self.play(FadeIn(tv_box), FadeIn(tv_formula), FadeIn(tv_explain), run_time=0.9)
        self.next_slide()

        # Example atoms
        ex_a = label_box("(RegulationLink Gene_A Gene_B)\n  TV = ⟨0.86, 0.90⟩", GREEN_B, 18, 5.0)
        ex_b = label_box("(InheritanceLink Alice Human)\n  TV = ⟨1.0, 0.99⟩", GREEN_B, 18, 5.0)
        ex_c = label_box("(ContextLink DrugX RegLink)\n  TV = ⟨0.5, 0.30⟩  ← low confidence", ORANGE, 18, 5.5)
        examples = VGroup(ex_a, ex_b, ex_c).arrange(DOWN, buff=0.22).to_edge(DOWN, buff=0.2)
        self.play(FadeIn(examples, lag_ratio=0.15), run_time=1.0)
        self.next_slide()

        # Inference preserves uncertainty
        infer = Text("Inference propagates (s,c) — no hallucination, no silent loss of evidence.",
                     font_size=22, color=YELLOW_B, weight=BOLD).to_edge(DOWN, buff=0.25)
        self.play(FadeIn(infer), run_time=0.6)
        self.next_slide()


# ──────────────────────────────────────────────────────────────────────────────
# 1.8 Learning Paradigms — Predictive Coding & Causal Coding
# ──────────────────────────────────────────────────────────────────────────────

class Phase1PredictiveCoding(Slide):
    def construct(self):
        hdr = Text("1.8 — Predictive Coding & Causal Coding", font_size=33, color=TEAL_B)
        hdr.to_edge(UP, buff=0.35)
        tg = tag("Local Updates · No Global Backprop", color=TEAL_B).next_to(hdr, DOWN, buff=0.25)
        self.play(FadeIn(hdr), FadeIn(tg), run_time=0.7)
        self.next_slide()

        # Standard backprop vs PC side-by-side
        # Left: backprop
        bp_title = Text("Standard Backprop", font_size=24, color=RED_B).move_to(LEFT * 3.5 + UP * 1.5)
        layers_bp = VGroup(*[
            RoundedRectangle(corner_radius=0.1, width=1.6, height=0.52,
                             stroke_color=RED_B, fill_opacity=0.18).move_to(LEFT * 3.5 + UP * (0.5 - i * 0.85))
            for i in range(4)
        ])
        labels_bp = VGroup(*[
            Text(f"Layer {4-i}", font_size=16, color=RED_B).move_to(layers_bp[i])
            for i in range(4)
        ])
        fwd = Arrow(layers_bp[0].get_bottom(), layers_bp[3].get_bottom() + UP * 0.1,
                    buff=0, color=RED_B, stroke_width=3)
        bwd = Arrow(layers_bp[3].get_bottom(), layers_bp[0].get_bottom() + UP * 0.1,
                    buff=0, color=RED_B, stroke_width=3)
        fwd_t = Text("Forward", font_size=16, color=RED_B).next_to(fwd, LEFT, buff=0.1)
        bwd_t = Text("Backward\n(global!)", font_size=16, color=RED_B, line_spacing=1.1).next_to(bwd, RIGHT, buff=0.1)
        self.play(FadeIn(bp_title), FadeIn(layers_bp), FadeIn(labels_bp), run_time=0.7)
        self.play(Create(fwd), FadeIn(fwd_t), Create(bwd), FadeIn(bwd_t), run_time=0.8)
        self.next_slide()

        # Right: predictive coding
        pc_title = Text("Predictive Coding (PC)", font_size=24, color=GREEN_B).move_to(RIGHT * 3.2 + UP * 1.5)
        layers_pc = VGroup(*[
            RoundedRectangle(corner_radius=0.1, width=1.6, height=0.52,
                             stroke_color=GREEN_B, fill_opacity=0.18).move_to(RIGHT * 3.2 + UP * (0.5 - i * 0.85))
            for i in range(4)
        ])
        for i, layer in enumerate(layers_pc):
            pred = Arrow(layer.get_top(), layers_pc[i-1].get_bottom() if i > 0 else layer.get_top() + UP * 0.5,
                         buff=0.04, color=TEAL_B, stroke_width=2.5, max_tip_length_to_length_ratio=0.2)
            err  = Arrow(layer.get_bottom() if i < 3 else layer.get_bottom(),
                         layers_pc[min(i+1,3)].get_top() if i < 3 else layer.get_bottom() + DOWN * 0.4,
                         buff=0.04, color=ORANGE, stroke_width=2.5, max_tip_length_to_length_ratio=0.2)
            self.add(pred, err)
        self.play(FadeIn(pc_title), FadeIn(layers_pc), run_time=0.7)

        local_note = Text("Each layer: predict ↑ + update on error ↓\nNo global backward pass needed!",
                          font_size=18, color=GREEN_B, line_spacing=1.2).to_edge(RIGHT, buff=0.3).shift(DOWN * 1.5)
        self.play(FadeIn(local_note), run_time=0.6)
        self.next_slide()

        props = panel("Why PC matters for Hyperon",
                      ["Works inside Atomspace (QuantiMORK integration)",
                       "Asynchronous & distributed training",
                       "Continual learning without catastrophic forgetting",
                       "Naturally pairs with PLN probabilistic semantics"],
                      width=10.0, tc=TEAL_B).to_edge(DOWN, buff=0.25)
        self.play(FadeIn(props, shift=UP * 0.1), run_time=0.8)
        self.next_slide()
