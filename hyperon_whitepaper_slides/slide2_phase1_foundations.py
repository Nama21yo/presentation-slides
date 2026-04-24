from manim import *
from manim_slides import Slide


class HyperonPhase1Base(Slide):
    def build_question(self, text: str) -> Text:
        q = Text(text, font_size=30, color=WHITE, line_spacing=1.2)
        q.to_edge(UP, buff=0.35)
        return q

    def build_tag(self, text: str, color=TEAL_B) -> VGroup:
        box = RoundedRectangle(
            corner_radius=0.12,
            width=4.2,
            height=0.6,
            stroke_color=color,
            stroke_width=2,
            fill_color=BLACK,
            fill_opacity=0.25,
        )
        label = Text(text, font_size=25, color=color).move_to(box)
        return VGroup(box, label)


class Phase1StandardGraphsSlide(HyperonPhase1Base):
    def construct(self):
        question = self.build_question(
            "How do we represent data to build an AGI?\nCan a simple graph hold complex thoughts?"
        )
        tag = self.build_tag("Standard Graph", color=BLUE_B).next_to(question, DOWN, buff=0.28)

        node_a = Circle(radius=0.65, color=BLUE_B, fill_opacity=0.25).move_to(LEFT * 3.2 + UP * 0.3)
        node_b = Circle(radius=0.65, color=BLUE_B, fill_opacity=0.25).move_to(RIGHT * 1.3 + UP * 0.3)
        text_a = Text("Concept", font_size=24).move_to(node_a)
        text_b = Text("Attribute", font_size=20).move_to(node_b)
        edge = Arrow(node_a.get_right(), node_b.get_left(), buff=0.14, color=WHITE, stroke_width=4)

        self.play(FadeIn(question, shift=UP * 0.2), FadeIn(tag, shift=UP * 0.2), run_time=1.1)
        self.play(Create(node_a), Create(node_b), FadeIn(text_a), FadeIn(text_b), run_time=1.1)
        self.play(GrowArrow(edge), run_time=0.9)

        self.next_slide()

        lens = VGroup(
            Circle(radius=0.36, color=YELLOW_B, stroke_width=4),
            Line(ORIGIN, DOWN * 0.45 + RIGHT * 0.35, color=YELLOW_B, stroke_width=5),
        ).move_to(edge.get_center() + UP * 0.6)
        tooltip = RoundedRectangle(
            corner_radius=0.08,
            width=2.65,
            height=0.5,
            stroke_color=RED_B,
            fill_color=BLACK,
            fill_opacity=0.3,
        ).next_to(edge, UP, buff=0.24)
        tooltip_text = Text("[NULL: No Identity]", font_size=21, color=RED_B).move_to(tooltip)

        self.play(FadeIn(lens, scale=0.9), run_time=0.5)
        self.play(edge.animate.set_color(RED_B).set_stroke(width=5), run_time=0.45)
        self.play(FadeIn(tooltip), FadeIn(tooltip_text), run_time=0.45)

        self.next_slide()

        node_c = Circle(radius=0.62, color=ORANGE, fill_opacity=0.22).move_to(DOWN * 1.45)
        text_c = Text("Confidence\n90%", font_size=20).move_to(node_c)
        try_arrow = Arrow(node_c.get_top(), edge.get_center(), buff=0.06, color=ORANGE, stroke_width=4)
        shatter = VGroup(
            Line(ORIGIN, RIGHT * 0.4 + UP * 0.25, color=RED_B, stroke_width=5),
            Line(ORIGIN, LEFT * 0.35 + UP * 0.24, color=RED_B, stroke_width=5),
            Line(ORIGIN, DOWN * 0.4, color=RED_B, stroke_width=5),
        ).move_to(edge.get_center())

        self.play(FadeIn(node_c, shift=DOWN * 0.2), FadeIn(text_c, shift=DOWN * 0.2), run_time=0.7)
        self.play(GrowArrow(try_arrow), run_time=0.55)
        self.play(try_arrow.animate.shift(DOWN * 0.28), Flash(edge.get_center(), color=RED_B), run_time=0.35)
        self.play(FadeOut(try_arrow), FadeIn(shatter, scale=0.7), run_time=0.35)
        self.play(FadeOut(shatter, shift=UP * 0.1), run_time=0.25)

        bullets = VGroup(
            Text("Nodes = First-Class (Hold Data)", font_size=24, color=BLUE_B),
            Text("Edges = Second-Class (Anonymous Wires)", font_size=24, color=RED_B),
        ).arrange(DOWN, aligned_edge=LEFT, buff=0.2).to_corner(DL, buff=0.55)

        self.play(FadeIn(bullets[0], shift=RIGHT * 0.2), FadeIn(bullets[1], shift=RIGHT * 0.2), run_time=0.9)
        self.next_slide()


class Phase1HypergraphsSlide(HyperonPhase1Base):
    def construct(self):
        question = self.build_question(
            "What if a cognitive thought involves multiple concepts\ninteracting simultaneously, rather than in pairs?"
        )
        tag = self.build_tag("Hypergraph", color=GREEN_B).next_to(question, DOWN, buff=0.28)

        positions = [LEFT * 3 + UP * 0.6, LEFT * 1.0 + UP * 1.0, RIGHT * 1.5 + UP * 0.3, LEFT * 0.2 + DOWN * 1.0]
        labels = ["A", "B", "C", "D"]
        nodes = VGroup()
        for pos, lbl in zip(positions, labels):
            c = Circle(radius=0.48, color=BLUE_B, fill_opacity=0.22).move_to(pos)
            t = Text(lbl, font_size=28).move_to(c)
            nodes.add(VGroup(c, t))

        self.play(FadeIn(question, shift=UP * 0.2), FadeIn(tag, shift=UP * 0.2), run_time=1.0)
        self.play(LaggedStart(*[FadeIn(n, scale=0.9) for n in nodes], lag_ratio=0.15), run_time=1.1)

        lines = VGroup()
        for i in range(4):
            for j in range(i + 1, 4):
                l = Line(nodes[i].get_center(), nodes[j].get_center(), color=GRAY_B, stroke_width=2.5, stroke_opacity=0.9)
                lines.add(l)
        red_x = VGroup(
            Line(LEFT * 2.8 + DOWN * 1.9, RIGHT * 2.8 + UP * 1.8, color=RED_B, stroke_width=8),
            Line(LEFT * 2.8 + UP * 1.8, RIGHT * 2.8 + DOWN * 1.9, color=RED_B, stroke_width=8),
        )

        self.play(Create(lines, lag_ratio=0.08), run_time=1.0)
        self.play(FadeIn(red_x), run_time=0.28)

        self.next_slide()

        boundary = RoundedRectangle(
            corner_radius=0.8,
            width=5.65,
            height=3.0,
            stroke_color=GREEN_B,
            stroke_width=6,
            fill_color=GREEN_E,
            fill_opacity=0.12,
        ).move_to(VGroup(nodes[0], nodes[1], nodes[2]).get_center() + RIGHT * 0.05)

        self.play(FadeOut(red_x), Uncreate(lines), run_time=0.6)
        self.play(Create(boundary), run_time=0.9)

        bullets = VGroup(
            Text("Hyperedge: Connects N-nodes simultaneously", font_size=22, color=GREEN_B),
            Text("Limitation: Still lacks internal identity", font_size=22, color=RED_B),
        ).arrange(DOWN, aligned_edge=LEFT, buff=0.2).to_corner(DL, buff=0.55)
        self.play(FadeIn(bullets[0], shift=UP * 0.1), FadeIn(bullets[1], shift=UP * 0.1), run_time=0.9)

        self.next_slide()

        timestamp = Text("timestamp=2025-01-17", font_size=18, color=ORANGE).to_edge(RIGHT, buff=0.6).shift(UP * 0.8)
        pointer = Arrow(timestamp.get_left(), boundary.get_right(), buff=0.1, color=ORANGE, stroke_width=4)
        self.play(FadeIn(timestamp, shift=LEFT * 0.2), GrowArrow(pointer), run_time=0.8)
        self.play(boundary.animate.set_stroke(color=GRAY_B).set_fill(opacity=0.05), Flash(boundary.get_center(), color=GRAY_B), run_time=0.5)
        self.play(FadeOut(pointer), FadeOut(timestamp), run_time=0.35)
        self.next_slide()


