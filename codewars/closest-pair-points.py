from itertools import combinations
from collections import namedtuple
from operator import itemgetter
from pprint import pformat

import math
from scipy.spatial import cKDTree as KDT


def closest_pair(points):
    # Brute force
    # minDist = float('inf')
    # out = None
    # for pair in combinations(points, 2):
    #     d = dist(*pair)
    #     if d < minDist:
    #         minDist = d
    #         out = pair
    # return out

    # My KDTree
    # tree = kdtree(list(points))
    # minDist, pair = float('inf'), None
    # for point in points:
    #     newDist, newPoint = nearest(tree, point, 0, float('inf'), None, 0)
    #     if newDist < minDist:
    #         minDist = newDist
    #         pair = (newPoint, point)
    # return pair

    # Use scipy
    tree = KDT(points)
    dists, idxs = tree.query(points, k=2)
    dists, idxs = dists[:, 1], idxs[:, 1]
    minIdx = dists.argmin()
    return points[minIdx], points[idxs[minIdx]]


class Node(namedtuple('Node', 'location left_child right_child')):
    def __repr__(self):
        return pformat(tuple(self))


def kdtree(point_list, depth: int = 0):
    if not point_list:
        return None
    k = len(point_list[0])  # assumes all points have the same dimension
    # Select axis based on depth so that axis cycles through all valid values
    axis = depth % k
    # Sort point list by axis and choose median as pivot element
    point_list.sort(key=itemgetter(axis))
    median = len(point_list) // 2
    # Create node and construct subtrees
    return Node(location=point_list[median],
                left_child=kdtree(point_list[:median], depth + 1),
                right_child=kdtree(point_list[median + 1:], depth + 1))


def dist(p1, p2):
    return math.sqrt((p1[0] - p2[0])**2 + (p1[1] - p2[1])**2)


def nearest(tree, point, depth, minDist, minPoint, duplicate):
    if tree is None:
        return minDist, minPoint
    k = len(point)
    axis = depth % k
    currDist = dist(tree.location, point)
    if currDist == 0:
        duplicate += 1
    if duplicate >= 2:
        return 0, point
    if 0 < currDist < minDist:
        minDist = currDist
        minPoint = tree.location
    if point[axis] >= tree.location[axis]:
        closeSide = tree.right_child
        farSide = tree.left_child
    else:
        closeSide = tree.right_child
        farSide = tree.left_child
    minDistClose, minPointClose = nearest(closeSide, point, depth + 1, minDist,
                                          minPoint, duplicate)
    if minDistClose < minDist:
        minDist = minDistClose
        minPoint = minPointClose
    if abs(point[axis] - tree.location[axis]) < minDist:
        minDistFar, minPointFar = nearest(farSide, point, depth + 1, minDist,
                                          minPoint, duplicate)
        if minDistFar < minDist:
            minDist = minDistFar
            minPoint = minPointFar
    return minDist, minPoint


points = (
    (2, 2),  # A
    (2, 8),  # B
    (5, 5),  # C
    (6, 3),  # D
    (6, 7),  # E
    (7, 4),  # F
    (7, 9)  # G
)

duplicated_points = (
    (2, 2),  # A
    (2, 8),  # B
    (5, 5),  # C
    (5, 5),  # C
    (6, 3),  # D
    (6, 7),  # E
    (7, 4),  # F
    (7, 9)  # G
)

if __name__ == "__main__":
    print(closest_pair(points))
    print(closest_pair(duplicated_points))
