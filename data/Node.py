from hlt.positionals import Position


class Node(object):
    def __init__(self, number, i=0, j=0):
        self.number = number
        self.position = Position(i, j)

        self._links = []

        self.halite_amount = 0
        self.ship, self.structure = None, None

    def __getitem__(self, item):
        return self._links[item]

    def __str__(self):
        return 'NODE. Number: {}; Count of links: {}'.format(self.number, len(self._links))

    def fully_str(self):
        result = [self.__str__()]
        for link in self._links:
            result.append(link.__str__())

        return '\n'.join(result)

    def add_link(self, link):
        self._links.append(link)