class Phase1MetagraphsSlide(HyperonPhase1Base):
    def construct(self):
        question = self.build_question(
            "How does an AGI reason about its own reasoning?\nWhere do we attach metadata to a relationship?"
        )
        tag = self.build_tag("Metagraph", color=PURPLE_B).next_to(question, DOWN, buff=0.28)

        a = Circle(radius=0.52, color=BLUE_B, fill_opacity=0.22).move_to(LEFT * 3 + DOWN * 0.1)
        b = Circle(radius=0.52, color=BLUE_B, fill_opacity=0.22).move_to(LEFT * 0.4 + DOWN * 0.1)
        ta = Text("A", font_size=30).move_to(a)
        tb = Text("B", font_size=30).move_to(b)
        edge = Arrow(a.get_right(), b.get_left(), buff=0.08, color=WHITE, stroke_width=5)

        self.play(FadeIn(question, shift=UP * 0.2), FadeIn(tag, shift=UP * 0.2), run_time=1.0)
        self.play(Create(a), Create(b), FadeIn(ta), FadeIn(tb), GrowArrow(edge), run_time=1.0)

        self.next_slide()

        edge_atom = Circle(radius=0.45, color=BLUE_B, fill_opacity=0.25).move_to(edge.get_center())
        edge_atom_label = Text("Link", font_size=18).move_to(edge_atom)
        self.play(Transform(edge, edge_atom), FadeIn(edge_atom_label), run_time=0.9)

        atom_labels = VGroup(
            Text("Atom", font_size=20, color=YELLOW_B).next_to(a, UP, buff=0.15),
            Text("Atom", font_size=20, color=YELLOW_B).next_to(b, UP, buff=0.15),
            Text("Atom", font_size=20, color=YELLOW_B).next_to(edge_atom, UP, buff=0.12),
        )
        self.play(LaggedStart(*[FadeIn(x, shift=UP * 0.1) for x in atom_labels], lag_ratio=0.15), run_time=0.9)

        truth_box = RoundedRectangle(
            corner_radius=0.1,
            width=3.9,
            height=0.78,
            stroke_color=GREEN_B,
            fill_color=GREEN_E,
            fill_opacity=0.2,
        ).to_edge(RIGHT, buff=0.4).shift(UP * 0.9)
        truth_text = Text("TruthValue: (0.8, 0.9)", font_size=21, color=GREEN_B).move_to(truth_box)
        t_arrow = Arrow(truth_box.get_left(), edge_atom.get_right(), buff=0.08, color=GREEN_B, stroke_width=4)

        self.play(FadeIn(truth_box), FadeIn(truth_text), GrowArrow(t_arrow), run_time=0.95)

        self.next_slide()

        context_box = RoundedRectangle(
            corner_radius=0.1,
            width=4.1,
            height=0.78,
            stroke_color=ORANGE,
            fill_color=BLACK,
            fill_opacity=0.25,
        ).to_edge(RIGHT, buff=0.4).shift(DOWN * 0.35)
        context_text = Text('Context: "During Training"', font_size=20, color=ORANGE).move_to(context_box)
        c_arrow = Arrow(context_box.get_left(), t_arrow.get_center(), buff=0.08, color=ORANGE, stroke_width=4)

        self.play(FadeIn(context_box), FadeIn(context_text), GrowArrow(c_arrow), run_time=0.9)

        web = VGroup()
        center = RIGHT * 2.3 + DOWN * 0.45
        hubs = [center + RIGHT * 1.0 + UP * 1.1, center + RIGHT * 1.25 + DOWN * 1.05, center + RIGHT * 2.2 + UP * 0.1]
        for h in hubs:
            hub_dot = Dot(h, radius=0.055, color=PURPLE_B)
            web.add(hub_dot)
            for source in [truth_box.get_center(), context_box.get_center(), edge_atom.get_center()]:
                link = Arrow(source, h, buff=0.2, color=PURPLE_B, stroke_width=2.5, max_tip_length_to_length_ratio=0.16)
                web.add(link)

        self.play(FadeIn(web, lag_ratio=0.07), run_time=1.0)

        bullets = VGroup(
            Text('Edges = Nodes = "Atoms"', font_size=24, color=YELLOW_B),
            Text("Infinite Compositional Structure", font_size=24, color=PURPLE_B),
        ).arrange(DOWN, aligned_edge=LEFT, buff=0.15).to_corner(DL, buff=0.55)
        self.play(FadeIn(bullets, shift=UP * 0.1), run_time=0.7)
        self.next_slide()


