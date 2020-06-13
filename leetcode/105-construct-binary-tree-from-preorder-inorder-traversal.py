from typing import List
from utils import TreeNode, prettyPrintTree


class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> TreeNode:
        if len(preorder) == 0:
            return None
        mid = inorder.index(preorder[0])
        t = TreeNode(preorder[0])
        t.left = self.buildTree(preorder[1:mid+1], inorder[:mid])
        t.right = self.buildTree(preorder[mid+1:], inorder[mid+1:])
        return t

if __name__ == "__main__":
    preorder = [3,9,20,15,7]
    inorder = [9,3,15,20,7]
    prettyPrintTree(Solution().buildTree(preorder, inorder))
