from utils import stringToTreeNode, TreeNode


class Solution:
    def maxDepth(self, root: TreeNode) -> int:
        if root is None:
            return 0
        return 1 + max(self.maxDepth(root.left), self.maxDepth(root.right))

    # def maxDepth(self, root: TreeNode) -> int:
    #     if root is None:
    #         return 0
    #     res = 0
    #     def helper(node, depth):
    #         nonlocal res
    #         if node is None:
    #             return
    #         res = max(depth, res)
    #         if node.left:
    #             helper(node.left, depth+1)
    #         if node.right:
    #             helper(node.right, depth+1)
    #     helper(root, 1)
    #     return res


if __name__ == "__main__":
    t = stringToTreeNode("[3,9,20,null,null,15,7]")
    print(Solution().maxDepth(t))
