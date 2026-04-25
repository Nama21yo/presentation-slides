from manim import *
from manim_slides import Slide


class AtomspaceBase(Slide):
    CONFIG = {"camera_config": {"background_color": BLACK}}

    def text_box(self, text: str, width: float = 4.0, color=BLUE_B, font_size: int = 24, padding: float = 0.2) -> VGroup:
        box = RoundedRectangle(
            corner_radius=0.08,
            width=width,
            height=padding * 2 + 0.6,
            stroke_color=color,
            stroke_width=2,
            fill_color=BLACK,
            fill_opacity=0.25,
        )
        label = Text(text, font_size=font_size, color=color).move_to(box)
        return VGroup(box, label)

    def causal_node(self, label: str, position: np.ndarray, color, radius: float = 0.4, font_size: int = 20) -> VGroup:
        circle = Circle(radius=radius, color=color, stroke_width=3, fill_color=BLACK, fill_opacity=0.4)
        text = Text(label, font_size=font_size, color=color).move_to(circle)
        circle.move_to(position)
        text.move_to(circle)
        return VGroup(circle, text)

    def formula_box(self, text: str, width: float = 8.0, color=YELLOW_B, font_size: int = 20) -> VGroup:
        box = RoundedRectangle(
            corner_radius=0.06,
            width=width,
            height=0.55,
            stroke_color=color,
            stroke_width=2,
            fill_color=BLACK,
            fill_opacity=0.2,
        )
        label = Text(text, font_size=font_size, color=color).move_to(box)
        return VGroup(box, label)

    def mini_card(self, title: str, body_lines: list, width: float, color, title_size: int = 18, body_size: int = 14) -> VGroup:
        lines = []
        for i, line in enumerate(body_lines):
            t = Text(line, font_size=body_size, color=GRAY_A if i > 0 else color)
            lines.append(t)
        content = VGroup(*lines).arrange(DOWN, aligned_edge=LEFT, buff=0.08)
        
        title_text = Text(title, font_size=title_size, color=color)
        header = VGroup(title_text, content).arrange(DOWN, aligned_edge=LEFT, buff=0.12)
        
        box = RoundedRectangle(
            corner_radius=0.06,
            width=width,
            height=header.height + 0.3,
            stroke_color=color,
            stroke_width=1.5,
            fill_color=BLACK,
            fill_opacity=0.2,
        )
        header.move_to(box)
        return VGroup(box, header)


