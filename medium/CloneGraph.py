"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

from typing import Optional
class Solution:
    # keep track of what has been cloned
    # explore graph with its neighbours, and clone what hasn't been cloned
    # BFS with a queue, replace visited with cloned

    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        if not node:
            return None

        queue = deque([node])
        cloned = {}

        while queue:
            curr = queue.popleft()

            # clone self if not cloned
            if curr not in cloned:
                cloned[curr] = Node(curr.val, [])

            # explore neighbours
            for neighbor in curr.neighbors:
                if neighbor not in cloned:
                    cloned[neighbor] = Node(neighbor.val, [])
                    queue.append(neighbor)
                cloned[curr].neighbors.append(cloned[neighbor])

        return cloned[node]
