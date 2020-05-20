"""
* CS61B LLRB: <https://algs4.cs.princeton.edu/33balanced/RedBlackBST.java.html>
* Java TreeMap with Red Black Tree: <https://github.com/AdoptOpenJDK/openjdk-jdk11/blob/999dbd4192d0f819cb5224f26e9e7fa75ca6f289/src/java.base/share/classes/java/util/TreeMap.java>
"""

class Node(object):
    def __init__(self, item, left=None, right=None, color=None):
        self.item = item
        self.left = left
        self.right = right
        self.color = color

class BST(object):
    def __init__(self):
        self.root = None
        self.size = 0

    def put(self, item):
        if not self.contains(item):
            self.root = self._putHelper(self.root, item) 
            self.root.color = BLACK
            self.size += 1

    def contains(self, item):
        return self._containsHelper(self.root, item)

    def delete(self, item):
        if self.contains(item):
            self.root = self._deleteHelper(self.root, item)
            self.size -= 1
            return True
        else:
            return False

    def _isNIL(self, node):
        return node == None

    def _containsHelper(self, node, item):
        if self._isNIL(node):
            return False
        elif node.item == item:
            return True
        elif node.item > item:
            return self._containsHelper(node.left, item)
        elif node.item < item:
            return self._containsHelper(node.right, item)

    def _putHelper(self, node, item):
        if self._isNIL(node):
            return Node(item, None, None, None)
        elif node.item > item:
            node.left = self._putHelper(node.left, item)
        elif node.item < item:
            node.right = self._putHelper(node.right, item)
        return node

    def _deleteHelper(self, node, item):
        """ Deletion has 3 cases: 
        * if deleting node with no children, i.e., it is a leaf, replace it with None; 
        * else if the node with 1 children, use its children to replace itself; 
        * the node with 2 children is tricky, one way is to find a successor from its leaves to replace itself, then delete the successor, the successor can be either the maximum on the left child or the minimum on the right child.
        """
        if self._isNIL(node):
            return
        if node.item > item:
            node.left = self._deleteHelper(node.left, item)
        elif node.item < item:
            node.right = self._deleteHelper(node.right, item)
        elif node.item == item:
            if self._isNIL(node.left):
                return node.right
            elif self._isNIL(node.right):
                return node.left
            else:
                returnNode = self._min(node.right)
                returnNode.right = self._deleteMin(node.right)
                returnNode.left = node.left
                return returnNode

    def _deleteMin(self, node):
        if self._isNIL(node.left):
            return node.right
        else:
            return self._deleteMin(node)

    def _min(self, node):
        if self._isNIL(node.left):
            return node
        else:
            return self._min(node.left)

    def display(self):
        self._displayHelper(self.root, "")

    def _displayHelper(self, node, prefix=""):
        if self._isNIL(node):
            return 
        self._displayHelper(node.left, prefix+" ")
        print(prefix + str(node.item))
        self._displayHelper(node.right, prefix+" ")

