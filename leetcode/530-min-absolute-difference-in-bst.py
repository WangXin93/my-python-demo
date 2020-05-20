# Definition for a binary tree node.
# in order tree traverse can get a sorted list for BST
# The minimum value difference between two neighbors in a sorted list is the answer.

from utils import stringToTreeNode, prettyPrintTree

class Solution:
    def getMinimumDifference(self, root):
        L = []
        def dfs(node):
            if node.left: dfs(node.left)
            L.append(node.val)
            if node.right: dfs(node.right)
        dfs(root)
        return min(b - a for a, b in zip(L, L[1:]))


if __name__ == "__main__":
    t = stringToTreeNode("[2, 1, 3]")
    prettyPrintTree(t)
    print(Solution().getMinimumDifference(t))