class AtomspaceSlide1(AtomspaceBase):
    def construct(self):
        tag = self.text_box("The Hyperon Atomspace", width=5.5, color=YELLOW_B, font_size=32)
        tag.to_edge(UP, buff=0.32)
        subtitle = Text("The universal memory substrate of AGI", font_size=21, color=GRAY_A)
        subtitle.next_to(tag, DOWN, buff=0.14)

        left_title = Text("Traditional AI", font_size=24, color=RED_B).move_to(LEFT * 3.5 + UP * 1.4)
        right_title = Text("Hyperon Atomspace", font_size=24, color=GREEN_B).move_to(RIGHT * 3.5 + UP * 1.4)
        divider = Line(UP * 1.7, DOWN * 2.0, color=GRAY_D, stroke_width=1.5)

        db_width, db_height = 1.6, 1.4
        db_positions = [
            (LEFT * 4.2 + DOWN * 0.3, "Facts", BLUE_B),
            (LEFT * 2.8 + DOWN * 0.3, "Programs", ORANGE),
            (LEFT * 2.0 + DOWN * 0.3, "Neural\nNets", PURPLE_B),
        ]
        
        left_dbs = VGroup()
        for pos, label, color in db_positions:
            rect = RoundedRectangle(
                corner_radius=0.1,
                width=db_width,
                height=db_height,
                stroke_color=color,
                stroke_width=2,
                fill_color=BLACK,
                fill_opacity=0.3,
            ).move_to(pos)
            lbl = Text(label, font_size=18, color=color).move_to(rect)
            left_dbs.add(VGroup(rect, lbl))

        atomspace = Circle(
            radius=1.5,
            stroke_color=GREEN_B,
            stroke_width=4,
            fill_color=BLACK,
            fill_opacity=0.35,
        ).move_to(RIGHT * 3.5 + DOWN * 0.3)
        
        node_positions = [
            atomspace.get_center() + LEFT * 0.7 + UP * 0.5,
            atomspace.get_center() + LEFT * 0.4 + DOWN * 0.6,
            atomspace.get_center() + RIGHT * 0.6 + UP * 0.5,
            atomspace.get_center() + RIGHT * 0.3 + DOWN * 0.5,
            atomspace.get_center() + UP * 0.15,
        ]
        node_colors = [BLUE_B, BLUE_B, ORANGE, ORANGE, PURPLE_B]
        atom_nodes = VGroup()
        for i, (pos, color) in enumerate(zip(node_positions, node_colors)):
            atom_nodes.add(Circle(radius=0.2, color=color, fill_opacity=0.5).move_to(pos))

        connections = [
            (0, 2), (1, 3), (2, 4), (3, 4)
        ]
        connection_lines = VGroup()
        for i, j in connections:
            connection_lines.add(
                Line(
                    atom_nodes[i].get_center(),
                    atom_nodes[j].get_center(),
                    color=WHITE,
                    stroke_width=2,
                )
            )

        problem_title = Text("The Problem:", font_size=20, color=RED_B).to_edge(DOWN, buff=2.0).shift(LEFT * 2.8)
        problem_desc = VGroup(
            Text("Deep learning, symbolic logic, and", font_size=15, color=GRAY_A),
            Text("evolutionary algorithms use", font_size=15, color=GRAY_A),
            Text("incompatible databases", font_size=15, color=GRAY_A),
        ).arrange(DOWN, aligned_edge=LEFT, buff=0.05).next_to(problem_title, DOWN, buff=0.1)

        solution_title = Text("The Solution:", font_size=20, color=GREEN_B).to_edge(DOWN, buff=2.0).shift(RIGHT * 2.8)
        solution_desc = VGroup(
            Text("Cognitive Synergy:", font_size=15, color=GRAY_A),
            Text("A Distributed Metagraph", font_size=15, color=GRAY_A),
            Text("acts as the 'gray matter'", font_size=15, color=GRAY_A),
        ).arrange(DOWN, aligned_edge=LEFT, buff=0.05).next_to(solution_title, DOWN, buff=0.1)

        self.play(FadeIn(tag), FadeIn(subtitle, shift=UP * 0.08), run_time=0.55)
        self.play(Create(divider), FadeIn(VGroup(left_title, right_title)), run_time=0.45)
        self.play(FadeIn(left_dbs, shift=LEFT * 0.15), run_time=0.75)
        self.play(FadeIn(atomspace, scale=1.05), FadeIn(atom_nodes), run_time=0.85)
        self.play(Create(connection_lines), run_time=0.55)
        self.play(FadeIn(problem_title), FadeIn(problem_desc, shift=DOWN * 0.1), run_time=0.65)
        self.play(FadeIn(solution_title), FadeIn(solution_desc, shift=DOWN * 0.1), run_time=0.65)
        self.next_slide()


