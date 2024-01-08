# ========= ATTEMPT FROM Dec 07, 2022 ========= #

# Definition for a binary tree node.
from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def rangeSumBST(self, root: Optional[TreeNode], low: int, high: int) -> int:
        if not root:
            return 0
        elif root.val < low:
            return self.rangeSumBST(root.right, low, high)
        elif root.val > high:
            return self.rangeSumBST(root.left, low, high)
        return root.val + self.rangeSumBST(root.left, low, high) + self.rangeSumBST(root.right, low, high)


# ========= ATTEMPT FROM Jan 08, 2024 (Daily Question) ========= #

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rangeSumBST(self, root: Optional[TreeNode], low: int, high: int, sum=0) -> int:
        if root.val is None:
            return sum
        if low <= root.val <= high:
            sum += root.val

        if root.left is not None:
            sum = self.rangeSumBST(root.left, low, high, sum)
        if root.right is not None:
            sum = self.rangeSumBST(root.right, low, high, sum)
                
        return sum

        