class Phase1ContentAddressingSlide(HyperonPhase1Base):
    def construct(self):
        question = self.build_question(
            "If an AGI's mind holds a billion interconnected Atoms,\nhow does it find a specific thought without a central database?"
        )
        tag = self.build_tag("Content-Based Addressing", color=YELLOW_B).next_to(question, DOWN, buff=0.28)

        n1 = Circle(radius=0.38, color=GOLD_B, fill_opacity=0.25).move_to(LEFT * 3.2 + UP * 0.3)
        n2 = Circle(radius=0.38, color=GOLD_B, fill_opacity=0.25).move_to(LEFT * 1.9 + UP * 1.1)
        n3 = Circle(radius=0.38, color=GOLD_B, fill_opacity=0.25).move_to(LEFT * 1.3 + DOWN * 0.5)
        e1 = Line(n1.get_center(), n2.get_center(), color=GOLD_B, stroke_width=4)
        e2 = Line(n1.get_center(), n3.get_center(), color=GOLD_B, stroke_width=4)
        cluster = VGroup(e1, e2, n1, n2, n3)

        scanner = RoundedRectangle(
            corner_radius=0.1,
            width=0.9,
            height=2.6,
            stroke_color=TEAL_B,
            fill_color=TEAL_E,
            fill_opacity=0.2,
        ).move_to(cluster.get_left() + RIGHT * 0.2)
        scan_label = Text("SHA-256 Hash", font_size=18, color=TEAL_B).next_to(scanner, UP, buff=0.1)

        self.play(FadeIn(question, shift=UP * 0.2), FadeIn(tag, shift=UP * 0.2), run_time=1.0)
        self.play(Create(cluster), run_time=0.9)
        self.play(FadeIn(scanner), FadeIn(scan_label), scanner.animate.shift(RIGHT * 3.6), run_time=1.2)

        hash_text = Text("0x9c7b2f...a31d", font_size=34, color=YELLOW_B).move_to(RIGHT * 1.8 + UP * 0.2)
        self.play(FadeOut(cluster, scale=0.9), FadeIn(hash_text, shift=UP * 0.1), run_time=0.8)

        self.next_slide()

        divider = Line(UP * 2.1 + RIGHT * 0.1, DOWN * 2.8 + RIGHT * 0.1, color=GRAY_B, stroke_width=2.4)
        left_label = Text("Vision Module", font_size=24, color=BLUE_B).move_to(LEFT * 3.2 + UP * 1.9)
        right_label = Text("Logic Module", font_size=24, color=GREEN_B).move_to(RIGHT * 3.2 + UP * 1.9)

        l_cluster = cluster.copy().scale(0.72).move_to(LEFT * 3.2 + UP * 0.4)
        r_cluster = cluster.copy().scale(0.72).move_to(RIGHT * 3.2 + UP * 0.4)
        l_hash = Text("0x9c7b2f...a31d", font_size=24, color=YELLOW_B).move_to(LEFT * 2.5 + DOWN * 1.2)
        r_hash = Text("0x9c7b2f...a31d", font_size=24, color=YELLOW_B).move_to(RIGHT * 2.7 + DOWN * 1.2)

        self.play(
            FadeOut(hash_text),
            FadeOut(scanner),
            FadeOut(scan_label),
            FadeIn(divider),
            FadeIn(left_label),
            FadeIn(right_label),
            run_time=0.8,
        )
        self.play(FadeIn(l_cluster), FadeIn(r_cluster), run_time=0.7)
        self.play(FadeIn(l_hash), FadeIn(r_hash), run_time=0.5)
        self.play(l_hash.animate.move_to(DOWN * 1.45), r_hash.animate.move_to(DOWN * 1.45), run_time=0.9)
        merged_hash = Text("0x9c7b2f...a31d", font_size=28, color=YELLOW_B).move_to(DOWN * 1.45)
        self.play(FadeOut(VGroup(l_hash, r_hash)), FadeIn(merged_hash, scale=1.1), run_time=0.45)

        formula = Text("Structure -> Hash Function -> CID\nHash = Identity", font_size=23, color=WHITE, line_spacing=1.2)
        formula.to_corner(DL, buff=0.55)
        self.play(FadeIn(formula, shift=RIGHT * 0.2), run_time=0.7)
        self.next_slide()


class Phase1MerkleTreeSlide(HyperonPhase1Base):
    def construct(self):
        question = self.build_question(
            "How can an AGI mathematically prove it has not corrupted\nits own core values or memories?"
        )
        tag = self.build_tag("Merkle Tree", color=GREEN_B).next_to(question, DOWN, buff=0.28)

        self.play(FadeIn(question, shift=UP * 0.2), FadeIn(tag, shift=UP * 0.2), run_time=1.0)

        leaves = VGroup()
        leaf_boxes = VGroup()
        for i in range(8):
            box = RoundedRectangle(corner_radius=0.03, width=1.32, height=0.35, stroke_color=GRAY_A, stroke_width=1.6)
            box.move_to(np.array([-5.2 + i * 1.48, -2.4, 0.0]))
            txt = Text(f"h{i:02x}..", font_size=17, color=GRAY_A).move_to(box)
            leaves.add(txt)
            leaf_boxes.add(box)

        self.play(LaggedStart(*[FadeIn(VGroup(b, t), shift=UP * 0.1) for b, t in zip(leaf_boxes, leaves)], lag_ratio=0.08), run_time=1.0)

        def parent_level(children: VGroup, y: float, color):
            parents = VGroup()
            connectors = VGroup()
            for i in range(0, len(children), 2):
                left = children[i]
                right = children[i + 1]
                px = (left.get_center()[0] + right.get_center()[0]) / 2
                box = RoundedRectangle(corner_radius=0.03, width=1.32, height=0.35, stroke_color=color, stroke_width=1.9)
                box.move_to(np.array([px, y, 0.0]))
                txt = Text(f"H{i//2:02x}..", font_size=17, color=color).move_to(box)
                parents.add(VGroup(box, txt))

                c1 = Line(left.get_top(), box.get_bottom() + LEFT * 0.2, color=color, stroke_width=2.2)
                c2 = Line(right.get_top(), box.get_bottom() + RIGHT * 0.2, color=color, stroke_width=2.2)
                connectors.add(c1, c2)
            return parents, connectors

        level1, conn1 = parent_level(leaf_boxes, -1.4, BLUE_B)
        level2, conn2 = parent_level(VGroup(*[p[0] for p in level1]), -0.35, TEAL_B)
        level3, conn3 = parent_level(VGroup(*[p[0] for p in level2]), 0.75, GREEN_B)
        root = RoundedRectangle(corner_radius=0.04, width=1.6, height=0.42, stroke_color=YELLOW_B, stroke_width=2.6).move_to(UP * 1.75)
        root_text = Text("RootHash", font_size=20, color=YELLOW_B).move_to(root)
        root_c1 = Line(level3[0][0].get_top(), root.get_bottom(), color=YELLOW_B, stroke_width=2.5)

        self.play(Create(conn1, lag_ratio=0.05), FadeIn(level1, lag_ratio=0.1), run_time=1.0)
        self.play(Create(conn2, lag_ratio=0.05), FadeIn(level2, lag_ratio=0.1), run_time=0.9)
        self.play(Create(conn3, lag_ratio=0.05), FadeIn(level3, lag_ratio=0.1), run_time=0.9)
        self.play(Create(root_c1), FadeIn(root), FadeIn(root_text), run_time=0.8)
        self.play(root.animate.set_glow_factor(0.25), Flash(root.get_center(), color=YELLOW_B), run_time=0.45)

        self.next_slide()

        target_leaf = VGroup(leaf_boxes[5], leaves[5])
        path = VGroup(
            leaf_boxes[5].copy().set_stroke(color=GREEN_B, width=3),
            level1[2][0].copy().set_stroke(color=GREEN_B, width=3),
            level2[1][0].copy().set_stroke(color=GREEN_B, width=3),
            level3[0][0].copy().set_stroke(color=GREEN_B, width=3),
            root.copy().set_stroke(color=GREEN_B, width=3),
        )
        target_leaf[0].set_stroke(color=GREEN_B, width=3)
        proof_text = Text("O(log n) cryptographic verification", font_size=22, color=GREEN_B).next_to(path[2], RIGHT, buff=0.35)

        self.play(FadeIn(path, lag_ratio=0.12), run_time=1.1)
        self.play(FadeIn(proof_text, shift=RIGHT * 0.2), run_time=0.6)
        self.next_slide()


