class Solution(object):
    def rob(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        evenSum = 0;
        oddSum = 0;
        if len(nums) == 0: return 0
        for i in range(0,len(nums)):
            if i%2 == 0:
                evenSum = max(evenSum + nums[i], oddSum)
            else:
                oddSum = max(evenSum, oddSum + nums[i])

        return max(evenSum, oddSum)
            
        
