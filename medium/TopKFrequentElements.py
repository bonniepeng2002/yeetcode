import heapq

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        # maintain dictionary with count of elements
        # turn dictionary into a heap and pop off top k elements of the heap

        elements = {}
        for i in nums:
            if i not in elements:
                elements[i] = 1
            else:
                elements[i] += 1

        # remember to invert values for a maxheap
        heap = [(-value, key) for (key, value) in elements.items()]
        # heapifies by first element
        heapq.heapify(heap)

        # return the top k
        res = heapq.nsmallest(k, heap)
        return [item[1] for item in res]
