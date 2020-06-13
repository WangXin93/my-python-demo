from utils import TreeNode, stringToTreeNode, prettyPrintTree
from typing import List


class Solution:
    # def levelOrder(self, root: TreeNode) -> List[List[int]]:
    #     res = []
    #     stack = []
    #     if root is None:
    #         return res
    #     stack.append((root, 0))
    #     while stack:
    #         head, depth = stack.pop(0)
    #         if len(res) <= depth:
    #             res.append([])
    #         res[depth].append(head.val)
    #         if head.left:
    #             stack.append((head.left, depth+1))
    #         if head.right:
    #             stack.append((head.right, depth+1))
    #     return res

    def levelOrder(self, root: TreeNode) -> List[List[int]]:
        res = []
        def helper(node, depth):
            if node is None:
                return
            if depth >= len(res):
                res.append([])
            res[depth].append(node.val)
            helper(node.left, depth+1)
            helper(node.right, depth+1)
        helper(root, 0)
        return res


if __name__ == "__main__":
    t = stringToTreeNode("[3,9,20,null,null,15,7]")
    print(Solution().levelOrder(t))
