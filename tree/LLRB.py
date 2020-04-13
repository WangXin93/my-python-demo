"""
* PDF: <https://www.cs.princeton.edu/~rs/talks/LLRB/LLRB.pdf>
* Code CS61B LLRB: <https://algs4.cs.princeton.edu/33balanced/RedBlackBST.java.html>
* DOC: <http://www.cs.princeton.edu/~rs/talks/LLRB/RedBlack.pdf>
* StackOverflow: <https://stackoverflow.com/questions/15455042/can-anyone-explain-the-deletion-of-left-lean-red-black-tree-clearly>

Left-Leaning Red-Black trees have a 1-1 correspondence with 2-3 trees. Every 2-3 tree has a unique LLRB red-black tree associated with it. As for 2-3-4 trees, they maintain correspondence with standard Red-Black trees.
"""

RED = True
BLACK = False

class Node(object):
    def __init__(self, item, left=None, right=None, color=None):
        self.item = item
        self.left = left
        self.right = right
        self.color = color

class LLRB(object):
    def __init__(self):
        self.root = None
        self.size = 0

    def put(self, item):
        if not self.contains(item):
            self.root = self._putHelper(self.root, item) 
            self.size += 1

    def contains(self, item):
        return self._containsHelper(self.root, item)

    def delete(self, item):
        if not self.contains(item):
            return False
        if not self.isRed(self.root.left) and not self.isRed(self.root.right):
            self.root.color = RED
        self.root = self._deleteHelper(self.root, item)
        self.size -= 1
        if self.size > 0:
            self.root.color = BLACK
        return True

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
            return Node(item, None, None, RED)
        # If flipColors is put here, it will be a top-down 2-3-4 tree.
        # if self.isRed(node.left) and self.isRed(node.right):
        #     self.flipColors(node)
        if node.item > item:
            node.left = self._putHelper(node.left, item)
        elif node.item < item:
            node.right = self._putHelper(node.right, item)

        # Fix any right-learning links
        # https://joshhug.gitbooks.io/hug61b/content/chap11/chap115.html
        if self.isRed(node.right) and not self.isRed(node.left):
            node = self.rotateLeft(node)
        if self.isRed(node.left) and self.isRed(node.left.left):
            node = self.rotateRight(node)
        if self.isRed(node.left) and self.isRed(node.right):
            self.flipColors(node)
        return node

    def _deleteHelper(self, node, item):
        """
        For Left Leaning Red Black tree, Just like a new node is red, we always also want to delete a red node. If the node isn't red, then we want to make it red first
        """
        if item < node.item:
            if (not self.isRed(node.left)) and (not self.isRed(node.left.left)):
                node = self.moveRedLeft(node)
            node.left = self._deleteHelper(node.left, item)
        else:
            if self.isRed(node.left):
                node = self.rotateRight(node)
            if (node.item == item) and (self._isNIL(node.right)):
                return None
            if (not self.isRed(node.right)) and (not self.isRed(node.right.left)):
                node = self.moveRedRight(node)
            if node.item == item:
                x = self._min(node.right)
                node.item = x.item
                node.right = self._deleteMin(node.right)
            else:
                node.right = self._deleteHelper(node.right, item)
        return self.balance(node)

    def balance(self, node):
        """ restore red-black tree invariant
        """
        if self.isRed(node.right):
            node = self.rotateLeft(node)
        if self.isRed(node.left) and self.isRed(node.left.left):
            node = self.rotateRight(node)
        if self.isRed(node.left) and self.isRed(node.right):
            self.flipColors(node)
        return node

    def _deleteMin(self, node):
        if self._isNIL(node.left):
            return None

        if not self.isRed(node.left) and not self.isRed(node.left.left):
            node = self.moveRedLeft(node)

        node.right = self._deleteMin(node.right)

        return self.balance(node)

    def deleteMaxRoot(self):
        self.root = self._deleteMax(self.root)
        self.root.color = BLACK;

    def deleteMinRoot(self):
        self.root = self._deleteMin(self.root)
        self.root.color = BLACK;

    def _deleteMax(self, node):
        if self.isRed(node.left):
            node = self.rotateRight(node)

        if self._isNIL(node.right):
            return None

        if (not self.isRed(node.right)) and (not self.isRed(node.right.left)):
            node = self.moveRedRight(node)

        node.right = self._deleteMax(node.right)

        return self.balance(node)

    def _min(self, node):
        if self._isNIL(node.left):
            return node
        else:
            return self._min(node.left)

    def rotateLeft(self, node):
        """ rotateLeft(G): Let x be the right child of G. Make G the new left child of x."""
        x = node.right
        node.right = x.left
        x.left = node
        x.color = x.left.color;
        x.left.color = RED
        return x

    def rotateRight(self, node):
        """ rotateRight(G): Let x be the left child of G. Make G the new right child of x."""
        x = node.left
        node.left = x.right
        x.right = node
        x.color = x.right.color;
        x.right.color = RED
        return x

    def moveRedLeft(self, node):
        """
        Assuming that h is red and both h.left and h.left.left are black, make h.left or one of its children red.
        """
        self.flipColors(node)
        if self.isRed(node.right.left):
            node.right = self.rotateRight(node.right)
            node = self.rotateLeft(node)
            self.flipColors(node)
        return node

    def moveRedRight(self, node):
        """
        Assuming that h is red and both h.right and h.right.left are black, make h.right or one of its children red.
        """
        self.flipColors(node)
        if self.isRed(node.left.left):
            node = self.rotateRight(node)
            self.flipColors(node)
        return node

    def flipColors(self, node):
        node.color = not node.color
        node.left.color = not node.left.color
        node.right.color = not node.right.color

    def isRed(self, node):
        if self._isNIL(node):
            return False
        return node.color == RED

    def display(self):
        self._displayHelper3(self.root, "")

    def _displayHelper3(self, node, prefix):
        """
        https://stackoverflow.com/questions/9727673/list-directory-tree-structure-in-python
        node_prefix_middle = "├──"
        node_prefix_last = "└──"
        parent_prefix_middle = "│   "
        parent_prefix_last = "   "
        node_prefix_first = "┌──"
        """
        if self._isNIL(node):
            return

        if prefix == "":
            self._displayHelper3(node.left, prefix +"┌──")
        elif prefix[-3:] == "└──":
            self._displayHelper3(node.left, prefix[:-3] + "│  " +"┌──")
        else:
            self._displayHelper3(node.left, prefix[:-3] + "   " + "┌──")

        displayColor = "R" if node.color == RED else "B"
        print(prefix + str(node.item) + "({})".format(displayColor))

        if prefix == "":
            self._displayHelper3(node.right, prefix +"└──")
        elif  prefix[-3:] == "┌──":
            self._displayHelper3(node.right, prefix[:-3] + "│  "+"└──")
        else:
            self._displayHelper3(node.right, prefix[:-3] + "   " + "└──")


    def _displayHelper2(self, node, prefix):
        """
        node_prefix_middle = "├──"
        node_prefix_last = "└──"
        parent_prefix_middle = "│   "
        parent_prefix_last = "   "
        """
        if self._isNIL(node):
            return
        print(prefix + str(node.item))

        if prefix[-3:] == "├──":
            prefix = prefix[:-3] + "│  "
        elif prefix[-3:] == "└──":
            prefix = prefix[:-3] + "   "

        if self._isNIL(node.left):
            self._displayHelper2(node.right, prefix+"└──")
        elif self._isNIL(node.right):
            self._displayHelper2(node.left, prefix+"└──")
        else:
            self._displayHelper2(node.left, prefix+"├──")
            self._displayHelper2(node.right, prefix+"└──")

    def _displayHelper(self, node, prefix=""):
        if self._isNIL(node):
            return 
        self._displayHelper(node.left, prefix+" ")
        print(prefix + str(node.item))
        self._displayHelper(node.right, prefix+" ")