class Phase1MerkleDagPathMapSlide(HyperonPhase1Base):
    def construct(self):
        question = self.build_question(
            "If a fundamental concept is used in 100,000 thoughts,\ndo we store 100,000 copies of it in the tree?"
        )
        tag = self.build_tag("Merkle-DAG and PathMap", color=ORANGE).next_to(question, DOWN, buff=0.28)

        self.play(FadeIn(question, shift=UP * 0.2), FadeIn(tag, shift=UP * 0.2), run_time=1.0)

        roots = [np.array([-4.3, 1.0, 0.0]), np.array([-2.4, 1.0, 0.0]), np.array([-0.5, 1.0, 0.0])]
        mids = [np.array([-4.3, -0.1, 0.0]), np.array([-2.4, -0.1, 0.0]), np.array([-0.5, -0.1, 0.0])]
        leaves = [np.array([-4.3, -1.3, 0.0]), np.array([-2.4, -1.3, 0.0]), np.array([-0.5, -1.3, 0.0])]

        tree_group = VGroup()
        duplicates = VGroup()
        for i in range(3):
            r = Circle(radius=0.22, color=BLUE_B).move_to(roots[i])
            m = Circle(radius=0.22, color=TEAL_B).move_to(mids[i])
            w = RoundedRectangle(corner_radius=0.05, width=1.2, height=0.36, stroke_color=RED_B, fill_color=RED_E, fill_opacity=0.2).move_to(leaves[i])
            wt = Text("Concept: Water", font_size=14, color=RED_B).move_to(w)
            l1 = Line(r.get_bottom(), m.get_top(), color=GRAY_B, stroke_width=2.2)
            l2 = Line(m.get_bottom(), w.get_top(), color=GRAY_B, stroke_width=2.2)
            tree_group.add(r, m, l1, l2)
            duplicates.add(VGroup(w, wt))

        counter = Text("Duplicate memory copies: 3", font_size=22, color=RED_B).to_edge(LEFT, buff=0.45).shift(DOWN * 2.4)

        self.play(FadeIn(tree_group, lag_ratio=0.08), FadeIn(duplicates, lag_ratio=0.12), run_time=1.2)
        self.play(FadeIn(counter, shift=UP * 0.1), run_time=0.5)

        self.next_slide()

        shared = RoundedRectangle(corner_radius=0.05, width=1.35, height=0.38, stroke_color=GREEN_B, fill_color=GREEN_E, fill_opacity=0.25).move_to(np.array([-2.4, -1.6, 0.0]))
        shared_t = Text("Concept: Water", font_size=15, color=GREEN_B).move_to(shared)
        dag_lines = VGroup(
            Line(mids[0], shared.get_top() + LEFT * 0.38, color=GREEN_B, stroke_width=2.8),
            Line(mids[1], shared.get_top(), color=GREEN_B, stroke_width=2.8),
            Line(mids[2], shared.get_top() + RIGHT * 0.38, color=GREEN_B, stroke_width=2.8),
        )
        structural = Text("Structural Sharing", font_size=30, color=GREEN_B).to_edge(RIGHT, buff=0.6).shift(DOWN * 0.2)

        self.play(FadeOut(duplicates), FadeIn(VGroup(shared, shared_t)), run_time=0.7)
        self.play(Create(dag_lines), run_time=0.8)
        self.play(FadeIn(structural, scale=1.05), Flash(shared.get_center(), color=GREEN_B), run_time=0.7)

        self.next_slide()

        self.play(FadeOut(VGroup(tree_group, dag_lines, shared, shared_t, structural, counter), scale=0.96), run_time=0.7)

        trie_nodes = {
            "": np.array([1.8, 1.2, 0]),
            "0": np.array([0.8, 0.2, 0]),
            "1": np.array([2.8, 0.2, 0]),
            "01": np.array([1.4, -0.85, 0]),
            "011": np.array([1.9, -1.85, 0]),
            "0110": np.array([2.4, -2.6, 0]),
            "10": np.array([3.3, -0.85, 0]),
        }
        trie = VGroup()
        for key, pos in trie_nodes.items():
            if key:
                parent = key[:-1]
                trie.add(Line(trie_nodes[parent], pos, color=GRAY_B, stroke_width=2.2))
        for key, pos in trie_nodes.items():
            c = Circle(radius=0.2, color=BLUE_B, fill_opacity=0.2).move_to(pos)
            t = Text(key if key else "root", font_size=16, color=BLUE_B).move_to(c)
            trie.add(c, t)

        path_text = Text("MORK PathMap (Prefix Trie)", font_size=26, color=BLUE_B).to_edge(RIGHT, buff=0.35).shift(UP * 2.25)
        bit_trail = Dot(trie_nodes[""], radius=0.08, color=YELLOW_B)

        self.play(FadeIn(trie, lag_ratio=0.05), FadeIn(path_text, shift=UP * 0.15), run_time=1.0)
        self.play(bit_trail.animate.move_to(trie_nodes["0"]), run_time=0.45)
        self.play(bit_trail.animate.move_to(trie_nodes["01"]), run_time=0.45)
        self.play(bit_trail.animate.move_to(trie_nodes["011"]), run_time=0.45)
        self.play(bit_trail.animate.move_to(trie_nodes["0110"]), Flash(trie_nodes["0110"], color=YELLOW_B), run_time=0.55)
        self.next_slide()


class Phase1WhyMerkleDagMandatorySlide(HyperonPhase1Base):
    def construct(self):
        question = self.build_question(
            "Why is this cryptographic structure the digital physics\nof the Hyperon AGI stack?"
        )
        self.play(FadeIn(question, shift=UP * 0.2), run_time=0.8)

        col_lines = VGroup(
            Line(LEFT * 2.35 + UP * 2.5, LEFT * 2.35 + DOWN * 3, color=GRAY_C, stroke_width=2),
            Line(RIGHT * 2.35 + UP * 2.5, RIGHT * 2.35 + DOWN * 3, color=GRAY_C, stroke_width=2),
        )
        self.play(Create(col_lines), run_time=0.45)

        titles = VGroup(
            Text("Absolute\nDeduplication", font_size=24, color=YELLOW_B, line_spacing=1.1).move_to(LEFT * 4.8 + UP * 1.95),
            Text("Lock-Free\nConcurrency", font_size=24, color=BLUE_B, line_spacing=1.1).move_to(UP * 1.95),
            Text("Verifiable\nDelta Patches", font_size=24, color=GREEN_B, line_spacing=1.1).move_to(RIGHT * 4.8 + UP * 1.95),
        )
        self.play(FadeIn(titles, shift=UP * 0.12), run_time=0.65)

        self.next_slide()


