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
        title = Text("Mathematical & Representational Foundations", font_size=34, color=BLUE_B)
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

        left_root = self.text_box("h_root_A", width=2.2, color=BLUE_B, font_size=17).move_to(LEFT * 4.55 + UP * 0.9)
        right_root = self.text_box("h_root_B", width=2.2, color=BLUE_B, font_size=17).move_to(LEFT * 2.0 + UP * 0.9)
        left_mid = self.text_box("h_mid_A", width=2.2, color=TEAL_B, font_size=17).move_to(LEFT * 4.9 + DOWN * 0.2)
        right_mid = self.text_box("h_mid_B", width=2.2, color=TEAL_B, font_size=17).move_to(LEFT * 1.65 + DOWN * 0.2)
        shared = self.text_box("h(shared_rule)", width=2.7, color=GREEN_B, font_size=16).move_to(LEFT * 3.25 + DOWN * 1.55)

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
            width=4.55,
            title_color=GREEN_B,
        ).to_edge(RIGHT, buff=0.35).shift(DOWN * 0.12)

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


class Phase1TrieShapeSlide(HyperonPhase1RefinedBase):
    def _word_node(self, label: str, point, color=BLUE_B, radius: float = 0.28) -> VGroup:
        node = Circle(radius=radius, color=color, fill_color=BLACK, fill_opacity=0.55, stroke_width=2.6)
        node.move_to(point)
        text = Text(label, font_size=18, color=color).move_to(node)
        return VGroup(node, text)

    def construct(self):
        tag = self.text_box("Data structures for scale: The Trie", width=8.5, color=TEAL_B, font_size=29)
        tag.to_edge(UP, buff=0.35)
        subtitle = Text("Moving from flat lists to shared prefixes", font_size=22, color=GRAY_A)
        subtitle.next_to(tag, DOWN, buff=0.18)

        divider = Line(UP * 2.15, DOWN * 2.85, color=GRAY_D, stroke_width=1.8)

        old_title = Text("Flat list", font_size=24, color=RED_B).move_to(LEFT * 4.25 + UP * 1.9)
        rows = VGroup()
        row_labels = ["Apple", "Apply", "Application", "...", "Appreciate"]
        for i, label in enumerate(row_labels):
            row = RoundedRectangle(
                corner_radius=0.04,
                width=3.35,
                height=0.43,
                stroke_color=GRAY_B,
                stroke_width=1.5,
                fill_color=BLACK,
                fill_opacity=0.22,
            )
            text = Text(label, font_size=16, color=GRAY_A).move_to(row)
            row.move_to(LEFT * 4.25 + UP * (1.1 - i * 0.48))
            text.move_to(row)
            rows.add(VGroup(row, text))

        scan_arrow = Arrow(
            rows[0].get_right() + RIGHT * 0.1,
            rows[-1].get_right() + RIGHT * 0.1,
            buff=0.04,
            color=RED_B,
            stroke_width=4,
            max_tip_length_to_length_ratio=0.12,
        )
        slow_label = Text("Slow search", font_size=20, color=RED_B).next_to(scan_arrow, RIGHT, buff=0.12)

        new_title = Text("Prefix tree", font_size=24, color=GREEN_B).move_to(RIGHT * 3.35 + UP * 1.9)
        positions = {
            "root": RIGHT * 3.35 + UP * 1.18,
            "APPL": RIGHT * 3.35 + UP * 0.25,
            "E": RIGHT * 2.15 + DOWN * 0.78,
            "Y": RIGHT * 3.35 + DOWN * 0.78,
            "ICATION": RIGHT * 4.65 + DOWN * 0.78,
        }
        root = self._word_node("root", positions["root"], color=GRAY_A, radius=0.31)
        appl = self.text_box("APPL", width=1.35, color=YELLOW_B, font_size=18, padding=0.14).move_to(positions["APPL"])
        e = self._word_node("E", positions["E"], color=GREEN_B)
        y_node = self._word_node("Y", positions["Y"], color=GREEN_B)
        ication = self.text_box("ICATION", width=1.55, color=GREEN_B, font_size=14, padding=0.13).move_to(positions["ICATION"])
        tree_nodes = VGroup(root, appl, e, y_node, ication)

        tree_edges = VGroup(
            Line(root.get_bottom(), appl.get_top(), color=YELLOW_B, stroke_width=4),
            Line(appl.get_bottom(), e.get_top(), color=GREEN_B, stroke_width=3),
            Line(appl.get_bottom(), y_node.get_top(), color=GREEN_B, stroke_width=3),
            Line(appl.get_bottom(), ication.get_top(), color=GREEN_B, stroke_width=3),
        )
        shared = Text("shared prefix: APPL", font_size=18, color=YELLOW_B).next_to(appl, LEFT, buff=0.25)
        apple = Text("APPLE", font_size=16, color=GREEN_B).next_to(e, DOWN, buff=0.1)
        apply = Text("APPLY", font_size=16, color=GREEN_B).next_to(y_node, DOWN, buff=0.1)
        application = Text("APPLICATION", font_size=15, color=GREEN_B).next_to(ication, DOWN, buff=0.1)

        bullets = self.bullet_panel(
            "Trie memory principle",
            [
                "Stores data by shape, not by scan order",
                "Shared prefixes are stored exactly once",
                "Removes huge redundancy in repeated structures",
            ],
            width=11.8,
            title_color=TEAL_B,
        )
        bullets.to_edge(DOWN, buff=0.25)

        self.play(FadeIn(tag), FadeIn(subtitle, shift=UP * 0.08), run_time=0.55)
        self.play(Create(divider), FadeIn(old_title), FadeIn(new_title), run_time=0.45)
        self.play(FadeIn(rows, lag_ratio=0.08), run_time=0.85)
        self.play(GrowArrow(scan_arrow), FadeIn(slow_label, shift=RIGHT * 0.08), run_time=0.55)
        self.play(Create(tree_edges[:1]), FadeIn(VGroup(root, appl)), FadeIn(shared), run_time=0.9)
        self.play(Create(tree_edges[1:]), FadeIn(VGroup(e, y_node, ication, apple, apply, application)), run_time=0.75)
        self.play(FadeIn(bullets, shift=UP * 0.08), run_time=0.75)
        self.next_slide()


