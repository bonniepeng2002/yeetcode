# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def findPath(self, root: 'TreeNode', dest: 'TreeNode') -> list['TreeNode']:

        unvisited = [root]
        visited = []
        parent = {}
        parent[root] = None

        while unvisited:
            curr = unvisited.pop()
            if not curr:
                continue
            visited.append(curr)

            if curr == dest:
                path = [dest]
                parentOfCurr = parent[dest]
                while parentOfCurr:
                    path.append(parentOfCurr)
                    parentOfCurr = parent[parentOfCurr]
                return path # path from destination to root

            if curr.left not in visited:
                parent[curr.left] = curr
                unvisited.append(curr.left)
            if curr.right not in visited:
                parent[curr.right] = curr
                unvisited.append(curr.right)

        return []


    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        # DFS to find the path to q and p
        # keep track of its parents, and then find the common parent that's the last in the array of parents

        if not root:
            return None

        pathToQ = self.findPath(root, q)
        pathToP = self.findPath(root, p)

        # find first common element
        setQ = set(pathToQ)
        for i in pathToP:
            if i in setQ:
                return i

        return None
