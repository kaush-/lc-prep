from typing import Optional
import math


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def inorder(self, root: Optional[TreeNode]) -> bool:
        if not root:
            return True

        if not self.inorder(root.left):
            return False

        if root.val <= self.prev:
            return False
        self.prev = root.val

        return self.inorder(root.right)

    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        self.prev = -math.inf
        return self.inorder(root)