class AtomspaceSlide2(AtomspaceBase):
    def construct(self):
        tag = self.text_box("Atoms: Building Blocks of Thought", width=7.2, color=YELLOW_B, font_size=28)
        tag.to_edge(UP, buff=0.32)
        subtitle = Text("Constructing knowledge via Nodes and Links", font_size=21, color=GRAY_A)
        subtitle.next_to(tag, DOWN, buff=0.14)

        nodes_title = Text("Nodes (The 'Nouns')", font_size=22, color=BLUE_B).move_to(LEFT * 3.2 + UP * 1.25)
        
        node_examples = [
            ("ConceptNode\n'Dog'", BLUE_B, LEFT * 3.9 + DOWN * 0.35, 16),
            ("NumberNode\n42", YELLOW_B, LEFT * 3.2 + DOWN * 0.35, 16),
            ("VariableNode\nX, Y", GREEN_B, LEFT * 2.5 + DOWN * 0.35, 16),
        ]
        
        node_group = VGroup()
        for label, color, pos, fsize in node_examples:
            circle = Circle(radius=0.45, color=color, fill_opacity=0.3).move_to(pos)
            text = Text(label, font_size=fsize, color=color).move_to(circle)
            node_group.add(VGroup(circle, text))

        links_title = Text("Links (The 'Verbs')", font_size=22, color=ORANGE).move_to(RIGHT * 3.2 + UP * 1.25)
        
        link_examples = [
            ("InheritanceLink\nDog -> Animal", ORANGE, RIGHT * 3.9 + DOWN * 0.5, 13),
            ("EvaluationLink\nEats -> Dog, Meat", YELLOW_B, RIGHT * 3.2 + DOWN * 0.5, 13),
            ("HYPERGRAPH\nLink -> N nodes\nLink -> Link", PURPLE_B, RIGHT * 2.5 + DOWN * 0.5, 11),
        ]
        
        link_group = VGroup()
        for label, color, pos, fsize in link_examples:
            box = RoundedRectangle(
                corner_radius=0.08,
                width=1.3,
                height=0.65,
                stroke_color=color,
                stroke_width=2,
                fill_color=BLACK,
                fill_opacity=0.3,
            ).move_to(pos)
            text = Text(label, font_size=fsize, color=color).move_to(box)
            link_group.add(VGroup(box, text))

        what_is = self.text_box("What is an Atom?", width=3.5, color=WHITE, font_size=24, padding=0.18)
        what_is.to_edge(DOWN, buff=2.0)
        definition = Text("The fundamental base unit of knowledge in Hyperon", font_size=18, color=GRAY_A).next_to(what_is, DOWN, buff=0.2)

        self.play(FadeIn(tag), FadeIn(subtitle, shift=UP * 0.08), run_time=0.55)
        self.play(FadeIn(nodes_title), FadeIn(links_title), run_time=0.45)
        self.play(FadeIn(node_group, shift=LEFT * 0.15), run_time=0.75)
        self.play(FadeIn(link_group, shift=RIGHT * 0.15), run_time=0.75)
        self.play(FadeIn(what_is), FadeIn(definition, shift=DOWN * 0.1), run_time=0.65)
        self.next_slide()


class AtomspaceSlide3(AtomspaceBase):
    def construct(self):
        tag = self.text_box("Atom Properties", width=5.0, color=YELLOW_B, font_size=32)
        tag.to_edge(UP, buff=0.32)
        subtitle = Text("The mathematical currencies of the AGI's mind", font_size=21, color=GRAY_A)
        subtitle.next_to(tag, DOWN, buff=0.14)

        atom_visual = Circle(
            radius=1.0,
            stroke_color=YELLOW_B,
            stroke_width=3,
            fill_color=BLACK,
            fill_opacity=0.4,
        ).move_to(LEFT * 2.8 + DOWN * 0.5)
        atom_label = Text("Atom", font_size=24, color=YELLOW_B).move_to(atom_visual)

        tv_title = Text("TruthValue (Belief)", font_size=22, color=BLUE_B).move_to(RIGHT * 2.8 + UP * 1.3)
        
        tv_formula = self.formula_box("(s, c)", width=2.5, color=WHITE, font_size=20).move_to(RIGHT * 2.8 + UP * 0.55)
        
        tv_details = VGroup(
            Text("Strength (s): Empirical truth", font_size=16, color=GRAY_A),
            Text("Confidence (c): Weight of evidence", font_size=16, color=GRAY_A),
        ).arrange(DOWN, aligned_edge=LEFT, buff=0.12).move_to(RIGHT * 2.8 + DOWN * 0.2)

        av_title = Text("AttentionValue (Focus)", font_size=22, color=GREEN_B).move_to(RIGHT * 2.8 + DOWN * 1.3)
        
        sti_bar = Rectangle(
            width=0.22,
            height=0.65,
            color=GREEN_B,
            fill_opacity=0.5,
        ).move_to(RIGHT * 2.55 + DOWN * 1.3)
        lti_bar = Rectangle(
            width=0.22,
            height=0.4,
            color=TEAL_B,
            fill_opacity=0.5,
        ).move_to(RIGHT * 3.05 + DOWN * 1.45)
        
        sti_label = Text("STI: Short-Term", font_size=14, color=GREEN_B).next_to(sti_bar, RIGHT, buff=0.08)
        lti_label = Text("LTI: Long-Term", font_size=14, color=TEAL_B).next_to(lti_bar, RIGHT, buff=0.08)

        self.play(FadeIn(tag), FadeIn(subtitle, shift=UP * 0.08), run_time=0.55)
        self.play(FadeIn(atom_visual), FadeIn(atom_label), run_time=0.65)
        self.play(FadeIn(tv_title), run_time=0.45)
        self.play(FadeIn(tv_formula), FadeIn(tv_details), run_time=0.65)
        self.play(FadeIn(av_title), run_time=0.35)
        self.play(FadeIn(sti_bar), FadeIn(lti_bar), FadeIn(sti_label), FadeIn(lti_label), run_time=0.55)
        self.next_slide()


