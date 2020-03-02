class Yolo(object):
    """
    >>> x = Yolo(1)
    >>> x.g(3)
    4
    >>> x.g(5)
    6
    >>> x.motto = 5
    >>> x.g(5)
    10
    """
    def __init__(self, n):
        self.motto = 1

    def g(self, s):
        return self.motto + s