class Phase1HierarchicalIndexingSlide(HyperonPhase1RefinedBase):
    def _node(self, point, color=GRAY_C, radius: float = 0.08) -> Dot:
        return Dot(point, radius=radius, color=color)

    def construct(self):
        tag = self.text_box("Hierarchical indexing", width=4.9, color=GREEN_B, font_size=30)
        tag.to_edge(UP, buff=0.35)
        subtitle = Text("Lookup cost follows the path length, not total memory size", font_size=22, color=GRAY_A)
        subtitle.next_to(tag, DOWN, buff=0.18)

        root_p = np.array([0.0, 1.25, 0.0])
        level1 = [np.array([-4.6, 0.35, 0.0]), np.array([-1.55, 0.35, 0.0]), np.array([1.55, 0.35, 0.0]), np.array([4.6, 0.35, 0.0])]
        level2 = []
        for parent in level1:
            level2.extend([parent + LEFT * 0.62 + DOWN * 0.85, parent + RIGHT * 0.62 + DOWN * 0.85])
        level3 = []
        for parent in level2:
            level3.extend([parent + LEFT * 0.28 + DOWN * 0.75, parent + RIGHT * 0.28 + DOWN * 0.75])

        dim_edges = VGroup()
        for p in level1:
            dim_edges.add(Line(root_p, p, color=GRAY_D, stroke_width=1.8))
        for i, p in enumerate(level2):
            dim_edges.add(Line(level1[i // 2], p, color=GRAY_D, stroke_width=1.6))
        for i, p in enumerate(level3):
            dim_edges.add(Line(level2[i // 2], p, color=GRAY_D, stroke_width=1.4))

        dim_nodes = VGroup(self._node(root_p, color=GRAY_B, radius=0.11))
        for p in level1:
            dim_nodes.add(self._node(p, radius=0.09))
        for p in level2:
            dim_nodes.add(self._node(p, radius=0.075))
        for p in level3:
            dim_nodes.add(self._node(p, radius=0.06))

        path_points = [root_p, level1[2], level2[5], level3[11]]
        path_edges = VGroup(
            Line(path_points[0], path_points[1], color=YELLOW_B, stroke_width=5),
            Line(path_points[1], path_points[2], color=YELLOW_B, stroke_width=5),
            Line(path_points[2], path_points[3], color=YELLOW_B, stroke_width=5),
        )
        path_nodes = VGroup(*[self._node(p, color=YELLOW_B, radius=0.12) for p in path_points])
        spotlight = Circle(radius=0.42, color=YELLOW_B, stroke_width=3).move_to(path_points[-1])
        path_label = Text("only this branch is touched", font_size=20, color=YELLOW_B)
        path_label.next_to(path_edges[1], RIGHT, buff=0.26)

        flat = self.bullet_panel(
            "Traditional flat database",
            [
                "Search time grows with data size",
                "Scans irrelevant items",
                "Bottlenecks under AGI-scale memory",
            ],
            width=5.8,
            title_color=RED_B,
        ).to_edge(DOWN, buff=0.25).shift(LEFT * 3.0)
        trie = self.bullet_panel(
            "Hierarchical Trie",
            [
                "Search time follows key length",
                "Skips irrelevant branches immediately",
                "Keeps lookup behavior stable as memory grows",
            ],
            width=5.8,
            title_color=GREEN_B,
        ).to_edge(DOWN, buff=0.25).shift(RIGHT * 3.0)

        self.play(FadeIn(tag), FadeIn(subtitle, shift=UP * 0.08), run_time=0.55)
        self.play(Create(dim_edges, lag_ratio=0.02), FadeIn(dim_nodes, lag_ratio=0.02), run_time=1.0)
        self.play(dim_edges.animate.set_opacity(0.24), dim_nodes.animate.set_opacity(0.36), run_time=0.45)
        self.play(Create(path_edges), FadeIn(path_nodes), Create(spotlight), FadeIn(path_label, shift=RIGHT * 0.08), run_time=0.9)
        self.play(FadeIn(flat, shift=UP * 0.08), FadeIn(trie, shift=UP * 0.08), run_time=0.8)
        self.next_slide()


class Phase1PathBasedAddressingSlide(HyperonPhase1RefinedBase):
    def _small_node(self, label: str, point, color=BLUE_B) -> VGroup:
        node = RoundedRectangle(
            corner_radius=0.08,
            width=1.45,
            height=0.46,
            stroke_color=color,
            stroke_width=2,
            fill_color=BLACK,
            fill_opacity=0.3,
        ).move_to(point)
        text = Text(label, font_size=17, color=color).move_to(node)
        return VGroup(node, text)

    def construct(self):
        tag = self.text_box("Path-based addressing", width=5.4, color=YELLOW_B, font_size=30)
        tag.to_edge(UP, buff=0.35)
        subtitle = Text("The ID is the map", font_size=24, color=GRAY_A)
        subtitle.next_to(tag, DOWN, buff=0.18)

        left_title = Text("Path key", font_size=23, color=YELLOW_B).move_to(LEFT * 3.95 + UP * 1.65)
        hash_box = self.text_box("A5 - B2 - C9", width=3.8, color=YELLOW_B, font_size=23, padding=0.22)
        hash_box.move_to(LEFT * 3.95 + UP * 0.9)

        steps = VGroup(
            self.text_box("Turn left", width=2.1, color=BLUE_B, font_size=17, padding=0.18),
            self.text_box("Turn right", width=2.25, color=TEAL_B, font_size=17, padding=0.18),
            self.text_box("Turn left", width=2.1, color=GREEN_B, font_size=17, padding=0.18),
        ).arrange(DOWN, buff=0.18)
        steps.move_to(LEFT * 3.95 + DOWN * 0.48)
        path_arrow = Arrow(hash_box.get_bottom(), steps.get_top(), buff=0.12, color=YELLOW_B, stroke_width=3)

        right_title = Text("Structural locality", font_size=23, color=GREEN_B).move_to(RIGHT * 3.2 + UP * 1.65)
        root = self._small_node("animal", RIGHT * 3.2 + UP * 1.0, color=GRAY_A)
        branch = self._small_node("canine", RIGHT * 3.2 + UP * 0.22, color=GREEN_B)
        dog = self._small_node("Dog", RIGHT * 1.9 + DOWN * 0.65, color=GREEN_B)
        wolf = self._small_node("Wolf", RIGHT * 3.2 + DOWN * 0.65, color=GREEN_B)
        fox = self._small_node("Fox", RIGHT * 4.5 + DOWN * 0.65, color=GREEN_B)
        local_edges = VGroup(
            Line(root.get_bottom(), branch.get_top(), color=GREEN_B, stroke_width=3),
            Line(branch.get_bottom(), dog.get_top(), color=GREEN_B, stroke_width=3),
            Line(branch.get_bottom(), wolf.get_top(), color=GREEN_B, stroke_width=3),
            Line(branch.get_bottom(), fox.get_top(), color=GREEN_B, stroke_width=3),
        )
        cluster_ring = RoundedRectangle(
            corner_radius=0.18,
            width=4.35,
            height=1.7,
            stroke_color=GREEN_B,
            stroke_width=2.4,
            fill_color=GREEN_E,
            fill_opacity=0.1,
        ).move_to(RIGHT * 3.2 + DOWN * 0.25)
        cache_label = Text("nearby in memory / cache", font_size=18, color=GREEN_B).next_to(cluster_ring, DOWN, buff=0.12)

        bullets = self.bullet_panel(
            "Why this matters",
            [
                "Efficient lookup: key bytes act like turn-by-turn directions",
                "Locality-aware keys can place related concepts on nearby branches",
                "Clustered data is friendlier to CPU cache and parallel traversal",
            ],
            width=11.8,
            title_color=YELLOW_B,
        )
        bullets.to_edge(DOWN, buff=0.24)

        self.play(FadeIn(tag), FadeIn(subtitle, shift=UP * 0.08), run_time=0.55)
        self.play(FadeIn(left_title), FadeIn(hash_box), run_time=0.6)
        self.play(GrowArrow(path_arrow), FadeIn(steps, lag_ratio=0.12), run_time=0.85)
        self.play(FadeIn(right_title), FadeIn(root), FadeIn(branch), Create(local_edges[0]), run_time=0.65)
        self.play(FadeIn(VGroup(dog, wolf, fox)), Create(local_edges[1:]), FadeIn(cluster_ring), run_time=0.9)
        self.play(FadeIn(cache_label), FadeIn(bullets, shift=UP * 0.08), run_time=0.75)
        self.next_slide()


class Phase1QuantaleBase(HyperonPhase1RefinedBase):
    formula_font = "DejaVu Sans"

    def formula_text(self, text: str, font_size: int = 25, color=WHITE, width: float | None = None) -> Text:
        label = Text(text, font_size=font_size, color=color, font=self.formula_font, line_spacing=1.08)
        if width is not None:
            self._fit(label, width)
        return label

    def formula_box(
        self,
        text: str,
        width: float,
        color=WHITE,
        font_size: int = 24,
        padding: float = 0.18,
        fill_opacity: float = 0.2,
    ) -> VGroup:
        label = self.formula_text(text, font_size=font_size, color=color, width=width - 2 * padding)
        box = RoundedRectangle(
            corner_radius=0.08,
            width=width,
            height=label.height + 2 * padding,
            stroke_color=color,
            stroke_width=2,
            fill_color=BLACK,
            fill_opacity=fill_opacity,
        )
        label.move_to(box)
        return VGroup(box, label)

    def concept_node(self, label: str, point, width: float = 2.05, color=BLUE_B, font_size: int = 15) -> VGroup:
        node = RoundedRectangle(
            corner_radius=0.08,
            width=width,
            height=0.48,
            stroke_color=color,
            stroke_width=2,
            fill_color=BLACK,
            fill_opacity=0.32,
        ).move_to(point)
        text = Text(label, font_size=font_size, color=color, line_spacing=1.0)
        self._fit(text, width - 0.22, min_size=10)
        text.move_to(node)
        return VGroup(node, text)

    def arrow_between(self, start: VGroup, end: VGroup, color=GRAY_B, width: float = 2.4) -> Arrow:
        return Arrow(
            start.get_top(),
            end.get_bottom(),
            buff=0.08,
            color=color,
            stroke_width=width,
            max_tip_length_to_length_ratio=0.11,
        )

    def build_vehicle_mammal_hasse(self, center=ORIGIN, scale: float = 1.0, highlight: bool = False) -> VGroup:
        nodes = {
            "vehicle": self.concept_node("Vehicle", [-1.25, 1.25, 0], width=1.65, color=GREEN_B),
            "mammal": self.concept_node("Mammal", [1.25, 1.25, 0], width=1.65, color=GREEN_B),
            "car": self.concept_node("Car", [-1.25, 0.34, 0], width=1.35, color=TEAL_B),
            "dog": self.concept_node("Dog", [0.72, 0.34, 0], width=1.35, color=TEAL_B),
            "sedan": self.concept_node("Sedan", [-1.25, -0.58, 0], width=1.45, color=BLUE_B),
            "retriever": self.concept_node("Retriever", [1.25, -0.58, 0], width=1.7, color=BLUE_B),
            "black_sedan": self.concept_node("Black sedan\nplate X", [-1.25, -1.62, 0], width=2.0, color=YELLOW_B, font_size=13),
            "golden": self.concept_node("Golden retriever\nborn 2022", [1.25, -1.62, 0], width=2.2, color=YELLOW_B, font_size=13),
        }
        edges = VGroup(
            self.arrow_between(nodes["black_sedan"], nodes["sedan"]),
            self.arrow_between(nodes["sedan"], nodes["car"]),
            self.arrow_between(nodes["car"], nodes["vehicle"]),
            self.arrow_between(nodes["golden"], nodes["retriever"]),
            self.arrow_between(nodes["retriever"], nodes["dog"]),
            self.arrow_between(nodes["dog"], nodes["mammal"]),
        )
        group = VGroup(edges, *nodes.values())
        if highlight:
            path = VGroup(
                self.arrow_between(nodes["black_sedan"], nodes["sedan"], color=YELLOW_B, width=4.3),
                self.arrow_between(nodes["sedan"], nodes["car"], color=YELLOW_B, width=4.3),
                self.arrow_between(nodes["car"], nodes["vehicle"], color=YELLOW_B, width=4.3),
            )
            group.add(path)
        group.scale(scale).move_to(center)
        return group


class Phase1LatticeHierarchySlide(Phase1QuantaleBase):
    def construct(self):
        tag = self.text_box("Lattices: Organizing Concepts in a Hierarchy", width=9.3, color=GREEN_B, font_size=29)
        tag.to_edge(UP, buff=0.32)
        subtitle = Text("The geometry of specificity vs. generality", font_size=21, color=GRAY_A)
        subtitle.next_to(tag, DOWN, buff=0.14)

        hasse = self.build_vehicle_mammal_hasse(center=LEFT * 3.15 + DOWN * 0.1, scale=0.92, highlight=True)
        top_label = self.text_box("Weak / General / Simple", width=3.5, color=GREEN_B, font_size=16, padding=0.16)
        top_label.move_to(LEFT * 3.15 + UP * 2.1)
        bottom_label = self.text_box("Strong / Specific / Complex", width=3.8, color=YELLOW_B, font_size=16, padding=0.16)
        bottom_label.move_to(LEFT * 3.15 + DOWN * 2.65)

        relation = self.bullet_panel(
            "Partial order relation (≤)",
            [
                "Ranks concepts by specificity and complexity",
                "a ≤ b means: a is stronger / more specific than b",
            ],
            width=6.3,
            title_color=YELLOW_B,
        ).to_edge(RIGHT, buff=0.35).shift(UP * 0.85)

        ax_title = Text("Partial order axioms", font_size=20, color=BLUE_B)
        ax_title.move_to(RIGHT * 3.1 + DOWN * 0.55)
        axioms = VGroup(
            Text("Reflexivity:     a <= a", font_size=18, color=BLUE_B, font="Noto Sans Mono", disable_ligatures=True),
            Text("Antisymmetry:   a <= b, b <= a  ->  a = b", font_size=15, color=TEAL_B, font="Noto Sans Mono", disable_ligatures=True),
            Text("Transitivity:   a <= b, b <= c  ->  a <= c", font_size=15, color=GREEN_B, font="Noto Sans Mono", disable_ligatures=True),
        ).arrange(DOWN, aligned_edge=LEFT, buff=0.22)
        for line in axioms:
            self._fit(line, 5.8)
        axioms.move_to(RIGHT * 3.1 + DOWN * 1.55)

        self.play(FadeIn(tag), FadeIn(subtitle, shift=UP * 0.08), run_time=0.55)
        self.play(FadeIn(VGroup(top_label, bottom_label)), FadeIn(hasse, lag_ratio=0.03), run_time=1.0)
        self.play(FadeIn(relation, shift=LEFT * 0.08), run_time=0.75)
        self.play(FadeIn(ax_title), FadeIn(axioms, lag_ratio=0.08), run_time=0.85)
        self.next_slide()


class Phase1LatticeOperationsSlide(Phase1QuantaleBase):
    def _join_diagram(self) -> VGroup:
        mammal = self.concept_node("Mammal", UP * 0.8, width=1.65, color=YELLOW_B)
        dog = self.concept_node("Dog", LEFT * 0.85 + DOWN * 0.42, width=1.25, color=BLUE_B)
        cat = self.concept_node("Cat", RIGHT * 0.85 + DOWN * 0.42, width=1.25, color=BLUE_B)
        animal = self.concept_node("Animal", UP * 1.55, width=1.5, color=GRAY_B)
        edges = VGroup(
            Arrow(dog.get_top(), mammal.get_bottom() + LEFT * 0.28, buff=0.07, color=YELLOW_B, stroke_width=3.4),
            Arrow(cat.get_top(), mammal.get_bottom() + RIGHT * 0.28, buff=0.07, color=YELLOW_B, stroke_width=3.4),
            Line(mammal.get_top(), animal.get_bottom(), color=GRAY_C, stroke_width=2),
        )
        label = self.formula_box("Dog ⊕ Cat = Mammal", width=3.25, color=YELLOW_B, font_size=18)
        label.next_to(VGroup(dog, cat), DOWN, buff=0.18)
        return VGroup(edges, animal, mammal, dog, cat, label)

    def _meet_diagram(self) -> VGroup:
        object_node = self.concept_node("Thing", UP * 1.55, width=1.35, color=GRAY_B)
        wheels = self.concept_node("Has wheels", LEFT * 0.95 + UP * 0.48, width=1.8, color=TEAL_B, font_size=14)
        human = self.concept_node("Human powered", RIGHT * 0.95 + UP * 0.48, width=2.1, color=TEAL_B, font_size=14)
        bicycle = self.concept_node("Bicycle", DOWN * 0.58, width=1.55, color=YELLOW_B)
        edges = VGroup(
            Line(object_node.get_bottom(), wheels.get_top(), color=GRAY_C, stroke_width=2),
            Line(object_node.get_bottom(), human.get_top(), color=GRAY_C, stroke_width=2),
            Arrow(wheels.get_bottom(), bicycle.get_top() + LEFT * 0.24, buff=0.07, color=YELLOW_B, stroke_width=3.4),
            Arrow(human.get_bottom(), bicycle.get_top() + RIGHT * 0.24, buff=0.07, color=YELLOW_B, stroke_width=3.4),
        )
        label = self.formula_box("Wheels ∧ Human powered = Bicycle", width=3.85, color=YELLOW_B, font_size=15)
        label.next_to(bicycle, DOWN, buff=0.18)
        return VGroup(edges, object_node, wheels, human, bicycle, label)

    def construct(self):
        tag = self.text_box("Lattices: Navigating the Hierarchy", width=7.4, color=TEAL_B, font_size=30)
        tag.to_edge(UP, buff=0.32)
        subtitle = Text("Mathematical operations combine concepts logically", font_size=21, color=GRAY_A)
        subtitle.next_to(tag, DOWN, buff=0.14)

        left_title = Text("Join: generalize upward", font_size=22, color=YELLOW_B).move_to(LEFT * 3.3 + UP * 1.85)
        right_title = Text("Meet: specialize downward", font_size=22, color=YELLOW_B).move_to(RIGHT * 3.25 + UP * 1.85)
        join = self._join_diagram().scale(0.82).move_to(LEFT * 3.25 + UP * 0.32)
        meet = self._meet_diagram().scale(0.82).move_to(RIGHT * 3.25 + UP * 0.32)
        divider = Line(UP * 1.95, DOWN * 2.35, color=GRAY_D, stroke_width=1.7)

        left = self.bullet_panel(
            "Join (⊕ or ∨) - logical OR",
            [
                "Finds the Least Upper Bound",
                "Moves up to GENERALIZE",
                "Dog ⊕ Cat = Mammal",
            ],
            width=5.75,
            title_color=BLUE_B,
        ).to_edge(DOWN, buff=0.22).shift(LEFT * 3.0)
        right = self.bullet_panel(
            "Meet (∧) - logical AND",
            [
                "Finds the Greatest Lower Bound",
                "Moves down to SPECIALIZE",
                "Wheels ∧ Human powered = Bicycle",
            ],
            width=5.75,
            title_color=GREEN_B,
        ).to_edge(DOWN, buff=0.22).shift(RIGHT * 3.0)

        self.play(FadeIn(tag), FadeIn(subtitle, shift=UP * 0.08), run_time=0.55)
        self.play(Create(divider), FadeIn(left_title), FadeIn(right_title), run_time=0.45)
        self.play(FadeIn(join, lag_ratio=0.04), FadeIn(meet, lag_ratio=0.04), run_time=1.0)
        self.play(FadeIn(left, shift=UP * 0.08), FadeIn(right, shift=UP * 0.08), run_time=0.8)
        self.next_slide()


class Phase1QuantaleActionSlide(Phase1QuantaleBase):
    def _mini_lattice(self) -> VGroup:
        top = self.concept_node("general", UP * 0.85, width=1.55, color=GREEN_B, font_size=14)
        mid_l = self.concept_node("case A", LEFT * 0.75, width=1.35, color=TEAL_B, font_size=13)
        mid_r = self.concept_node("case B", RIGHT * 0.75, width=1.35, color=TEAL_B, font_size=13)
        bottom = self.concept_node("specific", DOWN * 0.9, width=1.65, color=YELLOW_B, font_size=14)
        lines = VGroup(
            Line(bottom.get_top(), mid_l.get_bottom(), color=GRAY_B, stroke_width=2),
            Line(bottom.get_top(), mid_r.get_bottom(), color=GRAY_B, stroke_width=2),
            Line(mid_l.get_top(), top.get_bottom(), color=GRAY_B, stroke_width=2),
            Line(mid_r.get_top(), top.get_bottom(), color=GRAY_B, stroke_width=2),
        )
        title = Text("Complete Lattice", font_size=19, color=GREEN_B).next_to(top, UP, buff=0.25)
        return VGroup(lines, top, mid_l, mid_r, bottom, title)

    def _sequence_panel(self, labels: list[str], result: str, color, y: float) -> VGroup:
        a = self.formula_box(labels[0], width=1.15, color=color, font_size=20, padding=0.15)
        b = self.formula_box(labels[1], width=1.15, color=color, font_size=20, padding=0.15)
        out = self.text_box(result, width=1.7, color=color, font_size=17, padding=0.16)
        row = VGroup(
            a,
            Arrow(ORIGIN, RIGHT * 0.6, color=color, stroke_width=3, max_tip_length_to_length_ratio=0.18),
            b,
            Arrow(ORIGIN, RIGHT * 0.6, color=color, stroke_width=3, max_tip_length_to_length_ratio=0.18),
            out,
        ).arrange(RIGHT, buff=0.15)
        row.move_to(RIGHT * 3.1 + UP * y)
        formula = self.formula_text(f"{labels[0]} ⊗ {labels[1]}", font_size=18, color=color).next_to(row, DOWN, buff=0.08)
        return VGroup(row, formula)

    def construct(self):
        tag = self.text_box("Quantales: Adding Action to the Lattice", width=8.2, color=ORANGE, font_size=30)
        tag.to_edge(UP, buff=0.32)
        subtitle = Text("Upgrading a static hierarchy into an active reasoning engine", font_size=21, color=GRAY_A)
        subtitle.next_to(tag, DOWN, buff=0.14)

        lattice = self._mini_lattice().scale(0.98).move_to(LEFT * 4.2 + UP * 0.35)
        plus = self.formula_box("+ sequence\nmultiplication ⊗", width=2.45, color=ORANGE, font_size=18, padding=0.2)
        plus.move_to(LEFT * 0.85 + UP * 0.35)
        upgrade_arrow = Arrow(lattice.get_right(), plus.get_left(), buff=0.15, color=ORANGE, stroke_width=4)
        action_arrow = Arrow(plus.get_right(), RIGHT * 1.1 + UP * 0.35, buff=0.1, color=ORANGE, stroke_width=4)

        q_title = Text("Quantale", font_size=24, color=ORANGE).move_to(RIGHT * 3.1 + UP * 1.8)
        success = self._sequence_panel(["a", "b"], "success", GREEN_B, 0.75)
        failure = self._sequence_panel(["b", "a"], "halt", RED_B, -0.55)

        foundation = self.formula_box("Q = Complete Lattice + Multiplication (⊗)", width=5.45, color=YELLOW_B, font_size=18)
        foundation.to_edge(DOWN, buff=0.32).shift(LEFT * 3.25)
        law = self.formula_box("Distributive law\na ⊗ (b ⊕ c) = (a ⊗ b) ⊕ (a ⊗ c)", width=6.0, color=GREEN_B, font_size=17)
        law.to_edge(DOWN, buff=0.32).shift(RIGHT * 3.0)

        self.play(FadeIn(tag), FadeIn(subtitle, shift=UP * 0.08), run_time=0.55)
        self.play(FadeIn(lattice, lag_ratio=0.05), run_time=0.8)
        self.play(GrowArrow(upgrade_arrow), FadeIn(plus), GrowArrow(action_arrow), run_time=0.8)
        self.play(FadeIn(q_title), FadeIn(success, shift=RIGHT * 0.08), FadeIn(failure, shift=RIGHT * 0.08), run_time=0.85)
        self.play(FadeIn(foundation), FadeIn(law), run_time=0.85)
        self.next_slide()


class Phase1QuantalePowersSlide(Phase1QuantaleBase):
    def _sequence_power(self) -> VGroup:
        good = VGroup(
            self.formula_box("a", 0.75, GREEN_B, 18, 0.12),
            Arrow(ORIGIN, RIGHT * 0.4, color=GREEN_B, stroke_width=2.6, max_tip_length_to_length_ratio=0.2),
            self.formula_box("b", 0.75, GREEN_B, 18, 0.12),
            Arrow(ORIGIN, RIGHT * 0.4, color=GREEN_B, stroke_width=2.6, max_tip_length_to_length_ratio=0.2),
            self.text_box("success", 1.25, GREEN_B, 14, 0.12),
        ).arrange(RIGHT, buff=0.1)
        bad = VGroup(
            self.formula_box("b", 0.75, RED_B, 18, 0.12),
            Arrow(ORIGIN, RIGHT * 0.4, color=RED_B, stroke_width=2.6, max_tip_length_to_length_ratio=0.2),
            self.formula_box("a", 0.75, RED_B, 18, 0.12),
            Arrow(ORIGIN, RIGHT * 0.4, color=RED_B, stroke_width=2.6, max_tip_length_to_length_ratio=0.2),
            self.text_box("crash", 1.15, RED_B, 14, 0.12),
        ).arrange(RIGHT, buff=0.1)
        bad.next_to(good, DOWN, buff=0.22)
        title = Text("Composition", font_size=21, color=GREEN_B).next_to(good, UP, buff=0.22)
        note = self.formula_text("a ⊗ b ≠ b ⊗ a", font_size=18, color=YELLOW_B).next_to(bad, DOWN, buff=0.14)
        return VGroup(title, good, bad, note)

    def _uncertainty_power(self) -> VGroup:
        title = Text("Uncertainty", font_size=21, color=BLUE_B)
        s1 = Text("strength", font_size=14, color=GRAY_A)
        c1 = Text("confidence", font_size=14, color=GRAY_A)
        bars = VGroup()
        specs = [(2.0, GREEN_B), (1.45, BLUE_B), (1.65, GREEN_B), (1.05, BLUE_B)]
        labels = [s1, c1, Text("strength", font_size=14, color=GRAY_A), Text("confidence", font_size=14, color=GRAY_A)]
        for i, (w, color) in enumerate(specs):
            track = Rectangle(width=2.2, height=0.16, stroke_color=GRAY_C, stroke_width=1.2)
            fill = Rectangle(width=w, height=0.16, stroke_color=color, fill_color=color, fill_opacity=0.7, stroke_width=0)
            fill.align_to(track, LEFT)
            row = VGroup(labels[i], VGroup(track, fill)).arrange(RIGHT, buff=0.12)
            bars.add(row)
        bars.arrange(DOWN, aligned_edge=LEFT, buff=0.16)
        merge = self.formula_box("TV₁ ⊗ TV₂", width=2.4, color=YELLOW_B, font_size=18, padding=0.14)
        merge.next_to(bars, DOWN, buff=0.2)
        title.next_to(bars, UP, buff=0.2)
        return VGroup(title, bars, merge)

    def _residual_power(self) -> VGroup:
        simple = self.text_box("simple model a", width=2.5, color=GREEN_B, font_size=16, padding=0.16)
        complex_m = self.text_box("complex model b", width=2.7, color=RED_B, font_size=16, padding=0.16)
        missing = self.text_box("missing c", width=1.8, color=YELLOW_B, font_size=15, padding=0.14)
        simple.move_to(LEFT * 2.4)
        complex_m.move_to(RIGHT * 2.2)
        missing.move_to(ORIGIN + DOWN * 0.7)
        arrows = VGroup(
            Arrow(complex_m.get_left(), missing.get_right(), buff=0.12, color=YELLOW_B, stroke_width=3),
            Arrow(missing.get_left(), simple.get_right(), buff=0.12, color=YELLOW_B, stroke_width=3),
        )
        penalty = Text("Weakness penalty", font_size=18, color=YELLOW_B).next_to(missing, DOWN, buff=0.16)
        title = Text("Reasoning and simplicity prior", font_size=22, color=YELLOW_B).next_to(VGroup(simple, complex_m), UP, buff=0.28)
        return VGroup(title, arrows, simple, complex_m, missing, penalty)

    def construct(self):
        tag = self.text_box("The Essential Powers of the Quantale", width=7.5, color=YELLOW_B, font_size=30)
        tag.to_edge(UP, buff=0.3)
        subtitle = Text("How AGI weighs, examines, and evaluates thoughts", font_size=21, color=GRAY_A)
        subtitle.next_to(tag, DOWN, buff=0.12)

        comp = self._sequence_power().scale(0.9).move_to(LEFT * 3.45 + UP * 0.95)
        uncert = self._uncertainty_power().scale(0.9).move_to(RIGHT * 3.45 + UP * 0.95)
        residual = self._residual_power().scale(0.88).move_to(UP * -0.75)

        residual_formula = self.formula_box("a ⊘ b = ⋁ { c ∈ Q | b ⊗ c ≤ a }", width=6.4, color=ORANGE, font_size=22)
        residual_formula.to_edge(DOWN, buff=0.55)
        residual_note = self.text_box("Residual: missing step + complexity penalty", width=5.7, color=GRAY_A, font_size=16, padding=0.13)
        residual_note.next_to(residual_formula, UP, buff=0.12)

        self.play(FadeIn(tag), FadeIn(subtitle, shift=UP * 0.08), run_time=0.55)
        self.play(FadeIn(comp, shift=UP * 0.08), FadeIn(uncert, shift=UP * 0.08), run_time=0.9)
        self.play(FadeIn(residual, shift=UP * 0.08), run_time=0.8)
        self.play(FadeIn(residual_note, shift=UP * 0.06), FadeIn(residual_formula), run_time=0.8)
        self.next_slide()


class Phase1PLNBase(HyperonPhase1RefinedBase):
    def formula_box(
        self,
        text: str,
        width: float,
        color=WHITE,
        font_size: int = 22,
        padding: float = 0.18,
        fill_opacity: float = 0.2,
    ) -> VGroup:
        label = Text(text, font_size=font_size, color=color, font="Noto Sans Mono", disable_ligatures=True, line_spacing=1.05)
        self._fit(label, width - 2 * padding, min_size=10)
        box = RoundedRectangle(
            corner_radius=0.08,
            width=width,
            height=label.height + 2 * padding,
            stroke_color=color,
            stroke_width=2,
            fill_color=BLACK,
            fill_opacity=fill_opacity,
        )
        label.move_to(box)
        return VGroup(box, label)

    def tiny_label_box(self, text: str, point, width: float, color=WHITE, font_size: int = 14) -> VGroup:
        box = RoundedRectangle(
            corner_radius=0.06,
            width=width,
            height=0.42,
            stroke_color=color,
            stroke_width=1.7,
            fill_color=BLACK,
            fill_opacity=0.32,
        ).move_to(point)
        label = Text(text, font_size=font_size, color=color)
        self._fit(label, width - 0.2, min_size=9)
        label.move_to(box)
        return VGroup(box, label)


class Phase1ProbabilityVsLogicSlide(Phase1PLNBase):
    def construct(self):
        tag = self.text_box("Probability vs. Logic", width=5.1, color=YELLOW_B, font_size=31)
        tag.to_edge(UP, buff=0.32)
        subtitle = Text("Why AGI abandons absolute certainty", font_size=21, color=GRAY_A)
        subtitle.next_to(tag, DOWN, buff=0.14)

        divider = Line(UP * 1.8, DOWN * 2.75, color=GRAY_D, stroke_width=1.6)
        left_title = Text("Classical Logic", font_size=22, color=RED_B).move_to(LEFT * 3.35 + UP * 1.65)
        right_title = Text("Probabilistic Logic", font_size=22, color=GREEN_B).move_to(RIGHT * 3.25 + UP * 1.65)

        start = self.tiny_label_box("Fact", LEFT * 4.15 + UP * 0.82, 1.3, BLUE_B)
        test = self.tiny_label_box("Rule", LEFT * 3.2 + UP * 0.05, 1.3, YELLOW_B)
        true_box = self.tiny_label_box("True / 1", LEFT * 4.15 + DOWN * 0.8, 1.55, GREEN_B)
        false_box = self.tiny_label_box("False / 0", LEFT * 2.2 + DOWN * 0.8, 1.55, RED_B)
        rigid_edges = VGroup(
            Arrow(start.get_bottom(), test.get_top(), buff=0.05, color=WHITE, stroke_width=3),
            Arrow(test.get_bottom(), true_box.get_top(), buff=0.05, color=GREEN_B, stroke_width=3),
            Arrow(test.get_bottom(), false_box.get_top(), buff=0.05, color=RED_B, stroke_width=3),
        )
        exception = self.tiny_label_box("exception", LEFT * 1.55 + UP * 0.15, 1.65, ORANGE, font_size=13)
        exception_arrow = Arrow(exception.get_right(), test.get_left(), buff=0.08, color=ORANGE, stroke_width=3)
        red_x = VGroup(
            Line(LEFT * 3.75 + DOWN * 0.25, LEFT * 2.65 + DOWN * 1.35, color=RED_B, stroke_width=7),
            Line(LEFT * 2.65 + DOWN * 0.25, LEFT * 3.75 + DOWN * 1.35, color=RED_B, stroke_width=7),
        )

        points = [
            RIGHT * 2.05 + UP * 0.9,
            RIGHT * 3.35 + UP * 1.05,
            RIGHT * 4.45 + UP * 0.4,
            RIGHT * 2.45 + DOWN * 0.45,
            RIGHT * 3.65 + DOWN * 0.55,
            RIGHT * 4.75 + DOWN * 1.15,
            RIGHT * 2.95 + DOWN * 1.35,
        ]
        edges = VGroup()
        edge_specs = [(0, 1, 4.5), (1, 2, 2.0), (0, 3, 2.8), (3, 4, 5.6), (4, 2, 1.8), (4, 5, 4.2), (3, 6, 2.2), (6, 5, 3.4)]
        for i, j, width in edge_specs:
            edges.add(Line(points[i], points[j], color=GREEN_B, stroke_width=width, stroke_opacity=0.62))
        nodes = VGroup()
        for idx, p in enumerate(points):
            color = [GREEN_B, BLUE_B, YELLOW_B, TEAL_B, GREEN_B, ORANGE, BLUE_B][idx]
            nodes.add(Dot(p, radius=0.09, color=color))
        flow = VGroup(*[edge.copy().set_stroke(color=YELLOW_B, width=edge.stroke_width + 2.5, opacity=0.75) for edge in edges[:4]])

        left_panel = self.bullet_panel(
            "Boolean fails",
            [
                "Only True or False",
                "Contradictions break it",
            ],
            width=3.85,
            title_color=RED_B,
        ).to_edge(DOWN, buff=0.25).shift(LEFT * 4.25)
        middle_panel = self.bullet_panel(
            "Probability fails",
            [
                "Long chains dilute math",
                "Deep reasoning stalls",
            ],
            width=3.85,
            title_color=ORANGE,
        ).to_edge(DOWN, buff=0.25)
        right_panel = self.bullet_panel(
            "PLN solution",
            [
                "Keeps logical steps",
                "Tracks confidence bounds",
            ],
            width=3.85,
            title_color=GREEN_B,
        ).to_edge(DOWN, buff=0.25).shift(RIGHT * 4.25)

        self.play(FadeIn(tag), FadeIn(subtitle, shift=UP * 0.08), run_time=0.55)
        self.play(Create(divider), FadeIn(left_title), FadeIn(right_title), run_time=0.45)
        self.play(FadeIn(VGroup(start, test, true_box, false_box)), Create(rigid_edges), run_time=0.8)
        self.play(FadeIn(exception), GrowArrow(exception_arrow), run_time=0.5)
        self.play(FadeIn(red_x, scale=0.8), Flash(test.get_center(), color=RED_B), run_time=0.45)
        self.play(Create(edges, lag_ratio=0.05), FadeIn(nodes, lag_ratio=0.08), run_time=0.9)
        self.play(LaggedStart(*[ShowPassingFlash(f, time_width=0.45) for f in flow], lag_ratio=0.15), run_time=1.1)
        self.play(
            FadeIn(left_panel, shift=UP * 0.08),
            FadeIn(middle_panel, shift=UP * 0.08),
            FadeIn(right_panel, shift=UP * 0.08),
            run_time=0.8,
        )
        self.next_slide()


class Phase1SimpleTruthValueSlide(Phase1PLNBase):
    def construct(self):
        tag = self.text_box("The Simple Truth Value (STV)", width=6.4, color=BLUE_B, font_size=31)
        tag.to_edge(UP, buff=0.32)
        subtitle = Text("Escaping the ambiguity of single-number probabilities", font_size=21, color=GRAY_A)
        subtitle.next_to(tag, DOWN, buff=0.14)

        origin = LEFT * 3.55 + DOWN * 1.65
        x_axis = Arrow(origin, origin + RIGHT * 4.2, buff=0, color=GRAY_A, stroke_width=3, max_tip_length_to_length_ratio=0.04)
        y_axis = Arrow(origin, origin + UP * 3.25, buff=0, color=GRAY_A, stroke_width=3, max_tip_length_to_length_ratio=0.05)
        x_label = Text("Strength (s)", font_size=17, color=GRAY_A).next_to(x_axis, DOWN, buff=0.18)
        y_label = Text("Confidence (c)", font_size=17, color=GRAY_A).rotate(PI / 2).next_to(y_axis, LEFT, buff=0.18)
        ticks = VGroup()
        for i in range(6):
            x = origin + RIGHT * (i * 0.8)
            ticks.add(Line(x + DOWN * 0.06, x + UP * 0.06, color=GRAY_B, stroke_width=1.2))
        for i in range(5):
            y = origin + UP * (i * 0.75)
            ticks.add(Line(y + LEFT * 0.06, y + RIGHT * 0.06, color=GRAY_B, stroke_width=1.2))
        mid_v = DashedLine(origin + RIGHT * 2.0, origin + RIGHT * 2.0 + UP * 3.0, dash_length=0.08, color=GRAY_D)
        mid_h = DashedLine(origin + UP * 1.5, origin + RIGHT * 4.0 + UP * 1.5, dash_length=0.08, color=GRAY_D)

        quadrants = VGroup(
            Text("Looks False\nNeeds Data", font_size=14, color=ORANGE, line_spacing=0.9).move_to(origin + RIGHT * 1.0 + UP * 0.72),
            Text("Looks True\nNeeds Data", font_size=14, color=YELLOW_B, line_spacing=0.9).move_to(origin + RIGHT * 3.05 + UP * 0.72),
            Text("Proven False", font_size=15, color=RED_B).move_to(origin + RIGHT * 1.0 + UP * 2.25),
            Text("Proven True", font_size=15, color=GREEN_B).move_to(origin + RIGHT * 3.05 + UP * 2.25),
        )
        examples = VGroup(
            Dot(origin + RIGHT * 3.25 + UP * 2.42, radius=0.08, color=GREEN_B),
            Dot(origin + RIGHT * 0.7 + UP * 2.35, radius=0.08, color=RED_B),
            Dot(origin + RIGHT * 3.3 + UP * 0.78, radius=0.08, color=YELLOW_B),
            Dot(origin + RIGHT * 0.85 + UP * 0.68, radius=0.08, color=ORANGE),
        )

        problem = self.bullet_panel(
            "Why P(x)=0.5 is ambiguous",
            [
                "Could mean massive conflicting evidence",
                "Could mean no evidence at all",
                "One number cannot separate randomness from ignorance",
            ],
            width=5.95,
            title_color=RED_B,
        ).to_edge(RIGHT, buff=0.25).shift(UP * 0.82)
        solution = self.bullet_panel(
            "PLN truth vector: (s, c)",
            [
                "Strength s = how often it was true",
                "Confidence c = how much evidence supports s",
            ],
            width=5.95,
            title_color=BLUE_B,
        ).to_edge(RIGHT, buff=0.25).shift(DOWN * 1.4)
        vector = self.formula_box("(s, c)", width=2.0, color=YELLOW_B, font_size=27).move_to(RIGHT * 3.1 + DOWN * 0.08)

        self.play(FadeIn(tag), FadeIn(subtitle, shift=UP * 0.08), run_time=0.55)
        self.play(GrowArrow(x_axis), GrowArrow(y_axis), FadeIn(VGroup(x_label, y_label, ticks)), run_time=0.8)
        self.play(Create(mid_v), Create(mid_h), FadeIn(quadrants, lag_ratio=0.08), run_time=0.8)
        self.play(FadeIn(examples, lag_ratio=0.12), Flash(examples[0].get_center(), color=GREEN_B), run_time=0.7)
        self.play(FadeIn(problem, shift=LEFT * 0.08), run_time=0.75)
        self.play(FadeIn(vector, scale=1.05), FadeIn(solution, shift=LEFT * 0.08), run_time=0.85)
        self.next_slide()


class Phase1PLNTruthMathSlide(Phase1PLNBase):
    def construct(self):
        tag = self.text_box("The Mathematics of PLN Truth Values", width=8.0, color=GREEN_B, font_size=30)
        tag.to_edge(UP, buff=0.32)
        subtitle = Text("Calculating belief from raw observation", font_size=21, color=GRAY_A)
        subtitle.next_to(tag, DOWN, buff=0.14)

        dots = VGroup()
        for i in range(24):
            row = i // 8
            col = i % 8
            point = LEFT * 4.8 + UP * (0.95 - row * 0.34) + RIGHT * (col * 0.28)
            color = GREEN_B if i in {0, 1, 2, 4, 5, 8, 9, 11, 13, 16, 18, 20, 22, 23} else GRAY_B
            dots.add(Dot(point, radius=0.045, color=color))
        raw_reference = dots.copy().set_opacity(0.22)
        raw_label = Text("Raw\nevidence", font_size=18, color=GRAY_A, line_spacing=0.82).next_to(raw_reference, LEFT, buff=0.26)

        strength_engine = self.text_box("Strength\nEngine", width=2.2, color=GREEN_B, font_size=19, padding=0.22)
        confidence_engine = self.text_box("Confidence\nEngine", width=2.4, color=BLUE_B, font_size=19, padding=0.22)
        strength_engine.move_to(LEFT * 0.65 + UP * 0.72)
        confidence_engine.move_to(LEFT * 0.65 + DOWN * 0.72)
        funnel_s = Polygon(LEFT * 3.15 + UP * 1.25, LEFT * 2.0 + UP * 1.0, strength_engine.get_left() + LEFT * 0.05, strength_engine.get_left() + DOWN * 0.2, color=GREEN_B)
        funnel_s.set_fill(GREEN_E, opacity=0.12).set_stroke(GREEN_B, width=2)
        funnel_c = Polygon(LEFT * 3.15 + DOWN * 1.05, LEFT * 2.0 + DOWN * 0.9, confidence_engine.get_left() + LEFT * 0.05, confidence_engine.get_left() + UP * 0.2, color=BLUE_B)
        funnel_c.set_fill(BLUE_E, opacity=0.12).set_stroke(BLUE_B, width=2)

        s_formula = self.formula_box("s = n+ / n", width=2.65, color=GREEN_B, font_size=22)
        c_formula = self.formula_box("c = n / (n + k)", width=3.1, color=BLUE_B, font_size=20)
        s_formula.move_to(RIGHT * 2.2 + UP * 0.82)
        c_formula.move_to(RIGHT * 2.2 + DOWN * 0.72)
        output = self.formula_box("(s, c)", width=2.1, color=YELLOW_B, font_size=26).move_to(RIGHT * 4.75)
        out_arrows = VGroup(
            Arrow(strength_engine.get_right(), s_formula.get_left(), buff=0.1, color=GREEN_B, stroke_width=3),
            Arrow(confidence_engine.get_right(), c_formula.get_left(), buff=0.1, color=BLUE_B, stroke_width=3),
            Arrow(s_formula.get_right(), output.get_left() + UP * 0.12, buff=0.1, color=YELLOW_B, stroke_width=3),
            Arrow(c_formula.get_right(), output.get_left() + DOWN * 0.12, buff=0.1, color=YELLOW_B, stroke_width=3),
        )

        definitions = self.bullet_panel(
            "Variables",
            [
                "n+ = positive observations",
                "n = total observations",
                "k = lookahead / conservatism parameter",
            ],
            width=11.2,
            title_color=YELLOW_B,
        ).to_edge(DOWN, buff=0.28)

        self.play(FadeIn(tag), FadeIn(subtitle, shift=UP * 0.08), run_time=0.55)
        self.play(FadeIn(raw_label), FadeIn(raw_reference, lag_ratio=0.025), FadeIn(dots, lag_ratio=0.025), run_time=0.8)
        self.play(Create(funnel_s), Create(funnel_c), FadeIn(strength_engine), FadeIn(confidence_engine), run_time=0.75)
        self.play(
            LaggedStart(*[dot.animate.move_to(strength_engine.get_center()).set_opacity(0.35) for dot in dots[:12]], lag_ratio=0.025),
            run_time=0.75,
        )
        self.play(FadeIn(s_formula), GrowArrow(out_arrows[0]), run_time=0.55)
        self.play(
            LaggedStart(*[dot.animate.move_to(confidence_engine.get_center()).set_opacity(0.35) for dot in dots[12:]], lag_ratio=0.025),
            run_time=0.75,
        )
        self.play(FadeIn(c_formula), GrowArrow(out_arrows[1]), run_time=0.55)
        self.play(FadeIn(output, scale=1.05), GrowArrow(out_arrows[2]), GrowArrow(out_arrows[3]), FadeIn(definitions, shift=UP * 0.08), run_time=0.85)
        self.next_slide()


class Phase1ExpectedTruthDecisionSlide(Phase1PLNBase):
    def construct(self):
        tag = self.text_box("Decision Making Under Uncertainty", width=7.5, color=YELLOW_B, font_size=30)
        tag.to_edge(UP, buff=0.32)
        subtitle = Text("Calculating the Expected Truth Value E", font_size=21, color=GRAY_A)
        subtitle.next_to(tag, DOWN, buff=0.14)

        prior = self.text_box("Prior\ns0", width=2.2, color=BLUE_B, font_size=21, padding=0.24)
        learned = self.text_box("Observed\nstrength s", width=2.8, color=GREEN_B, font_size=19, padding=0.24)
        prior.move_to(LEFT * 4.45 + UP * 0.65)
        learned.move_to(RIGHT * 4.25 + UP * 0.65)
        bucket = self.text_box("Decision\nE", width=2.4, color=YELLOW_B, font_size=21, padding=0.24).move_to(DOWN * 1.85)

        slider_track = Line(LEFT * 1.9 + UP * 0.82, RIGHT * 1.9 + UP * 0.82, color=GRAY_A, stroke_width=5)
        slider_knob = Circle(radius=0.16, color=YELLOW_B, fill_color=YELLOW_B, fill_opacity=0.7).move_to(LEFT * 0.75 + UP * 0.82)
        slider_label = Text("confidence c", font_size=19, color=YELLOW_B).next_to(slider_track, UP, buff=0.2)
        low = Text("0", font_size=15, color=GRAY_A).next_to(slider_track.get_start(), DOWN, buff=0.1)
        high = Text("1", font_size=15, color=GRAY_A).next_to(slider_track.get_end(), DOWN, buff=0.1)

        prior_flow = CubicBezier(prior.get_bottom(), LEFT * 4.3 + DOWN * 0.4, LEFT * 1.1 + DOWN * 0.65, bucket.get_left(), color=BLUE_B)
        learned_flow = CubicBezier(learned.get_bottom(), RIGHT * 4.1 + DOWN * 0.35, RIGHT * 1.05 + DOWN * 0.62, bucket.get_right(), color=GREEN_B)
        prior_flow.set_stroke(width=7, opacity=0.55)
        learned_flow.set_stroke(width=3, opacity=0.42)

        formula = self.formula_box("E = c*s + (1-c)*s0", width=5.5, color=YELLOW_B, font_size=22).move_to(DOWN * 0.42)
        high_conf = self.text_box("High c: trust observed data", width=4.2, color=GREEN_B, font_size=18, padding=0.18).to_edge(DOWN, buff=0.45).shift(LEFT * 3.0)
        low_conf = self.text_box("Low c: fall back to prior", width=4.0, color=BLUE_B, font_size=18, padding=0.18).to_edge(DOWN, buff=0.45).shift(RIGHT * 3.0)

        self.play(FadeIn(tag), FadeIn(subtitle, shift=UP * 0.08), run_time=0.55)
        self.play(FadeIn(prior), FadeIn(learned), FadeIn(bucket), run_time=0.75)
        self.play(Create(slider_track), FadeIn(VGroup(slider_knob, slider_label, low, high)), run_time=0.65)
        self.play(Create(prior_flow), Create(learned_flow), FadeIn(formula), run_time=0.85)
        self.play(
            slider_knob.animate.move_to(RIGHT * 1.45 + UP * 0.82),
            learned_flow.animate.set_stroke(width=8, opacity=0.68),
            prior_flow.animate.set_stroke(width=2.5, opacity=0.28),
            FadeIn(high_conf, shift=UP * 0.08),
            run_time=0.85,
        )
        self.play(
            slider_knob.animate.move_to(LEFT * 1.45 + UP * 0.82),
            prior_flow.animate.set_stroke(width=8, opacity=0.65),
            learned_flow.animate.set_stroke(width=2.5, opacity=0.26),
            FadeIn(low_conf, shift=UP * 0.08),
            run_time=0.85,
        )
        self.next_slide()


class Phase1LearningBase(Phase1PLNBase):
    def causal_node(self, label: str, point, color=WHITE, radius: float = 0.35, font_size: int = 20) -> VGroup:
        circle = Circle(radius=radius, stroke_color=color, stroke_width=2.2, fill_color=BLACK, fill_opacity=0.35)
        circle.move_to(point)
        text = Text(label, font_size=font_size, color=color, line_spacing=0.9)
        self._fit(text, radius * 1.62, min_size=10)
        text.move_to(circle)
        return VGroup(circle, text)

    def mini_card(
        self,
        title: str,
        body: list[str],
        width: float,
        color=WHITE,
        title_size: int = 20,
        body_size: int = 16,
    ) -> VGroup:
        title_t = Text(title, font_size=title_size, color=color)
        self._fit(title_t, width - 0.45, min_size=11)
        lines = VGroup()
        for line in body:
            t = Text(line, font_size=body_size, color=GRAY_A, line_spacing=0.92)
            self._fit(t, width - 0.45, min_size=9)
            lines.add(t)
        lines.arrange(DOWN, aligned_edge=LEFT, buff=0.08)
        content = VGroup(title_t, lines).arrange(DOWN, aligned_edge=LEFT, buff=0.16)
        panel = RoundedRectangle(
            corner_radius=0.09,
            width=width,
            height=content.height + 0.36,
            stroke_color=color,
            stroke_width=1.7,
            fill_color=BLACK,
            fill_opacity=0.24,
        )
        content.move_to(panel).shift(LEFT * 0.03)
        return VGroup(panel, content)

    def small_plot(self, origin, width: float, height: float, title: str, color=WHITE) -> VGroup:
        x_axis = Arrow(origin, origin + RIGHT * width, buff=0, color=GRAY_B, stroke_width=2.4, max_tip_length_to_length_ratio=0.05)
        y_axis = Arrow(origin, origin + UP * height, buff=0, color=GRAY_B, stroke_width=2.4, max_tip_length_to_length_ratio=0.06)
        title_t = Text(title, font_size=16, color=color)
        self._fit(title_t, width + 0.3, min_size=10)
        title_t.next_to(VGroup(x_axis, y_axis), UP, buff=0.14)
        y_label = Text("Recovery", font_size=12, color=GRAY_A).rotate(PI / 2).next_to(y_axis, LEFT, buff=0.1)
        x_label = Text("Treatment", font_size=12, color=GRAY_A).next_to(x_axis, DOWN, buff=0.1)
        return VGroup(x_axis, y_axis, title_t, y_label, x_label)


class Phase1ActiveInferenceLoopSlide(Phase1LearningBase):
    def construct(self):
        tag = self.text_box("Learning Paradigms: Active Inference", width=7.6, color=BLUE_B, font_size=30)
        tag.to_edge(UP, buff=0.32)
        subtitle = Text("Biological learning with top-down predictions", font_size=20, color=GRAY_A)
        subtitle.next_to(tag, DOWN, buff=0.14)

        high = self.text_box("High-level\nbeliefs mu", width=2.5, color=BLUE_B, font_size=20, padding=0.2).move_to(LEFT * 4.0 + UP * 0.95)
        model = self.text_box("Generative\nmodel", width=2.45, color=TEAL_B, font_size=20, padding=0.2).move_to(LEFT * 4.0 + DOWN * 0.15)
        sensory = self.text_box("Sensory\nlayer", width=2.45, color=GREEN_B, font_size=20, padding=0.2).move_to(LEFT * 4.0 + DOWN * 1.25)
        subtract = Circle(radius=0.28, color=YELLOW_B, fill_color=BLACK, fill_opacity=0.35).move_to(LEFT * 1.95 + DOWN * 1.25)
        minus = Text("-", font_size=28, color=YELLOW_B, font="Noto Sans Mono").move_to(subtract)
        sensor_in = Arrow(LEFT * 1.0 + DOWN * 2.15, subtract.get_bottom(), buff=0.06, color=GREEN_B, stroke_width=4)
        sensor_label = Text("Sensory data x", font_size=16, color=GREEN_B).next_to(sensor_in, DOWN, buff=0.08)
        down_1 = Arrow(high.get_bottom(), model.get_top(), buff=0.08, color=BLUE_B, stroke_width=4)
        down_2 = Arrow(model.get_bottom(), sensory.get_top(), buff=0.08, color=BLUE_B, stroke_width=4)
        pred_label = Text("Predictions\nf(mu)", font_size=14, color=BLUE_B, line_spacing=0.84).move_to(LEFT * 5.45 + UP * 0.1)
        compare_arrow = Arrow(sensory.get_right(), subtract.get_left(), buff=0.08, color=YELLOW_B, stroke_width=4)
        error_path = VGroup(
            Arrow(subtract.get_top(), LEFT * 1.95 + UP * 0.4, buff=0.04, color=ORANGE, stroke_width=4),
            Arrow(LEFT * 1.95 + UP * 0.4, high.get_right(), buff=0.08, color=ORANGE, stroke_width=4),
        )
        error_label = Text("Prediction error e", font_size=16, color=ORANGE).next_to(error_path, RIGHT, buff=0.12)

        passive = self.mini_card(
            "Traditional AI: passive",
            ["data in -> conclusion out", "Every example travels upward"],
            width=5.2,
            color=RED_B,
            title_size=21,
        )
        active = self.mini_card(
            "AGI learning: active",
            ["belief predicts sensor input", "Only error moves upward"],
            width=5.2,
            color=GREEN_B,
            title_size=21,
        )
        VGroup(passive, active).arrange(DOWN, buff=0.22).move_to(RIGHT * 3.1 + UP * 0.32)

        loop_steps = VGroup(
            self.text_box("1 Predict", width=1.85, color=BLUE_B, font_size=18, padding=0.14),
            self.text_box("2 Compare", width=1.95, color=YELLOW_B, font_size=18, padding=0.14),
            self.text_box("3 Update", width=1.85, color=ORANGE, font_size=18, padding=0.14),
        ).arrange(RIGHT, buff=0.18).move_to(RIGHT * 3.1 + DOWN * 1.75)
        step_arrows = VGroup(
            Arrow(loop_steps[0].get_right(), loop_steps[1].get_left(), buff=0.06, color=GRAY_B, stroke_width=2.8),
            Arrow(loop_steps[1].get_right(), loop_steps[2].get_left(), buff=0.06, color=GRAY_B, stroke_width=2.8),
        )

        self.play(FadeIn(tag), FadeIn(subtitle, shift=UP * 0.08), run_time=0.55)
        self.play(FadeIn(VGroup(high, model, sensory)), Create(VGroup(down_1, down_2)), FadeIn(pred_label), run_time=0.8)
        self.play(FadeIn(VGroup(subtract, minus)), GrowArrow(compare_arrow), GrowArrow(sensor_in), FadeIn(sensor_label), run_time=0.75)
        self.play(Create(error_path), FadeIn(error_label), Flash(subtract.get_center(), color=YELLOW_B), run_time=0.85)
        self.play(FadeIn(passive, shift=LEFT * 0.08), FadeIn(active, shift=LEFT * 0.08), run_time=0.75)
        self.play(FadeIn(loop_steps, lag_ratio=0.12), Create(step_arrows), run_time=0.7)
        self.next_slide()


class Phase1PredictiveCodingMathSlide(Phase1LearningBase):
    def construct(self):
        tag = self.text_box("The Mathematics of Predictive Coding", width=7.3, color=YELLOW_B, font_size=30)
        tag.to_edge(UP, buff=0.32)
        subtitle = Text("Minimizing surprise, also called free energy", font_size=21, color=GRAY_A)
        subtitle.next_to(tag, DOWN, buff=0.14)

        error_node = Circle(radius=0.42, color=YELLOW_B, fill_color=BLACK, fill_opacity=0.34).move_to(LEFT * 3.8 + UP * 0.3)
        error_text = Text("-", font_size=36, color=YELLOW_B).move_to(error_node)
        sensory = self.formula_box("x", width=1.0, color=GREEN_B, font_size=25).move_to(LEFT * 5.55 + UP * 0.3)
        prediction = self.formula_box("f(mu)", width=1.7, color=BLUE_B, font_size=23).move_to(LEFT * 3.8 + UP * 1.55)
        error_out = self.formula_box("e", width=1.0, color=ORANGE, font_size=25).move_to(LEFT * 2.2 + UP * 0.3)
        in_arrows = VGroup(
            Arrow(sensory.get_right(), error_node.get_left(), buff=0.08, color=GREEN_B, stroke_width=4),
            Arrow(prediction.get_bottom(), error_node.get_top(), buff=0.08, color=BLUE_B, stroke_width=4),
            Arrow(error_node.get_right(), error_out.get_left(), buff=0.08, color=ORANGE, stroke_width=4),
        )
        variables = self.mini_card(
            "Variables",
            ["x = sensory data", "mu = belief state", "f(mu) = predicted data"],
            width=4.3,
            color=GRAY_B,
            title_size=20,
            body_size=16,
        ).move_to(LEFT * 4.0 + DOWN * 1.45)

        origin = RIGHT * 1.35 + DOWN * 2.15
        x_axis = Arrow(origin, origin + RIGHT * 4.2, buff=0, color=GRAY_B, stroke_width=2.6, max_tip_length_to_length_ratio=0.04)
        y_axis = Arrow(origin, origin + UP * 2.05, buff=0, color=GRAY_B, stroke_width=2.6, max_tip_length_to_length_ratio=0.06)
        curve_points = []
        for i in range(22):
            x = i / 21
            y = (1.0 - x) ** 2 * 1.45 + 0.25
            curve_points.append(origin + RIGHT * (x * 3.75 + 0.18) + UP * y)
        curve = VMobject(color=ORANGE, stroke_width=4)
        curve.set_points_smoothly(curve_points)
        desc = Arrow(curve_points[5], curve_points[15], buff=0.02, color=YELLOW_B, stroke_width=4)
        graph_label = Text("Surprise e^2", font_size=16, color=ORANGE).rotate(PI / 2).next_to(y_axis, LEFT, buff=0.12).shift(UP * 0.35)
        time_label = Text("time t", font_size=16, color=GRAY_A).next_to(x_axis, DOWN, buff=0.12)
        gd_label = Text("gradient descent", font_size=16, color=YELLOW_B).next_to(desc, UP, buff=0.08)

        error_formula = self.formula_box("e = x - f(mu)", width=3.2, color=ORANGE, font_size=23).move_to(RIGHT * 3.35 + UP * 1.55)
        learn_formula = self.formula_box("dmu/dt ∝ - ∂(e^2)/∂mu", width=4.65, color=YELLOW_B, font_size=20).move_to(RIGHT * 3.35 + UP * 0.72)
        note = self.text_box("Learning updates only where prediction failed.", width=5.4, color=GRAY_A, font_size=16, padding=0.15).to_edge(DOWN, buff=0.25).shift(RIGHT * 2.75)

        self.play(FadeIn(tag), FadeIn(subtitle, shift=UP * 0.08), run_time=0.55)
        self.play(FadeIn(VGroup(sensory, prediction, error_node, error_text, error_out)), Create(in_arrows), run_time=0.85)
        self.play(FadeIn(variables, shift=UP * 0.08), run_time=0.55)
        self.play(FadeIn(error_formula), FadeIn(learn_formula, shift=UP * 0.06), run_time=0.75)
        self.play(Create(VGroup(x_axis, y_axis)), FadeIn(VGroup(graph_label, time_label)), Create(curve), run_time=0.8)
        self.play(GrowArrow(desc), FadeIn(gd_label), FadeIn(note, shift=UP * 0.08), run_time=0.8)
        self.next_slide()


class Phase1CausalCodingSimpsonSlide(Phase1LearningBase):
    def construct(self):
        tag = self.text_box("Causal Coding: Breaking Correlations", width=7.4, color=RED_B, font_size=30)
        tag.to_edge(UP, buff=0.32)
        subtitle = Text("Simpson's Paradox shows why pattern matching is not enough", font_size=20, color=GRAY_A)
        subtitle.next_to(tag, DOWN, buff=0.14)

        agg_origin = LEFT * 5.55 + UP * 0.45
        agg_plot = self.small_plot(agg_origin, 2.7, 1.35, "Aggregated view", color=YELLOW_B)
        agg_line = Line(agg_origin + RIGHT * 0.45 + UP * 0.35, agg_origin + RIGHT * 2.25 + UP * 1.05, color=YELLOW_B, stroke_width=4)
        agg_dots = VGroup(
            Dot(agg_origin + RIGHT * 0.55 + UP * 0.42, radius=0.055, color=YELLOW_B),
            Dot(agg_origin + RIGHT * 0.9 + UP * 0.50, radius=0.055, color=YELLOW_B),
            Dot(agg_origin + RIGHT * 1.95 + UP * 0.92, radius=0.055, color=YELLOW_B),
            Dot(agg_origin + RIGHT * 2.25 + UP * 1.10, radius=0.055, color=YELLOW_B),
        )
        agg_label = self.text_box("Drug helps?", width=1.85, color=YELLOW_B, font_size=15, padding=0.12)
        agg_label.next_to(agg_plot, RIGHT, buff=0.25).shift(DOWN * 0.05)

        strat_origin = LEFT * 5.55 + DOWN * 1.95
        strat_plot = self.small_plot(strat_origin, 2.7, 1.35, "Stratified by Z", color=BLUE_B)
        men_line = Line(strat_origin + RIGHT * 0.45 + UP * 1.05, strat_origin + RIGHT * 2.25 + UP * 0.78, color=BLUE_B, stroke_width=4)
        women_line = Line(strat_origin + RIGHT * 0.45 + UP * 0.58, strat_origin + RIGHT * 2.25 + UP * 0.30, color=GREEN_B, stroke_width=4)
        men_label = Text("Men", font_size=13, color=BLUE_B).next_to(men_line, UP, buff=0.04)
        women_label = Text("Women", font_size=13, color=GREEN_B).next_to(women_line, DOWN, buff=0.04)
        strat_label = self.text_box("Drug hurts\ninside each group", width=2.3, color=RED_B, font_size=14, padding=0.12).next_to(strat_plot, DOWN, buff=0.12)

        z = self.causal_node("Z\nGender", RIGHT * 3.95 + UP * 1.1, BLUE_B, radius=0.38, font_size=15)
        x = self.causal_node("X\nTreatment", RIGHT * 2.75 + DOWN * 0.45, YELLOW_B, radius=0.38, font_size=13)
        y = self.causal_node("Y\nRecovery", RIGHT * 5.1 + DOWN * 0.45, GREEN_B, radius=0.38, font_size=13)
        z_to_x = Arrow(z.get_bottom(), x.get_top(), buff=0.08, color=BLUE_B, stroke_width=4)
        z_to_y = Arrow(z.get_bottom(), y.get_top(), buff=0.08, color=BLUE_B, stroke_width=4)
        x_to_y = Arrow(x.get_right(), y.get_left(), buff=0.08, color=YELLOW_B, stroke_width=4)
        backdoor = VGroup(z_to_x.copy().set_color(RED_B).set_stroke(width=7, opacity=0.45), z_to_y.copy().set_color(RED_B).set_stroke(width=7, opacity=0.45))
        dag_title = Text("The hidden confounder", font_size=18, color=RED_B).next_to(z, UP, buff=0.2)
        dag_note = self.mini_card(
            "Hyperon stores causes, not just correlations",
            ["A -> B means A physically changes B", "The DAG tells PLN which paths are valid"],
            width=3.8,
            color=GREEN_B,
            title_size=18,
            body_size=14,
        ).move_to(RIGHT * 3.95 + DOWN * 2.12)

        self.play(FadeIn(tag), FadeIn(subtitle, shift=UP * 0.08), run_time=0.55)
        self.play(Create(agg_plot), Create(agg_line), FadeIn(agg_dots), FadeIn(agg_label), run_time=0.8)
        self.play(Create(strat_plot), Create(VGroup(men_line, women_line)), FadeIn(VGroup(men_label, women_label, strat_label)), run_time=0.9)
        self.play(FadeIn(VGroup(z, x, y, dag_title)), GrowArrow(z_to_x), GrowArrow(z_to_y), GrowArrow(x_to_y), run_time=0.85)
        self.play(FadeIn(backdoor), Flash(z.get_center(), color=RED_B), FadeIn(dag_note, shift=LEFT * 0.08), run_time=0.85)
        self.next_slide()


class Phase1DoCalculusSurgerySlide(Phase1LearningBase):
    def construct(self):
        tag = self.text_box("Causal Coding: The do-Calculus", width=6.7, color=YELLOW_B, font_size=30)
        tag.to_edge(UP, buff=0.32)
        subtitle = Text("Mathematically simulating physical interventions", font_size=21, color=GRAY_A)
        subtitle.next_to(tag, DOWN, buff=0.14)

        left_title = Text("Observe: P(Y | X)", font_size=21, color=RED_B).move_to(LEFT * 3.7 + UP * 1.55)
        right_title = Text("Intervene: P(Y | do(X))", font_size=21, color=GREEN_B).move_to(RIGHT * 3.25 + UP * 1.55)
        divider = Line(UP * 1.75, DOWN * 1.8, color=GRAY_D, stroke_width=1.6)

        z_l = self.causal_node("Z", LEFT * 3.7 + UP * 0.85, BLUE_B)
        x_l = self.causal_node("X", LEFT * 4.7 + DOWN * 0.55, YELLOW_B)
        y_l = self.causal_node("Y", LEFT * 2.75 + DOWN * 0.55, GREEN_B)
        lx = Arrow(z_l.get_bottom(), x_l.get_top(), buff=0.08, color=RED_B, stroke_width=5)
        ly = Arrow(z_l.get_bottom(), y_l.get_top(), buff=0.08, color=RED_B, stroke_width=5)
        xy_l = Arrow(x_l.get_right(), y_l.get_left(), buff=0.08, color=YELLOW_B, stroke_width=4)
        backdoor_label = Text("backdoor path", font_size=15, color=RED_B).next_to(VGroup(lx, ly), DOWN, buff=0.05)

        z_r = self.causal_node("Z", RIGHT * 3.25 + UP * 0.85, BLUE_B)
        x_r = self.causal_node("X", RIGHT * 2.25 + DOWN * 0.55, YELLOW_B)
        y_r = self.causal_node("Y", RIGHT * 4.2 + DOWN * 0.55, GREEN_B)
        cut_arrow = DashedLine(z_r.get_bottom(), x_r.get_top(), dash_length=0.08, color=GRAY_D, stroke_width=3)
        ry = Arrow(z_r.get_bottom(), y_r.get_top(), buff=0.08, color=BLUE_B, stroke_width=4)
        xy_r = Arrow(x_r.get_right(), y_r.get_left(), buff=0.08, color=YELLOW_B, stroke_width=4)
        cut_x = VGroup(
            Line(cut_arrow.get_center() + LEFT * 0.2 + UP * 0.2, cut_arrow.get_center() + RIGHT * 0.2 + DOWN * 0.2, color=RED_B, stroke_width=6),
            Line(cut_arrow.get_center() + LEFT * 0.2 + DOWN * 0.2, cut_arrow.get_center() + RIGHT * 0.2 + UP * 0.2, color=RED_B, stroke_width=6),
        )
        do_label = self.text_box("do(X)", width=1.45, color=YELLOW_B, font_size=17, padding=0.12).next_to(x_r, DOWN, buff=0.18)
        surgery_note = Text("incoming arrows to X are deleted", font_size=15, color=GREEN_B).next_to(cut_x, RIGHT, buff=0.12)

        observe_card = self.mini_card(
            "Observation",
            ["X happens naturally", "Z may explain both X and Y"],
            width=4.0,
            color=RED_B,
            title_size=18,
            body_size=14,
        ).move_to(LEFT * 3.65 + DOWN * 1.9)
        intervene_card = self.mini_card(
            "Intervention",
            ["The AGI forces X", "Confounding backdoors are severed"],
            width=4.05,
            color=GREEN_B,
            title_size=18,
            body_size=14,
        ).move_to(RIGHT * 3.4 + DOWN * 1.9)

        rules = VGroup(
            self.mini_card("Rule 1", ["ignore irrelevant W", "P(Y|do(X),Z,W)=P(Y|do(X),Z)"], 3.9, BLUE_B, 15, 11),
            self.mini_card("Rule 2", ["swap action with observation", "P(Y|do(X),Z)=P(Y|X,Z)"], 3.9, YELLOW_B, 15, 11),
            self.mini_card("Rule 3", ["delete irrelevant action", "P(Y|do(X))=P(Y)"], 3.9, GREEN_B, 15, 11),
        ).arrange(RIGHT, buff=0.2).to_edge(DOWN, buff=0.18)
        graph_group = VGroup(left_title, right_title, divider, z_l, x_l, y_l, lx, ly, xy_l, z_r, x_r, y_r, cut_arrow, ry, xy_r, cut_x, do_label, backdoor_label, surgery_note)
        graph_group.shift(UP * 0.32)

        self.play(FadeIn(tag), FadeIn(subtitle, shift=UP * 0.08), run_time=0.55)
        self.play(Create(divider), FadeIn(VGroup(left_title, right_title)), run_time=0.45)
        self.play(FadeIn(VGroup(z_l, x_l, y_l)), GrowArrow(lx), GrowArrow(ly), GrowArrow(xy_l), FadeIn(backdoor_label), run_time=0.85)
        self.play(FadeIn(VGroup(z_r, x_r, y_r)), Create(cut_arrow), GrowArrow(ry), GrowArrow(xy_r), FadeIn(do_label), run_time=0.85)
        self.play(FadeIn(cut_x, scale=0.8), FadeIn(surgery_note), FadeIn(observe_card), FadeIn(intervene_card), run_time=0.75)
        self.play(FadeIn(rules, shift=UP * 0.08), run_time=0.75)
        self.next_slide()


class Phase1BackdoorAdjustmentSlide(Phase1LearningBase):
    def construct(self):
        tag = self.text_box("Calculating do(X) from Passive Data", width=7.4, color=GREEN_B, font_size=30)
        tag.to_edge(UP, buff=0.32)
        subtitle = Text("Backdoor adjustment: eliminating confounders mathematically", font_size=20, color=GRAY_A)
        subtitle.next_to(tag, DOWN, buff=0.14)

        z = self.causal_node("Z\nGender", LEFT * 4.65 + UP * 1.0, BLUE_B, radius=0.35, font_size=14)
        x = self.causal_node("X\nTreatment", LEFT * 5.35 + UP * 0.05, YELLOW_B, radius=0.35, font_size=13)
        y = self.causal_node("Y\nRecovery", LEFT * 3.8 + UP * 0.05, GREEN_B, radius=0.35, font_size=13)
        z_x = Arrow(z.get_bottom(), x.get_top(), buff=0.08, color=RED_B, stroke_width=4)
        z_y = Arrow(z.get_bottom(), y.get_top(), buff=0.08, color=RED_B, stroke_width=4)
        x_y = Arrow(x.get_right(), y.get_left(), buff=0.08, color=YELLOW_B, stroke_width=3.5)
        backdoor_label = Text("Backdoor path", font_size=15, color=RED_B).next_to(VGroup(z_x, z_y), LEFT, buff=0.08)

        challenge = self.mini_card(
            "Challenge",
            ["Treatment assignment is biased.", "Gender Z affects X and Y."],
            width=5.0,
            color=RED_B,
            title_size=20,
            body_size=15,
        ).move_to(RIGHT * 2.2 + UP * 0.7)

        formula = self.formula_box(
            "P(Y=1 | do(X=1)) = sum_z P(Y=1 | X=1, Z=z) P(Z=z)",
            width=11.3,
            color=YELLOW_B,
            font_size=18,
        ).move_to(DOWN * 0.82)

        col_x = [-3.75, -1.15, 1.25, 3.55]
        header_y = -1.36
        men_y = -1.82
        women_y = -2.20
        headers = VGroup(*[
            Text(label, font_size=15, color=color).move_to(RIGHT * x + UP * header_y)
            for x, label, color in zip(
                col_x,
                ["Z subgroup", "Recovery if treated", "Population weight", "Contribution"],
                [BLUE_B, GREEN_B, YELLOW_B, ORANGE],
            )
        ])
        men_row = VGroup(*[
            Text(label, font_size=16, color=color).move_to(RIGHT * x + UP * men_y)
            for x, label, color in zip(col_x, ["Men", "0.60", "0.50", "0.30"], [GRAY_A, GREEN_B, YELLOW_B, ORANGE])
        ])
        women_row = VGroup(*[
            Text(label, font_size=16, color=color).move_to(RIGHT * x + UP * women_y)
            for x, label, color in zip(col_x, ["Women", "0.40", "0.50", "0.20"], [GRAY_A, GREEN_B, YELLOW_B, ORANGE])
        ])
        table = VGroup(headers, men_row, women_row)
        table_box = RoundedRectangle(
            corner_radius=0.08,
            width=9.25,
            height=1.35,
            stroke_color=GRAY_B,
            stroke_width=1.7,
            fill_color=BLACK,
            fill_opacity=0.22,
        ).move_to(UP * -1.80)
        table_rules = VGroup(
            Line(LEFT * 4.45 + UP * -1.58, RIGHT * 4.45 + UP * -1.58, color=GRAY_D, stroke_width=1.2),
            Line(RIGHT * -2.45 + UP * -1.18, RIGHT * -2.45 + UP * -2.42, color=GRAY_D, stroke_width=1.0),
            Line(RIGHT * 0.05 + UP * -1.18, RIGHT * 0.05 + UP * -2.42, color=GRAY_D, stroke_width=1.0),
            Line(RIGHT * 2.45 + UP * -1.18, RIGHT * 2.45 + UP * -2.42, color=GRAY_D, stroke_width=1.0),
        )
        table_group = VGroup(table_box, table_rules, table)

        naive = self.text_box("Naive pooled\nP(Y=1 | X=1) = 0.80", width=3.1, color=RED_B, font_size=15, padding=0.14).to_edge(DOWN, buff=0.25).shift(LEFT * 4.55)
        adjusted = self.text_box("Adjusted causal\n0.30 + 0.20 = 0.50", width=3.35, color=GREEN_B, font_size=15, padding=0.14).to_edge(DOWN, buff=0.25).shift(RIGHT * 4.35)
        conclusion_arrow = Arrow(naive.get_right(), adjusted.get_left(), buff=0.15, color=YELLOW_B, stroke_width=4)

        self.play(FadeIn(tag), FadeIn(subtitle, shift=UP * 0.08), run_time=0.55)
        self.play(FadeIn(VGroup(z, x, y)), GrowArrow(z_x), GrowArrow(z_y), GrowArrow(x_y), FadeIn(backdoor_label), run_time=0.85)
        self.play(FadeIn(challenge, shift=LEFT * 0.08), run_time=0.6)
        self.play(FadeIn(formula, scale=1.02), run_time=0.75)
        self.play(FadeIn(table_group, shift=UP * 0.08), run_time=0.75)
        self.play(FadeIn(naive), GrowArrow(conclusion_arrow), FadeIn(adjusted), Flash(adjusted.get_center(), color=GREEN_B), run_time=0.85)
        self.next_slide()