# ===========================
# Refactored Phase 1 sequence
# ===========================


class HyperonPhase1RefinedBase(Slide):
    def _fit(self, t: Text, width: float, min_size: int = 16) -> Text:
        while t.width > width and t.font_size > min_size:
            t.scale(0.94)
        return t

    def text_box(
        self,
        text: str,
        width: float = 5.8,
        color=WHITE,
        font_size: int = 26,
        padding: float = 0.26,
        fill_opacity: float = 0.22,
        line_spacing: float = 1.12,
    ) -> VGroup:
        label = Text(text, font_size=font_size, color=color, line_spacing=line_spacing)
        self._fit(label, width - 2 * padding)
        panel = RoundedRectangle(
            corner_radius=0.12,
            width=width,
            height=label.height + 2 * padding,
            stroke_color=color,
            stroke_width=2,
            fill_color=BLACK,
            fill_opacity=fill_opacity,
        )
        label.move_to(panel)
        return VGroup(panel, label)

    def bullet_panel(self, title: str, bullets: list[str], width: float = 6.2, title_color=YELLOW_B) -> VGroup:
        title_t = Text(title, font_size=27, color=title_color)
        self._fit(title_t, width - 0.6)
        items = VGroup()
        for b in bullets:
            d = Dot(radius=0.04, color=title_color)
            t = Text(b, font_size=21, color=WHITE, line_spacing=1.08)
            self._fit(t, width - 0.95)
            items.add(VGroup(d, t).arrange(RIGHT, buff=0.13, aligned_edge=UP))
        items.arrange(DOWN, aligned_edge=LEFT, buff=0.16)
        content = VGroup(title_t, items).arrange(DOWN, aligned_edge=LEFT, buff=0.2)
        panel = RoundedRectangle(
            corner_radius=0.12,
            width=width,
            height=content.height + 0.45,
            stroke_color=GRAY_B,
            stroke_width=2,
            fill_color=BLACK,
            fill_opacity=0.24,
        )
        content.move_to(panel).shift(LEFT * 0.06)
        return VGroup(panel, content)


class Phase1QuestionOnlySlide(HyperonPhase1RefinedBase):
    def construct(self):
        title = Text("Phase 1 — Mathematical & Representational Foundations", font_size=34, color=BLUE_B)
        title.to_edge(UP, buff=0.4)
        q = self.text_box("How we represent data to build an AGI system?", width=10.5, font_size=48, padding=0.4)
        q.move_to(ORIGIN + DOWN * 0.05)
        self.play(FadeIn(title, shift=UP * 0.15), run_time=0.7)
        self.play(FadeIn(q, scale=0.98), run_time=1.0)
        self.next_slide()


class Phase1StandardGraphGeneSlide(HyperonPhase1RefinedBase):
    def construct(self):
        tag = self.text_box("Standard graph baseline", width=4.7, color=BLUE_B, font_size=28)
        tag.to_edge(UP, buff=0.35)

        a = Circle(radius=0.6, color=BLUE_B, fill_opacity=0.2).move_to(LEFT * 3.8 + UP * 0.8)
        b = Circle(radius=0.6, color=BLUE_B, fill_opacity=0.2).move_to(LEFT * 1.3 + UP * 0.8)
        la = Text("Gene A", font_size=20).move_to(a)
        lb = Text("Gene B", font_size=20).move_to(b)
        rel = Arrow(a.get_right(), b.get_left(), buff=0.08, color=WHITE, stroke_width=4)
        rel_t = Text("activates", font_size=18).next_to(rel, UP, buff=0.08)

        panel = self.bullet_panel(
            "What binary graph gives us",
            [
                "One edge naturally connects two entities",
                "Great for simple facts like Gene A -> Gene B",
                "But richer biology quickly outgrows this form",
            ],
            width=6.8,
            title_color=BLUE_B,
        )
        panel.to_edge(RIGHT, buff=0.4).shift(DOWN * 0.12)

        self.play(FadeIn(tag), run_time=0.5)
        self.play(FadeIn(VGroup(a, b, la, lb)), GrowArrow(rel), FadeIn(rel_t), run_time=0.9)
        self.play(FadeIn(panel, shift=LEFT * 0.08), run_time=0.8)
        self.next_slide()


class Phase1BinaryEdgesNotEnoughSlide(HyperonPhase1RefinedBase):
    def construct(self):
        tag = self.text_box("Why binary edges are not enough", width=6.6, color=RED_B, font_size=29)
        tag.to_edge(UP, buff=0.35)

        points = [LEFT * 4 + UP * 0.8, LEFT * 2.2 + UP * 1.0, LEFT * 3.1 + DOWN * 0.6]
        names = ["Gene A", "Gene B", "Gene C"]
        nodes = VGroup()
        for p, n in zip(points, names):
            c = Circle(radius=0.38, color=BLUE_B, fill_opacity=0.2).move_to(p)
            t = Text(n, font_size=17).move_to(c)
            nodes.add(VGroup(c, t))
        pair_edges = VGroup(
            Line(nodes[0].get_center(), nodes[1].get_center(), color=GRAY_B, stroke_width=2.8),
            Line(nodes[1].get_center(), nodes[2].get_center(), color=GRAY_B, stroke_width=2.8),
            Line(nodes[0].get_center(), nodes[2].get_center(), color=GRAY_B, stroke_width=2.8),
        )

        conf = self.text_box("confidence = 0.90", width=3.0, color=ORANGE, font_size=18, padding=0.2)
        cond = self.text_box("condition = liver tissue", width=3.8, color=ORANGE, font_size=17, padding=0.2)
        conf.move_to(LEFT * 1.0 + DOWN * 0.8)
        cond.next_to(conf, DOWN, buff=0.2)
        ca = Arrow(conf.get_left(), pair_edges[0].get_center(), buff=0.1, color=ORANGE, stroke_width=2.8)
        da = Arrow(cond.get_left(), pair_edges[1].get_center(), buff=0.1, color=ORANGE, stroke_width=2.8)

        panel = self.bullet_panel(
            "Main limitations",
            [
                "A+B+C complex is forced into three separate pair links",
                "Semantically wrong for one unified biological event",
                "Confidence and condition should attach to the relation itself",
            ],
            width=6.9,
            title_color=RED_B,
        )
        panel.to_edge(RIGHT, buff=0.2).shift(UP * 0.45)

        self.play(FadeIn(tag), run_time=0.5)
        self.play(FadeIn(nodes, lag_ratio=0.1), Create(pair_edges), run_time=0.9)
        self.play(FadeIn(conf), FadeIn(cond), GrowArrow(ca), GrowArrow(da), run_time=0.8)
        self.play(FadeIn(panel), run_time=0.7)
        self.next_slide()


