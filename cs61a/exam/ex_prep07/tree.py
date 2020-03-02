class Tree(object):
    def __init__(self, label, branches=None):
        if branches is None:
            branches = []
        self.label = label
        for b in branches:
            assert isinstance(b, Tree)
        self.branches = branches

    def is_leaf(self):
        return not self.branches

    def __repr__(self):
        label_str = repr(self.label)
        if not self.branches:
            branches_str = ""
        else:
            branches_str = ", " + repr(self.branches)
        return "Tree({0}{1})".format(label_str, branches_str)

    def __str__(self, indent=0):
        template = "{0}\n{1}"
        label_str = indent*"  " + str(self.label)
        branches_str = [b.__str__(indent=indent+1) for b in self.branches]
        return template.format(label_str, "\n".join(branches_str)).rstrip()


class Link(object):
    def __init__(self, first, rest=None):
        self.first = first
        assert isinstance(rest, Link) or rest is None
        self.rest = rest

    def __repr__(self):
        first_str = repr(self.first)
        rest_str = "" if self.rest is None else ", "+repr(self.rest)
        return "Link({0}{1})".format(
            first_str,
            rest_str
        )

    def __str__(self):
        string = "<"
        while self.rest is not None:
            string += str(self.first) + " "
            self = self.rest
        return string + str(self.first) + ">"

    def is_last(self):
        return self.rest is None
