from utils import TreeNode, stringToTreeNode, prettyPrintTree
from typing import List


class Solution:
    def levelOrder(self, root: TreeNode) -> List[List[int]]:
        res = []
        def helper(node, depth):
            if node is None:
                return
            if depth >= len(res):
                res.append([])
            if depth % 2 == 0:
                res[depth].append(node.val)
            else:
                res[depth].insert(0, node.val)
            helper(node.left, depth+1)
            helper(node.right, depth+1)
        helper(root, 0)
        return res


if __name__ == "__main__":
    t = stringToTreeNode("[3,9,20,null,null,15,7]")
    print(Solution().levelOrder(t))
