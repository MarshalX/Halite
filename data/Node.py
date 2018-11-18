class Node(object):
    def __init__(self, number):
        self.number = number

        self._links = []

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
