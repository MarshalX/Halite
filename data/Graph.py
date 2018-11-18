from hlt.entity import Entity
from hlt.positionals import Position

from utils.Position import normalize

from data.Node import Node
from data.Link import Link


class Graph(object):
    def __init__(self, width, height):
        self.width = width
        self.height = height

        self.nodes_count = self.width * self.height
        self.links_count = self.nodes_count * 2

        self._nodes = [Node(i) for i in range(self.nodes_count)]
        self._links = []

        self.build_links()

    def build_links(self):
        for node in self._nodes:
            nodes_to_link = []

            # Связь с правой ячейкой
            if (node.number + 1) % self.height != 0:
                second_node = self._nodes[node.number + 1]
                nodes_to_link.append(second_node)

            # Связь с нижней ячейкой
            if node.number + self.width < self.nodes_count:
                second_node = self._nodes[node.number + self.width]
                nodes_to_link.append(second_node)

            # Связь с началом и концом карты(по горизонтали). Тороидальность мира
            if node.number % self.width == 0:
                second_node = self._nodes[node.number + self.width - 1]
                nodes_to_link.append(second_node)

            # Связь с началом и концом карты(по вертикали). Тороидальность мира
            if node.number < self.height:
                second_node = self._nodes[self.nodes_count - self.width + node.number]
                nodes_to_link.append(second_node)

            for node_to_link in nodes_to_link:
                link = Link(node, node_to_link)

                node.add_link(link)
                node_to_link.add_link(link.swap_direction())

                self._links.append(link)
                self._links.append(link.swap_direction())

    def __str__(self):
        return 'GRAPH. Nodes: {}; Links: {}'.format(len(self._nodes), len(self._links))

    def __getitem__(self, location):
        if isinstance(location, Position):
            location = normalize(location, self.width, self.height)
            return self._nodes[location.y * location.x - 1]
        elif isinstance(location, Entity):
            return self._nodes[location.position.y * location.position.x - 1]
        elif isinstance(location, int):
            return self._nodes[location]
        return None
