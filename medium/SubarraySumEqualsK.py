class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        
        # for every window subarray from beginning, store the sum in a map
        # count the number of windows whose sums are k
        # count the number of windows whose sums are k when another window sum is subtracted from current sum
        # window[i] - window[j] = k means window[i] - k = window[j]

        windowMap = {
            0: nums[0]
        }

        for i in range(1, len(nums)):
            window = nums[0:i]
            # windowMap[i] = sum(window)
            windowMap[i] = windowMap[i-1] + nums[i]

        number = 0

        for i in range(0, len(nums)):
            if windowMap[i] == k:
                number += 1
            for j in range(0, i):
                if windowMap[i] - windowMap[j] == k:
                    number += 1

        return number

        
