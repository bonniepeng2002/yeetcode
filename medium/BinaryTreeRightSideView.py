from collections import deque

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        # mathematical way: calculate which indices are on each level, and add the largest index to the list to return

        # traverse the tree level by level
        # this is done with a queue
        # the queue will store the nodes at each level
        # the last node on the level goes into the answer array
        # we'll get the next level nodes and continue

        # 1. populate queue
        # 2. get the rightmost element
        # 3. get the next level nodes into the queue while popping current queue

        if not root:
            return []
            
        queue = deque([root])
        rightSide = []

        while queue:
            rightSide.append(queue[-1].val) # double sided queue (so I can get last element)
            newqueue = deque()
            while queue:
                child = queue.popleft()
                if child: # only add if it's not null
                    if child.left:
                        newqueue.append(child.left)
                    if child.right:
                        newqueue.append(child.right)
            queue = newqueue

        return rightSide
