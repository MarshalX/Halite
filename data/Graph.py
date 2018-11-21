import math

from hlt.entity import Entity
from hlt.positionals import Position

from utils.Position import normalize

from data.Node import Node
from data.Link import Link


class Graph(object):
    def __init__(self, game_map):
        self.width = game_map.width
        self.height = game_map.height

        self.nodes_count = self.width * self.height
        self.links_count = self.nodes_count * 4

        self._nodes = [Node(number, number % self.width, number // self.height) for number in range(self.nodes_count)]
        self._links = []

        self.build_links()
        self._set_weight(game_map)

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

    def _set_weight(self, game_map):
        for i in range(game_map.height):
            for j in range(game_map.width):
                ceil = game_map[Position(i, j)]
                node = self[ceil.position]

                node.halite_amount = ceil.halite_amount
                node.structure = ceil.structure
                node.ship = ceil.ship

                for link in node:
                    link.weight = math.floor(ceil.halite_amount * 0.1)

    def update_weight(self, game_map):
        #   TODO: Оптимизировать
        self._set_weight(game_map)

    def __str__(self):
        return 'GRAPH. Nodes: {}; Links: {}'.format(self.nodes_count, self.links_count)

    def __getitem__(self, location):
        if isinstance(location, Position):
            location = normalize(location, self.width, self.height)

            return self._nodes[location.y * self.width + location.x]
        elif isinstance(location, Entity):
            return self._nodes[location.position.y * self.width + location.position.x]
        elif isinstance(location, int):
            return self._nodes[location]
        return None
