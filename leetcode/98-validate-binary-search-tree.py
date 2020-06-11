from utils import TreeNode, stringToTreeNode, prettyPrintTree


class Solution:
    def isValidBST(self, root: TreeNode) -> bool:
        def helper(node, minVal, maxVal):
            if node is None:
                return True
            if node.val >= maxVal or node.val <= minVal:
                return False
            return helper(node.left, minVal, node.val) and helper(node.right, node.val, maxVal)
        return helper(root, float('-inf'), float('inf'))

    def inorder_traverse(self, root: TreeNode) -> bool:
        """ In order traverse the binary search tree will 
        get a sorted list.
        """
        lst = []
        def helper(node):
            if node is None:
                return 
            if node.left:
                helper(node.left)
            lst.append(node.val)
            if node.right:
                helper(node.right)
        helper(root)
        for i in range(len(lst) - 1):
            if lst[i] >= lst[i+1]:
                return False
        return True


if __name__ == "__main__":
    t = stringToTreeNode("[]")
    print(Solution().isValidBST(t))  # True
    t = stringToTreeNode("[10,5,15,null,null,6,20]")
    print(Solution().isValidBST(t))  # False
    t= stringToTreeNode("[2,1,3]")
    print(Solution().isValidBST(t))  # True
    t= stringToTreeNode("[5,1,4,null,null,3,6]")
    print(Solution().isValidBST(t))  # False
