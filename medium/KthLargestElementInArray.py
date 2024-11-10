class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        # find and delete max number k-1 times, return on kth time

        # too slow
        # for i in range(k-1):
        #     maximum = max(nums) # O(n)
        #     nums.remove(maximum) # O(n)

        # return max(nums)

        # faster solution, use a min heap
        from heapq import heappop, heappush, heapify

        # create heap, O(logn)
        heapify(nums)

        for i in range(len(nums)-k):
            heappop(nums)

        return nums[0]

