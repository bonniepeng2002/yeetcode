# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        # every node has the chance to be root
        # at each node, calculate the longest path crossing that node
            # this is height of its left and right subtrees
        # find the max between all nodes

        # IDEA:
        # find the max height starting from each root's subtrees
        # add them together to find the diameter
        # do this for every node that can be a root

        # max height starting from node
        def height(node: Optional[TreeNode], diameter) -> int:
            if not node:
                return 0

            # get left and right heights
            left = height(node.left, diameter)
            right = height(node.right, diameter)

            # calculate diameter, and update if needed
            diameter[0] = max(diameter[0], left + right)

            return max(left, right) + 1
        
        diameter = [0]
        height(root, diameter)
        return diameter[0]


