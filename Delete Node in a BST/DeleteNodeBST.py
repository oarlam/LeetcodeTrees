# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def deleteNode(self, root, key: int):
        dummy = TreeNode(left = root)
        parent = dummy
        target = root

        while target and target.val != key:
            parent = target
            if key < target.val:
                target = target.left
            else:
                target = target.right

        if target is None:
            return root

        replacement = target.right if target.right else target.left

        if parent.right is target:
            parent.right = replacement
        else:
            parent.left = replacement

        if target.right and target.left:
            cur = target.right
            while cur.left is not None:
                cur = cur.left
            cur.left = target.left
        return dummy.left
