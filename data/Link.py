class Link(object):
    def __init__(self, _from, _to, weight=0):
        self._from = _from
        self._to = _to
        self.weight = weight

    def swap_direction(self):
        return Link(self._to, self._from, self.weight)

    def __str__(self):
        return 'LINK. From: {}; To: {}'.format(self._from.number, self._to.number)