class Phase1HypergraphSlide(HyperonPhase1RefinedBase):
    def construct(self):
        tag = self.text_box("Hypergraph solution for group relations", width=7.4, color=GREEN_B, font_size=29)
        tag.to_edge(UP, buff=0.35)

        points = [LEFT * 3.7 + UP * 0.8, LEFT * 1.8 + UP * 0.9, LEFT * 2.8 + DOWN * 0.7]
        genes = VGroup()
        for p, n in zip(points, ["Gene A", "Gene B", "Gene C"]):
            c = Circle(radius=0.4, color=BLUE_B, fill_opacity=0.2).move_to(p)
            t = Text(n, font_size=18).move_to(c)
            genes.add(VGroup(c, t))
        hyperedge = RoundedRectangle(corner_radius=0.65, width=3.45, height=2.45, stroke_color=GREEN_B, stroke_width=5, fill_color=GREEN_E, fill_opacity=0.12).move_to(VGroup(*genes).get_center())
        h_text = Text("Hyperedge = one A+B+C complex", font_size=19, color=GREEN_B).next_to(hyperedge, DOWN, buff=0.16)

        panel = self.bullet_panel(
            "What improves",
            [
                "A single edge now connects multiple genes at once",
                "Group interaction is represented faithfully",
                "Next gap: edge still not fully first-class",
            ],
            width=6.5,
            title_color=GREEN_B,
        )
        panel.to_edge(RIGHT, buff=0.38).shift(DOWN * 0.08)

        self.play(FadeIn(tag), run_time=0.5)
        self.play(FadeIn(genes, lag_ratio=0.12), run_time=0.8)
        self.play(Create(hyperedge), FadeIn(h_text), run_time=0.85)
        self.play(FadeIn(panel), run_time=0.7)
        self.next_slide()


class Phase1GraphLimitsAndFirstClassSlide(HyperonPhase1RefinedBase):
    def construct(self):
        tag = self.text_box("First-class relations", width=4.8, color=YELLOW_B, font_size=29)
        tag.to_edge(UP, buff=0.35)

        node_a = self.text_box("Gene A", width=2.2, color=BLUE_B, font_size=20).move_to(LEFT * 4.4 + UP * 0.55)
        node_b = self.text_box("Gene B", width=2.2, color=BLUE_B, font_size=20).move_to(LEFT * 1.8 + UP * 0.55)
        edge = Arrow(node_a.get_right(), node_b.get_left(), buff=0.08, color=WHITE, stroke_width=4)
        edge_label = Text("regulates", font_size=18, color=WHITE).next_to(edge, UP, buff=0.1)

        left = self.bullet_panel(
            "Second-class edge",
            ["Anonymous wire only", "Hard to target directly", "Metadata has no clean anchor"],
            width=5.3,
            title_color=RED_B,
        ).move_to(LEFT * 3.2 + DOWN * 1.45)

        edge_atom = Circle(radius=0.45, color=PURPLE_B, fill_opacity=0.22).move_to(RIGHT * 1.0 + UP * 0.55)
        edge_atom_label = Text("RegulationLink", font_size=16, color=PURPLE_B).move_to(edge_atom)
        meta = self.text_box("confidence = 0.8", width=3.1, color=GREEN_B, font_size=17, padding=0.2).move_to(RIGHT * 4.0 + UP * 1.35)
        meta_arrow = Arrow(meta.get_left(), edge_atom.get_right(), buff=0.08, color=GREEN_B, stroke_width=3)

        right = self.bullet_panel(
            "First-class relation",
            ["Link has identity", "Other links can reference it", "Context/causality attach naturally"],
            width=5.3,
            title_color=GREEN_B,
        ).move_to(RIGHT * 3.6 + DOWN * 1.45)

        transition = Arrow(LEFT * 0.2 + UP * 0.55, RIGHT * 0.55 + UP * 0.55, buff=0.05, color=YELLOW_B, stroke_width=4)

        self.play(FadeIn(tag), run_time=0.5)
        self.play(FadeIn(node_a), FadeIn(node_b), GrowArrow(edge), FadeIn(edge_label), run_time=0.9)
        self.play(FadeIn(left), run_time=0.6)
        self.play(GrowArrow(transition), run_time=0.4)
        self.play(Transform(edge, edge_atom), FadeOut(edge_label), FadeIn(edge_atom_label), run_time=0.8)
        self.play(FadeIn(meta), GrowArrow(meta_arrow), FadeIn(right), run_time=0.9)
        self.next_slide()


class Phase1MetagraphConceptSlide(HyperonPhase1RefinedBase):
    def construct(self):
        tag = self.text_box("Metagraph concept", width=4.2, color=PURPLE_B, font_size=30)
        tag.to_edge(UP, buff=0.35)

        gene_a = self.text_box("Gene A", width=2.0, color=BLUE_B, font_size=18).move_to(LEFT * 5.0 + UP * 0.7)
        gene_b = self.text_box("Gene B", width=2.0, color=BLUE_B, font_size=18).move_to(LEFT * 2.9 + UP * 0.7)
        reg = self.text_box("RegulationLink", width=3.0, color=PURPLE_B, font_size=18).move_to(LEFT * 3.95 + DOWN * 0.55)
        a_to_reg = Arrow(gene_a.get_bottom(), reg.get_top() + LEFT * 0.45, buff=0.08, color=PURPLE_B, stroke_width=3)
        b_to_reg = Arrow(gene_b.get_bottom(), reg.get_top() + RIGHT * 0.45, buff=0.08, color=PURPLE_B, stroke_width=3)

        eval_link = self.text_box("EvaluationLink\n(0.8, 0.9)", width=2.8, color=GREEN_B, font_size=16).move_to(RIGHT * 0.1 + UP * 1.45)
        inhib_link = self.text_box("InhibitionLink\nDrug X", width=2.8, color=ORANGE, font_size=16).move_to(RIGHT * 0.1 + DOWN * 0.25)
        context_link = self.text_box("ContextLink\nLiver Tissue", width=2.8, color=YELLOW_B, font_size=16).move_to(RIGHT * 3.0 + DOWN * 1.45)

        eval_to_reg = Arrow(eval_link.get_left(), reg.get_right(), buff=0.08, color=GREEN_B, stroke_width=3)
        inhib_to_reg = Arrow(inhib_link.get_left(), reg.get_right() + DOWN * 0.08, buff=0.08, color=ORANGE, stroke_width=3)
        context_to_inhib = Arrow(context_link.get_left(), inhib_link.get_right(), buff=0.08, color=YELLOW_B, stroke_width=3)

        self.play(FadeIn(tag), run_time=0.45)
        self.play(FadeIn(gene_a), FadeIn(gene_b), FadeIn(reg), GrowArrow(a_to_reg), GrowArrow(b_to_reg), run_time=0.9)
        self.play(FadeIn(eval_link), GrowArrow(eval_to_reg), run_time=0.55)
        self.play(FadeIn(inhib_link), GrowArrow(inhib_to_reg), run_time=0.55)
        self.play(FadeIn(context_link), GrowArrow(context_to_inhib), run_time=0.55)
        self.next_slide()


