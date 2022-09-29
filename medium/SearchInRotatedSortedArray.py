class Solution(object):
    def search(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        # perform binary search, calculating index in each recursion
        if target not in nums: return -1
        
        n = len(nums)
        res = 0
        
        if target in nums[:n/2]:
            res = self.binarySearch(nums[:n/2], target)
        else:
            res = n/2 + self.binarySearch(nums[n/2:], target)
            
        return res - 1
            
    def binarySearch(self, nums, target):
        print(nums)
        if target == nums[0]: return 1
        if target in nums[:len(nums)/2]:
            return self.binarySearch(nums[:len(nums)/2], target)
        else:
            return len(nums)/2 + self.binarySearch(nums[len(nums)/2:], target)
        
    
