"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':

        # iterate through the list twice
        # first pass creates all the new nodes, with a mapping from old node to new node
        # second pass sets the next and random pointers

        if not head:
            return None

        oldToNew = {} # dictionary with pointers as keys!

        curr = head
        while curr:
            oldToNew[curr] = Node(curr.val)
            curr = curr.next

        curr = head
        while curr:
            # set next
            oldToNew[curr].next = oldToNew.get(curr.next)
            # set random
            oldToNew[curr].random = oldToNew.get(curr.random)
            curr = curr.next

        return oldToNew[head]

        # Pseudocode for the interweaving method

        # first pass of list, create a duplicate of original node A', and put it between old A and old B
        # this is the mapping - old node is connected to new node
        # second pass
        # get old node next and random
        # assign new node's next and random to old node's next.next and random.next (access the new versions)
        # double traversal, but saved on space
        # separate the object for returning

        # if not head:
        #     return None

        # # first pass
        # curr = head
        # while curr:
        #     newNode = Node(curr.val) # create the new node
        #     # interweave new node
        #     tmp = curr.next
        #     newNode.next = tmp
        #     curr.next = newNode

        #     # skip newly created newNode
        #     curr = tmp

        # # second pass, assigning next and random
        # curr = head
        # while curr and curr.next:
        #     oldNext = curr.next.next
        #     oldRandom = curr.random
        #     newNode = curr.next
        #     if oldNext.next:
        #         newNode.next = oldNext.next
        #     if curr.random:
        #         newNode.random = curr.random.next

        # # separate the list
        # newHead = head.next
        # curr = head
        # while curr: # not many checks because I crafted the list to ensure it exists
        #     curr.next.next = curr.next.next.next.next
        #     curr = curr.next.next

        # return newHead
