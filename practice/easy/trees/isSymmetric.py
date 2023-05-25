from typing import Optional
from collections import deque


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def isMirror(self, tree1, tree2):
        if tree1 is None and tree2 is None:
            return True
        
        if tree1 is None or tree2 is None:
            return False
        
        return tree1.val == tree2.val and \
               self.isMirror(tree1.right, tree2.left) and \
               self.isMirror(tree1.left, tree2.right)

    def isSymmetricIteration(self, root: Optional[TreeNode]) -> bool:
        q = deque()
        q.append(root.left)
        q.append(root.right)

        while len(q):
            print(q)
            tree1 = q.popleft()
            tree2 = q.popleft()

            if tree1 is None and tree2 is None:
                continue

            if tree1 is None or tree2 is None:
                return False

            if tree1.val != tree2.val:
                return False
            q.append(tree1.left)
            q.append(tree2.right)
            q.append(tree1.right)
            q.append(tree2.left)

        return True

    def isSymmetric(self, root: Optional[TreeNode]) -> bool:
        # return self.isMirror(root, root)
        return self.isSymmetricIteration(root)