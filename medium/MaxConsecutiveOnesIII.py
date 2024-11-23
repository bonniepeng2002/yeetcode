class Solution:
    def longestOnes(self, nums: List[int], k: int) -> int:
        # start window at every element, expand until k 0's are flipped
        # if can't flip k 0's, then skip
        # count the one's in the window
        # accummulate max window size

        # iteratively construct a window until there are k 0's
        # count the length of this window

        # maxLen = 0
        # for windowStart in range(0, len(nums)):
        #     windowEnd = windowStart
        #     zeroes = k
        #     while zeroes > 0 and windowEnd < len(nums):
        #         if nums[windowEnd] == 0:
        #             zeroes -= 1
        #         windowEnd += 1
        #     # now that 0s are all used up, find the next 0 and thats the outside of the window
        #     while windowEnd < len(nums) and nums[windowEnd] == 1:
        #         windowEnd += 1
        #     windowSize = windowEnd - windowStart   
        #     maxLen = max(maxLen, windowSize)
            
        # return maxLen

        # ------

        # two pointers to track the largest window with at most k 0's

        left = 0
        maxSize = 0

        numZero = 0
        for i in range(len(nums)):
            if nums[i] == 0:
                numZero += 1

            if numZero > k:
                if nums[left] == 0:
                    numZero -= 1
                left += 1
            
            if numZero <= k:
                maxSize = max(maxSize, i+1 - left)

        return maxSize