class Phase1MetagraphGeneExampleSlide(HyperonPhase1RefinedBase):
    def construct(self):
        tag = self.text_box("Gene example in metagraph form", width=6.6, color=PURPLE_B, font_size=29)
        tag.to_edge(UP, buff=0.35)

        panel = self.bullet_panel(
            "What metagraph unlocks",
            [
                "Edges and nodes are both Atoms",
                "Links can point to links directly",
                "Confidence, context, causality stay attached to the relation",
                "Supports deep composition in one unified memory fabric",
            ],
            width=10.8,
            title_color=PURPLE_B,
        )
        panel.move_to(UP * 0.2)

        atoms = VGroup(
            self.text_box("Node Atom", width=2.4, color=BLUE_B, font_size=17).move_to(LEFT * 4.0 + DOWN * 1.7),
            self.text_box("Link Atom", width=2.4, color=PURPLE_B, font_size=17).move_to(LEFT * 1.0 + DOWN * 1.7),
            self.text_box("Meta-Link Atom", width=2.8, color=GREEN_B, font_size=17).move_to(RIGHT * 2.4 + DOWN * 1.7),
        )
        l1 = Arrow(atoms[0].get_right(), atoms[1].get_left(), buff=0.08, color=WHITE, stroke_width=3)
        l2 = Arrow(atoms[1].get_right(), atoms[2].get_left(), buff=0.08, color=GREEN_B, stroke_width=3)

        self.play(FadeIn(tag), run_time=0.5)
        self.play(FadeIn(panel), run_time=0.9)
        self.play(FadeIn(atoms), GrowArrow(l1), GrowArrow(l2), run_time=0.8)
        self.next_slide()


class Phase1ContentAddressingSlide(HyperonPhase1RefinedBase):
    def construct(self):
        tag = self.text_box("Content-based addressing (detailed)", width=7.4, color=YELLOW_B, font_size=29)
        tag.to_edge(UP, buff=0.35)

        atom = self.text_box("Atom structure", width=2.8, color=BLUE_B, font_size=19).move_to(LEFT * 4.0 + UP * 0.7)
        hashf = self.text_box("SHA-256", width=2.4, color=TEAL_B, font_size=22).move_to(LEFT * 1.2 + UP * 0.7)
        cid = self.text_box("CID\n0x9c7b2f...", width=3.3, color=YELLOW_B, font_size=20).move_to(RIGHT * 2.2 + UP * 0.7)
        scanner = Rectangle(width=0.25, height=1.25, color=TEAL_B, fill_opacity=0.25).move_to(atom)
        self.play(FadeIn(tag), run_time=0.5)
        self.play(FadeIn(atom), FadeIn(hashf), FadeIn(cid), run_time=0.7)
        self.play(FadeIn(scanner), scanner.animate.shift(RIGHT * 0.9), run_time=0.55)
        self.play(FadeOut(scanner), run_time=0.2)
        self.play(GrowArrow(Arrow(atom.get_right(), hashf.get_left(), buff=0.08, color=WHITE, stroke_width=3)), GrowArrow(Arrow(hashf.get_right(), cid.get_left(), buff=0.08, color=WHITE, stroke_width=3)), run_time=0.7)
        pulse = Circle(radius=0.45, color=YELLOW_B, stroke_width=3).move_to(cid)
        self.play(Flash(hashf.get_center(), color=TEAL_B), Create(pulse), run_time=0.4)
        self.play(FadeOut(pulse), run_time=0.15)

        panel = self.bullet_panel(
            "Properties",
            [
                "Same structure => same CID",
                "Tiny content change => completely new CID",
                "Identity is content-derived, not location-derived",
            ],
            width=10.4,
            title_color=YELLOW_B,
        )
        panel.to_edge(DOWN, buff=0.35)
        self.play(FadeIn(panel), run_time=0.75)
        self.next_slide()


class Phase1MerkleTreeSlide(HyperonPhase1RefinedBase):
    def construct(self):
        tag = self.text_box("Merkle tree with gene hashes", width=6.8, color=GREEN_B, font_size=29)
        tag.to_edge(UP, buff=0.35)

        leaves = VGroup(
            self.text_box("h(GeneA)", width=2.0, color=GRAY_A, font_size=17, padding=0.16).move_to(LEFT * 4.6 + DOWN * 2.0),
            self.text_box("h(GeneB)", width=2.0, color=GRAY_A, font_size=17, padding=0.16).move_to(LEFT * 2.3 + DOWN * 2.0),
            self.text_box("h(RegLink)", width=2.0, color=GRAY_A, font_size=17, padding=0.16).move_to(ORIGIN + DOWN * 2.0),
            self.text_box("h(Context)", width=2.0, color=GRAY_A, font_size=17, padding=0.16).move_to(RIGHT * 2.3 + DOWN * 2.0),
        )
        p1 = self.text_box("h01", width=1.8, color=TEAL_B, font_size=17, padding=0.16).move_to(LEFT * 3.45 + DOWN * 0.85)
        p2 = self.text_box("h23", width=1.8, color=TEAL_B, font_size=17, padding=0.16).move_to(RIGHT * 1.15 + DOWN * 0.85)
        root = self.text_box("Merkle Root", width=2.6, color=YELLOW_B, font_size=19, padding=0.18).move_to(LEFT * 1.15 + UP * 0.6)

        lines = VGroup(
            Line(leaves[0].get_top(), p1.get_bottom() + LEFT * 0.28, color=TEAL_B, stroke_width=2.4),
            Line(leaves[1].get_top(), p1.get_bottom() + RIGHT * 0.28, color=TEAL_B, stroke_width=2.4),
            Line(leaves[2].get_top(), p2.get_bottom() + LEFT * 0.28, color=TEAL_B, stroke_width=2.4),
            Line(leaves[3].get_top(), p2.get_bottom() + RIGHT * 0.28, color=TEAL_B, stroke_width=2.4),
            Line(p1.get_top(), root.get_bottom() + LEFT * 0.3, color=YELLOW_B, stroke_width=2.6),
            Line(p2.get_top(), root.get_bottom() + RIGHT * 0.3, color=YELLOW_B, stroke_width=2.6),
        )

        self.play(FadeIn(tag), run_time=0.5)
        self.play(FadeIn(leaves, lag_ratio=0.1), run_time=0.85)
        self.play(Create(lines[:4]), FadeIn(VGroup(p1, p2)), run_time=0.8)
        self.play(Create(lines[4:]), FadeIn(root), run_time=0.75)
        self.next_slide()


