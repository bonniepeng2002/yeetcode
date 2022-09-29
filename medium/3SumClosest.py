class Solution(object):
    def threeSumClosest(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        # sort the list in ascending order
        # 3 pointers, one at beginning of list, one iterating from front, one iterating from back
        # calculate the sum of the 3 pointers
        # if the abs of the difference between the sum and target is less than diff of result and target, update result
        # if the sum is less than target, then that means smaller pointer is too far away. Move front pointer up
        # if the sum is larger, then we overshot, and need to move pointer down
        
        nums = sorted(nums)
        i = 0
        result = nums[0] + nums[1] + nums[2]
        for i in range(len(nums) - 2):
            j, k = i+1, len(nums) - 1
            while j < k:
                
                mySum = nums[i] + nums[j] + nums[k]
                
                if mySum == target: return mySum
                
                if abs(target - mySum) < abs(target - result):
                    result = mySum
                
                if mySum < target: j += 1
                elif mySum > target: k -= 1
                    
        return result

