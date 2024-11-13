class Solution:
    def nextPermutation(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        
        # find the first number that's smaller than its next, starting from the back
        # this determines the boundary for the next largest permutation
        # if none found, just reverse the array
        # then find the next largest number of that, and swap it
        # reverse the entire right side of the array
        
        # this is because when getting next lexicographic order, you should start from the back!
        # due to the nature of the list, when we find the pivot, its right side is in decreasing order
        # to change it to lexicographical increasing, we just reverse the right side

        length = len(nums)
      
        # First, find the first element from the right that is smaller than the element next to it.
        pivot = -1
        for i in range(length - 2, -1, -1):
            if nums[i] < nums[i + 1]:
                pivot = i
                break
      
        # If such an element was found, then we can form the next permutation
        if pivot != -1:
            # Now, we find the smallest element greater than the 'pivot', starting from the end
            for j in range(length - 1, pivot, -1):
                if nums[j] > nums[pivot]:
                    # Swap the 'pivot' with this element
                    nums[pivot], nums[j] = nums[j], nums[pivot]
                    break
      
        # Finally, reverse the elements following the 'pivot' (inclusive if pivot is -1)
        # to get the lowest possible sequence with the 'pivot' being the prefix
        nums[pivot + 1:] = reversed(nums[pivot + 1:])
                