class Phase1MerkleDagProgressiveSlide(HyperonPhase1RefinedBase):
    def construct(self):
        tag = self.text_box("Merkle-DAG: what is added", width=6.0, color=ORANGE, font_size=29)
        tag.to_edge(UP, buff=0.35)

        left_root = self.text_box("h_root_A", width=2.2, color=BLUE_B, font_size=17).move_to(LEFT * 3.0 + UP * 0.9)
        right_root = self.text_box("h_root_B", width=2.2, color=BLUE_B, font_size=17).move_to(RIGHT * 0.3 + UP * 0.9)
        left_mid = self.text_box("h_mid_A", width=2.2, color=TEAL_B, font_size=17).move_to(LEFT * 3.6 + DOWN * 0.2)
        right_mid = self.text_box("h_mid_B", width=2.2, color=TEAL_B, font_size=17).move_to(RIGHT * 0.9 + DOWN * 0.2)
        shared = self.text_box("h(shared_rule)", width=2.7, color=GREEN_B, font_size=16).move_to(LEFT * 1.35 + DOWN * 1.6)

        links = VGroup(
            Line(left_root.get_bottom(), left_mid.get_top(), color=GRAY_B, stroke_width=2.5),
            Line(right_root.get_bottom(), right_mid.get_top(), color=GRAY_B, stroke_width=2.5),
            Line(left_mid.get_bottom(), shared.get_top() + LEFT * 0.28, color=GREEN_B, stroke_width=3),
            Line(right_mid.get_bottom(), shared.get_top() + RIGHT * 0.28, color=GREEN_B, stroke_width=3),
        )

        explainer = self.bullet_panel(
            "Actual Merkle-DAG behavior",
            [
                "Shared child hash is referenced by multiple parents",
                "No duplicate copy of the same sub-structure",
                "Content-hash identity keeps integrity verifiable",
            ],
            width=6.9,
            title_color=GREEN_B,
        ).to_edge(RIGHT, buff=0.35).shift(DOWN * 0.25)

        self.play(FadeIn(tag), run_time=0.45)
        self.play(FadeIn(VGroup(left_root, right_root, left_mid, right_mid)), run_time=0.7)
        self.play(Create(links[:2]), run_time=0.5)
        self.play(FadeIn(shared), Create(links[2:]), Flash(shared.get_center(), color=GREEN_B), run_time=0.9)
        self.play(FadeIn(explainer, shift=LEFT * 0.08), run_time=0.8)
        self.next_slide()


class Phase1ImmutabilityVersioningSlide(HyperonPhase1RefinedBase):
    def construct(self):
        tag = self.text_box("Advantages of Merkle-DAG", width=6.1, color=YELLOW_B, font_size=29)
        tag.to_edge(UP, buff=0.35)

        cards = VGroup(
            self.bullet_panel("A. Deduplication", ["Same thought => same CID", "No duplicate atoms"], width=4.1, title_color=GREEN_B),
            self.bullet_panel("B. Lock-free writes", ["Writers create new nodes", "Readers continue safely"], width=4.1, title_color=BLUE_B),
            self.bullet_panel("C. Verifiable patches", ["Patch updates root hash", "State remains auditable"], width=4.1, title_color=ORANGE),
        ).arrange(RIGHT, buff=0.22).to_edge(UP, buff=1.9)

        stage = Rectangle(width=11.8, height=3.3, stroke_color=GRAY_C, stroke_width=1.8).to_edge(DOWN, buff=0.28)

        self.play(FadeIn(tag), run_time=0.45)
        self.play(FadeIn(cards, lag_ratio=0.1), run_time=0.9)
        self.play(Create(stage), run_time=0.4)
        self.next_slide()

        filter_box = RoundedRectangle(corner_radius=0.08, width=2.3, height=0.6, stroke_color=YELLOW_B).move_to(LEFT * 4.1 + DOWN * 0.1)
        sink = Circle(radius=0.35, color=YELLOW_B, fill_opacity=0.26).move_to(LEFT * 4.1 + DOWN * 1.25)
        sink_text = Text("CID", font_size=15, color=YELLOW_B).move_to(sink)
        falling = VGroup(*[Text("Atom", font_size=16, color=WHITE).move_to(LEFT * 4.1 + UP * (0.8 + i * 0.34)) for i in range(5)])
        self.play(FadeIn(filter_box), FadeIn(sink), FadeIn(sink_text), run_time=0.45)
        self.play(LaggedStart(*[f.animate.move_to(filter_box.get_center()).set_opacity(0.25) for f in falling], lag_ratio=0.1), run_time=0.9)
        self.play(FadeOut(falling), Flash(sink.get_center(), color=YELLOW_B), run_time=0.35)

        self.next_slide()

        parent = self.text_box("Parent", width=2.0, color=GRAY_A, font_size=18, padding=0.18).move_to(ORIGIN + UP * 0.8)
        node_a = self.text_box("Node A", width=2.0, color=BLUE_B, font_size=18, padding=0.18).move_to(LEFT * 0.8 + DOWN * 0.5)
        link_a = Arrow(parent.get_bottom(), node_a.get_top(), buff=0.08, color=GRAY_A, stroke_width=3)
        node_b = self.text_box("Node B", width=2.0, color=ORANGE, font_size=18, padding=0.18).move_to(RIGHT * 1.2 + DOWN * 1.2)
        link_b = Arrow(parent.get_bottom(), node_b.get_top(), buff=0.08, color=ORANGE, stroke_width=3)
        self.play(FadeIn(parent), FadeIn(node_a), GrowArrow(link_a), run_time=0.65)
        self.play(FadeIn(node_b, shift=DOWN * 0.1), run_time=0.45)
        self.play(Transform(link_a, link_b), run_time=0.55)

        self.next_slide()

        root = self.text_box("Merkle Root", width=2.5, color=GREEN_B, font_size=18, padding=0.18).move_to(RIGHT * 4.1 + UP * 0.55)
        patch = self.text_box("Patch Delta", width=2.5, color=ORANGE, font_size=18, padding=0.18).move_to(RIGHT * 4.1 + DOWN * 0.55)
        trace = self.text_box("CheckpointRef", width=2.8, color=TEAL_B, font_size=17, padding=0.18).move_to(RIGHT * 4.1 + DOWN * 1.55)
        p_to_r = Arrow(patch.get_top(), root.get_bottom(), buff=0.08, color=ORANGE, stroke_width=3)
        self.play(FadeIn(root), FadeIn(patch), GrowArrow(p_to_r), run_time=0.7)
        self.play(Flash(root.get_center(), color=GREEN_B), FadeIn(trace), run_time=0.6)

        self.next_slide()
