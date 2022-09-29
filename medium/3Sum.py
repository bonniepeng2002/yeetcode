class Solution(object):
    def threeSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        r = set()
        for i in range(0, len(nums)):
            target = -1 * nums[i]
            myDict = {}
            for j in range(i+1, len(nums)):
                if target - nums[j] in myDict:
                    sort = sorted([nums[i], nums[j], target - nums[j]])
                    r.add(tuple(sort))
                myDict[nums[j]] = j
        return list(r)
