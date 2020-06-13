"""
        1
    /       \
   2         2
  / \       / \
 3   4     4   3
/ \ / \   / \ / \
5 6 7 8   8 7 6 5
"""
from utils import TreeNode, stringToTreeNode, prettyPrintTree


class Solution:
    def isSymmetric(self, root: TreeNode) -> bool:
        if root is None:
            return True
        return self.isMirror(root.left, root.right)

    def isMirror(self, left, right):
        if left is None:
            return right is None
        if right is None:
            return left is None
        return left.val == right.val and self.isMirror(left.left, right.right) and self.isMirror(left.right, right.left)


if __name__ == "__main__":
    t = stringToTreeNode("[1,2,2,null,3,null,3]")
    print(Solution().isSymmetric(t))  # False
    t = stringToTreeNode("[1,2,3]")
    print(Solution().isSymmetric(t))  # False
