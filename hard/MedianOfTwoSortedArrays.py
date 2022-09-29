class Solution(object):
    def findMedianSortedArrays(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: float
        """
        
        # this solution is O(m+n), not the required O(log(m+n))
        
        medIndex = (len(nums1)+len(nums2))/2
        
        if (len(nums1) == 0 and len(nums2) == 0): return None
        if (len(nums1) == 0):
            if (len(nums2)%2): return nums2[medIndex]
            else: return float(nums2[medIndex-1]+nums2[medIndex])/2
        if (len(nums2) == 0):
            if (len(nums1)%2): return nums1[medIndex]
            else: return float(nums1[medIndex-1]+nums1[medIndex])/2
        
        current = 0
        prev = 0
        index1 = 0
        index2 = 0
        
        while medIndex != -1:
            medIndex -= 1
            prev = current
            if (index2 >= len(nums2)):
                current = nums1[index1]
                index1 += 1
                continue
            if (index1 < len(nums1) and nums1[index1] < nums2[index2]):
                current = nums1[index1]
                index1 += 1
            else:
                current = nums2[index2]
                index2 += 1
            
        if ((len(nums1)+len(nums2))%2):
            return current
        else:
            return float(current+prev)/2
            
