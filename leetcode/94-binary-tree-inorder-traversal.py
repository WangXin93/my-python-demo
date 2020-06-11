from utils import TreeNode, stringToTreeNode
from typing import List


class Solution:
    def inorderTraversal(self, root: TreeNode) -> List[int]:
        if root is None:
            return []
        res = [root.val]
        left = self.inorderTraversal(root.left)
        right = self.inorderTraversal(root.right)
        res = left + res + right
        return res

if __name__ == "__main__":
    t = stringToTreeNode("[1,null,2,3]")
    print(Solution().inorderTraversal(t))
    t = stringToTreeNode("[]")
    print(Solution().inorderTraversal(t))
