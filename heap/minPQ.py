""" https://joshhug.gitbooks.io/hug61b/content/chap13/chap132.html
"""

class minPQ(object):
    def __init__(self):
        self.items = []

    def add(self, item):
        """ Add to the end of heap temporarily. Swim up the hierarchy to the proper place."""
        self.items.append(item)
        self.swimup(len(self.items)-1)

    def getSmallest(self):
        """ Return the root of the heap (This is guaranteed to be the minimum by our min-heap property"""
        if self.size() > 0:
            return self.items[0]

    def removeSmallest(self):
        """ Swap the last item in the heap into the root. Sink down the hierarchy to the proper place.
        Sinking involves swapping nodes if parent > child. Swap with the smallest child to preserve min-heap property."""
        smallest = self.items[0]
        self.swap(0, len(self.items)-1)
        self.items = self.items[:-1]
        self.swimdown(0)
        return smallest

    def swimup(self, idx):
        if self.items[idx] < self.items[self.getParentIdx(idx)]:
            self.swap(idx, self.getParentIdx(idx))
            self.swimup(self.getParentIdx(idx))

    def swimdown(self, idx):
        children = self.getChildrenIdx(idx)
        if len(children) == 0:
            return
        smallChild = children[0]
        if len(children) > 1 and self.items[children[1]] < self.items[smallChild]:
            smallChild = children[1]

        if self.items[idx] > self.items[smallChild]:
            self.swap(idx, smallChild)
            self.swimdown(smallChild)

    def swap(self, a, b):
        self.items[a], self.items[b] = self.items[b], self.items[a]

    def getChildrenIdx(self, idx):
        """ Find index of nodes' children as a list
        0: 1, 2
        1: 3, 4
        2: 5, 6
        3, 7, 8
        """
        children = []
        one = idx * 2 + 1
        if one < len(self.items):
            children.append(one)
        two = idx * 2 + 2
        if two < len(self.items):
            children.append(two)
        return children
        
    def getParentIdx(self, idx):
        """
        0, 1, 2, 3, 4, 5, 6, 7
        0, 0, 0, 1, 1, 2, 2, 3
        """
        if idx == 0: return 0
        return (idx-1) // 2

    def size(self):
        return len(self.items)
