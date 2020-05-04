from collections import namedtuple
from pprint import pformat


class Node(namedtuple("Node", "coord left right")):
    def __repr__(self):
        return pformat(tuple(self))


# class Node:
#     def __init__(self, coord, left=None, right=None):
#         self.coord = coord
#         self.left = left
#         self.right = right

#     def __str__(self):
#         return self._strHelper(self, "")

#     def _strHelper(self, tree, indent):
#         out = "{}{}".format(indent, tree.coord)
#         if tree.left is not None:
#             out += "\n{}".format(
#                 self._strHelper(tree.left, indent+" "))
#         if tree.right is not None:
#             out += "\n{}".format(
#                 self._strHelper(tree.right, indent+" "))
#         return out


def kdtree(lst, axis=0):
    if len(lst) == 0:
        return None
    dim = len(lst[0])
    lst.sort(key=lambda x: x[axis])
    medianIdx = len(lst) // 2
    leftLst = lst[:medianIdx]
    rightLst = lst[medianIdx+1:]
    t = Node(lst[medianIdx],
             kdtree(leftLst, (axis+1) % dim),
             kdtree(rightLst, (axis+1) % dim))
    return t


if __name__ == "__main__":
    lst = [(2, 3), (5, 4), (9, 6), (4, 7), (8, 1), (7, 2), (10, 10)]
    t = kdtree(lst)
    print(t)