class AtomspaceSlide4(AtomspaceBase):
    def construct(self):
        tag = self.text_box("Everything = Atom", width=4.5, color=YELLOW_B, font_size=32)
        tag.to_edge(UP, buff=0.32)
        subtitle = Text("Breaking down the barriers of computation", font_size=21, color=GRAY_A)
        subtitle.next_to(tag, DOWN, buff=0.14)

        items = [
            ("Facts", "The sky is blue", BLUE_B, LEFT * 3.5 + UP * 0.7),
            ("Programs", "MeTTa code\nLambdaLinks", ORANGE, LEFT * 1.3 + UP * 0.7),
            ("Neural\nActivations", "Weights/Biases\nas vectors", PURPLE_B, RIGHT * 1.3 + UP * 0.7),
            ("Goals", "Target nodes\nhigh weight", GREEN_B, RIGHT * 3.5 + UP * 0.7),
        ]

        item_group = VGroup()
        for label, desc, color, pos in items:
            box = RoundedRectangle(
                corner_radius=0.08,
                width=1.4,
                height=1.0,
                stroke_color=color,
                stroke_width=2,
                fill_color=BLACK,
                fill_opacity=0.3,
            ).move_to(pos)
            lbl = Text(label, font_size=18, color=color).move_to(box.get_center() + UP * 0.22)
            dsc = Text(desc, font_size=12, color=GRAY_A).move_to(box.get_center() + DOWN * 0.18)
            item_group.add(VGroup(box, lbl, dsc))

        fused = VGroup(
            Circle(
                radius=0.7,
                stroke_color=YELLOW_B,
                stroke_width=4,
                fill_color=BLACK,
                fill_opacity=0.45,
            ).move_to(ORIGIN + DOWN * 0.8),
            Text("ATOM", font_size=20, color=YELLOW_B).move_to(ORIGIN + DOWN * 0.8),
        )

        arrows_to_center = VGroup(
            Line(LEFT * 2.4 + UP * 0.7, ORIGIN + DOWN * 0.8, color=BLUE_B, stroke_width=2.5),
            Line(LEFT * 2.2 + UP * 0.7, ORIGIN + DOWN * 0.8, color=ORANGE, stroke_width=2.5),
            Line(RIGHT * 2.2 + UP * 0.7, ORIGIN + DOWN * 0.8, color=PURPLE_B, stroke_width=2.5),
            Line(RIGHT * 2.4 + UP * 0.7, ORIGIN + DOWN * 0.8, color=GREEN_B, stroke_width=2.5),
        )

        result_title = Text("The Result:", font_size=20, color=WHITE).to_edge(DOWN, buff=1.8)
        result_lines = VGroup(
            Text("Logic engine can verify neural weights.", font_size=14, color=GRAY_A),
            Text("Evolutionary algorithm can mutate code.", font_size=14, color=GRAY_A),
            Text("Neural network can guide logic intuition.", font_size=14, color=GRAY_A),
            Text("Total cognitive synergy.", font_size=14, color=GREEN_B),
        ).arrange(DOWN, aligned_edge=LEFT, buff=0.08).next_to(result_title, DOWN, buff=0.12)

        self.play(FadeIn(tag), FadeIn(subtitle, shift=UP * 0.08), run_time=0.55)
        self.play(FadeIn(item_group, shift=UP * 0.1), run_time=0.85)
        self.play(FadeIn(fused, scale=1.1), run_time=0.65)
        self.play(Create(arrows_to_center), run_time=0.55)
        self.play(FadeIn(result_title), FadeIn(result_lines, shift=DOWN * 0.1), run_time=0.65)
        self.next_slide()