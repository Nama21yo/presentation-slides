from manim import *
from manim_slides import Slide
import numpy as np


class HyperonWhitePaperTitleSlide(Slide):
    def _build_neural_cluster(self) -> VGroup:
        rng = np.random.default_rng(7)
        node_points = []
        for _ in range(16):
            x = rng.normal(loc=-4.2, scale=1.0)
            y = rng.normal(loc=0.0, scale=1.35)
            x = np.clip(x, -6.3, -2.3)
            y = np.clip(y, -2.9, 2.9)
            node_points.append(np.array([x, y, 0.0]))

        edges = VGroup()
        for i, p in enumerate(node_points):
            distances = sorted(
                ((np.linalg.norm(p - q), j) for j, q in enumerate(node_points) if j != i),
                key=lambda item: item[0],
            )
            for _, j in distances[:3]:
                if j < i:
                    continue
                edge = Line(node_points[i], node_points[j])
                edge.set_stroke(color=BLUE_E, width=2.0, opacity=0.35)
                edges.add(edge)

        nodes = VGroup()
        glows = VGroup()
        for point in node_points:
            glow = Dot(point, radius=0.16, color=BLUE_D).set_opacity(0.18)
            node = Dot(point, radius=0.055, color=BLUE_B)
            glows.add(glow)
            nodes.add(node)

        neural_cluster = VGroup(edges, glows, nodes)
        return neural_cluster

    def _build_logic_tree(self) -> VGroup:
        center_x = 4.35
        top_y = 2.35
        level_gap = 1.0
        tree_width = 4.6

        tree_points = []
        for level in range(4):
            count = 2**level
            step = tree_width / count
            start_x = center_x - tree_width / 2 + step / 2
            y = top_y - level * level_gap
            for i in range(count):
                tree_points.append(np.array([start_x + i * step, y, 0.0]))

        labels = ["ROOT", "AND", "OR", "A", "B", "C", "D"] + [f"R{i}" for i in range(1, 9)]
        nodes = VGroup()
        for index, point in enumerate(tree_points):
            box = RoundedRectangle(
                corner_radius=0.03,
                width=0.46,
                height=0.24,
                stroke_color=GRAY_A,
                stroke_width=1.7,
                fill_color=GRAY_E,
                fill_opacity=0.22,
            ).move_to(point)
            text = Text(labels[index], font_size=11, color=GRAY_A).move_to(point)
            nodes.add(VGroup(box, text))

        branches = VGroup()
        for parent_idx in range(7):
            left_child_idx = 2 * parent_idx + 1
            right_child_idx = 2 * parent_idx + 2

            parent_box = nodes[parent_idx][0]
            left_box = nodes[left_child_idx][0]
            right_box = nodes[right_child_idx][0]

            left_branch = Line(
                parent_box.get_bottom(),
                left_box.get_top(),
                buff=0.04,
                color=GRAY_B,
            ).set_stroke(width=2.2, opacity=0.78)
            right_branch = Line(
                parent_box.get_bottom(),
                right_box.get_top(),
                buff=0.04,
                color=GRAY_B,
            ).set_stroke(width=2.2, opacity=0.78)

            branches.add(left_branch, right_branch)

        return VGroup(branches, nodes)

    def _build_unified_graph(self) -> VGroup:
        points = {
            "hub": np.array([0.0, -0.1, 0.0]),
            "n1": np.array([-0.9, 0.95, 0.0]),
            "n2": np.array([0.0, 1.2, 0.0]),
            "n3": np.array([0.9, 0.95, 0.0]),
            "n4": np.array([-1.25, -0.05, 0.0]),
            "n5": np.array([1.25, -0.05, 0.0]),
            "n6": np.array([-0.9, -1.05, 0.0]),
            "n7": np.array([0.0, -1.3, 0.0]),
            "n8": np.array([0.9, -1.05, 0.0]),
            "l1": np.array([-2.45, 0.75, 0.0]),
            "l2": np.array([-2.9, -0.05, 0.0]),
            "l3": np.array([-2.3, -0.9, 0.0]),
            "r1": np.array([2.45, 0.75, 0.0]),
            "r2": np.array([2.9, -0.05, 0.0]),
            "r3": np.array([2.3, -0.9, 0.0]),
        }
        ordered_keys = list(points.keys())

        edges_idx = [
            ("hub", "n1"),
            ("hub", "n2"),
            ("hub", "n3"),
            ("hub", "n4"),
            ("hub", "n5"),
            ("hub", "n6"),
            ("hub", "n7"),
            ("hub", "n8"),
            ("n1", "n2"),
            ("n2", "n3"),
            ("n3", "n5"),
            ("n5", "n8"),
            ("n8", "n7"),
            ("n7", "n6"),
            ("n6", "n4"),
            ("n4", "n1"),
            ("n1", "n5"),
            ("n3", "n7"),
            ("n2", "n6"),
            ("n4", "n8"),
            ("l1", "n1"),
            ("l2", "n4"),
            ("l3", "n6"),
            ("r1", "n3"),
            ("r2", "n5"),
            ("r3", "n8"),
            ("l1", "l2"),
            ("l2", "l3"),
            ("r1", "r2"),
            ("r2", "r3"),
            ("l2", "r2"),
        ]
        edge_palette = [BLUE_B, TEAL_B, GREEN_B, YELLOW_B, ORANGE, PINK, PURPLE_B]

        edges = VGroup()
        for idx, (i, j) in enumerate(edges_idx):
            start = points[i]
            end = points[j]
            bend = 0.24 if start[1] <= end[1] else -0.24
            if abs(start[0] - end[0]) < 0.5:
                bend = 0.0
            edge = ArcBetweenPoints(start, end, angle=bend)
            edge.set_stroke(color=edge_palette[idx % len(edge_palette)], width=3.1, opacity=0.84)
            edges.add(edge)

        ambient_rings = VGroup(
            Circle(radius=2.1, color=BLUE_E, stroke_opacity=0.25, stroke_width=2.0),
            Circle(radius=1.45, color=TEAL_E, stroke_opacity=0.22, stroke_width=2.0),
            Circle(radius=0.95, color=GREEN_E, stroke_opacity=0.2, stroke_width=2.0),
        ).move_to(points["hub"])

        nodes = VGroup()
        node_palette = [WHITE, BLUE_B, TEAL_B, GREEN_B, YELLOW_B, ORANGE, PINK, PURPLE_B]
        for idx, key in enumerate(ordered_keys):
            point = points[key]
            base_radius = 0.09 if key == "hub" else 0.062
            glow = Dot(point, radius=base_radius * 2.2, color=node_palette[idx % len(node_palette)]).set_opacity(0.2)
            core = Dot(point, radius=base_radius, color=node_palette[idx % len(node_palette)])
            nodes.add(VGroup(glow, core))

        return VGroup(edges, nodes, ambient_rings)

    def construct(self):
        title = Text("Hyperon White Paper Presentation", font_size=52, weight=BOLD)
        title.to_edge(UP, buff=0.35)
        presenter = Text("Natnael Yohanes - iCog Labs", font_size=26, color=GRAY_A)
        presenter.next_to(title, DOWN, buff=0.2)

        left_label = Text("Chaotic Neural System", font_size=22, color=BLUE_B)
        left_label.move_to(np.array([-4.2, -3.2, 0]))
        right_label = Text("Rigid Logic Tree", font_size=22, color=GRAY_A)
        right_label.move_to(np.array([4.0, -3.2, 0]))

        neural_cluster = self._build_neural_cluster()
        logic_tree = self._build_logic_tree()

        self.play(FadeIn(title, shift=UP * 0.3), FadeIn(presenter, shift=UP * 0.2), run_time=1.4)
        self.play(
            LaggedStart(
                Create(neural_cluster[0]),
                FadeIn(neural_cluster[1], scale=0.95),
                FadeIn(neural_cluster[2], scale=0.95),
                lag_ratio=0.2,
            ),
            LaggedStart(Create(logic_tree[0]), FadeIn(logic_tree[1], scale=0.98), lag_ratio=0.2),
            FadeIn(left_label, shift=UP * 0.2),
            FadeIn(right_label, shift=UP * 0.2),
            run_time=2.0,
        )

        self.play(
            AnimationGroup(
                *[
                    glow.animate.scale(1.25).set_opacity(0.26)
                    for glow in neural_cluster[1]
                ],
                lag_ratio=0.04,
            ),
            run_time=1.2,
        )
        self.play(
            AnimationGroup(
                *[
                    glow.animate.scale(0.8).set_opacity(0.16)
                    for glow in neural_cluster[1]
                ],
                lag_ratio=0.04,
            ),
            run_time=0.9,
        )

        self.next_slide()

        left_anchors = [neural_cluster[2][4], neural_cluster[2][8], neural_cluster[2][11]]
        right_anchors = [logic_tree[1][1], logic_tree[1][2], logic_tree[1][4]]
        failed_links = VGroup()
        for left, right in zip(left_anchors, right_anchors):
            link = DashedLine(
                left.get_center(),
                right.get_center(),
                dash_length=0.16,
                dashed_ratio=0.72,
                color=YELLOW,
            ).set_stroke(width=3.0, opacity=0.9)
            failed_links.add(link)

        for link in failed_links:
            spark = ShowPassingFlash(link.copy().set_stroke(width=7, color=YELLOW), time_width=0.35)
            self.play(Create(link), spark, run_time=0.55)
            self.play(link.animate.set_color(RED_B).set_opacity(0.4), run_time=0.2)
            self.play(FadeOut(link, shift=UP * 0.06), run_time=0.25)

        statement = Text(
            "Hyperon 2025: from AGI to ASI",
            font_size=54,
            weight=BOLD,
            gradient=(BLUE_B, GREEN_B, YELLOW_B),
        )
        statement.move_to(ORIGIN + DOWN * 0.1)
        statement_bg = SurroundingRectangle(statement, corner_radius=0.2, color=WHITE, fill_opacity=0.05, buff=0.2)

        self.play(FadeIn(statement_bg, scale=1.03), FadeIn(statement, shift=UP * 0.2), run_time=1.2)

        self.next_slide()

        unified_graph = self._build_unified_graph()
        unified_label = Text(
            "Unified cognitive graph",
            font_size=24,
            color=WHITE,
        ).next_to(unified_graph, DOWN, buff=0.55)

        self.play(FadeOut(presenter, shift=UP * 0.2), run_time=0.45)

        self.play(
            neural_cluster.animate.shift(RIGHT * 2.4).scale(0.75),
            logic_tree.animate.shift(LEFT * 2.4).scale(0.75),
            run_time=1.2,
        )
        self.play(
            FadeOut(VGroup(neural_cluster, logic_tree, left_label, right_label), scale=0.96),
            FadeIn(unified_graph, scale=1.08),
            statement.animate.scale(0.65).to_edge(UP, buff=1.2),
            FadeOut(statement_bg),
            run_time=1.8,
        )
        self.play(FadeIn(unified_label, shift=UP * 0.15), run_time=0.7)

        pulse_edges = AnimationGroup(
            *[
                edge.animate.set_stroke(opacity=1.0, width=4.0)
                for edge in unified_graph[0]
            ],
            lag_ratio=0.03,
        )
        settle_edges = AnimationGroup(
            *[
                edge.animate.set_stroke(opacity=0.82, width=3.0)
                for edge in unified_graph[0]
            ],
            lag_ratio=0.03,
        )
        self.play(pulse_edges, run_time=1.0)
        self.play(settle_edges, run_time=0.8)

        self.next_slide()
