# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rangeSumBST(self, root: Optional[TreeNode], low: int, high: int) -> int:
        # sum everything as the right children of the low, and the left children of the high

        # root == low, low + recursion on the right child
        # root == high, high + recursion on the left child
        # root in between, root + recursion on left and recursion on right
        # root < low, recursion on right child
        # root > high, recursion on left child
        # return 0

        # worst case: O(n)
        # average case: O(nodes between low and high) or O(logn)

        if not root:
            return 0

        if root.val == low:
            return low + self.rangeSumBST(root.right, low, high)
        elif root.val == high:
            return high + self.rangeSumBST(root.left, low, high)
        elif low < root.val < high:
            return root.val + self.rangeSumBST(root.right, low, high) + self.rangeSumBST(root.left, low, high)
        elif root.val < low:
            return  + self.rangeSumBST(root.right, low, high)
        elif root.val > high:
            return  + self.rangeSumBST(root.left, low, high)
        else:
            return 0
