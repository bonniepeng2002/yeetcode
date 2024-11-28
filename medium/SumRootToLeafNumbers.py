# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def dfs(self, root: Optional[TreeNode], acc: str) -> str:
        # if non-existent:
        if not root:
            return "0"

        # if leaf, return the path
        if not root.left and not root.right:
            return acc + str(root.val)

        # left child
        leftPath = self.dfs(root.left, acc + str(root.val))
        # right child
        rightPath = self.dfs(root.right, acc + str(root.val))

        return int(leftPath) + int(rightPath)

    def sumNumbers(self, root: Optional[TreeNode]) -> int:
        return int(self.dfs(root, "0"))
        

# this question is asking to run dfs on the graph, keep track of all paths (as numbers) and sum them together
# remember to define each question as an algorithm to help you decide how to proceed
