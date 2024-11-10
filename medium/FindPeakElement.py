class Solution:
    def findPeakElement(self, nums: List[int]) -> int:
        def isPeak(idx):
            if idx - 1 >= 0 and idx + 1 < len(nums):
                if nums[idx-1] < nums[idx] and nums[idx] > nums[idx+1]:
                    return True
            elif idx - 1 < 0 and nums[idx] > nums[idx+1]:
                return True
            elif idx + 1 >= len(nums) and nums[idx] > nums[idx-1]:
                return True
        # the only way to reach log n is to actually divide the problem in half each time

        # Use binary search. Check if the middle element is a peak.
        # If not, and it's greater than the right element, then peak is on the left
        # Similar for right

        if len(nums) == 1:
            return 0
        elif len(nums) == 2:
            if nums[0] > nums[1]:
                return 0
            else:
                return 1

        mididx = (len(nums) - 1) // 2
        if isPeak(mididx):
            return mididx
        elif nums[mididx] > nums[mididx+1]:
            return self.findPeakElement(nums[:mididx+1])
        else:
            return mididx + self.findPeakElement(nums[mididx:])
