class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        # start from the back
        # hold an end index of nums1
        # going through both arrays from the end, place the larger of the elements at end index
        # go until one array runs out, then add the rest of the array to the beginning

        # separate cases for if nums1 > nums2: replace nums1[i] with 0

        endidx = len(nums1) - 1

        # if m runs out first, O(m+n)
        # if n runs out first, O(n)
        while m > 0 and n > 0:
            elem1 = nums1[m-1]
            elem2 = nums2[n-1]

            if elem1 > elem2:
                nums1[endidx] = elem1
                nums1[m-1] = 0
                m -= 1
            else:
                nums1[endidx] = elem2
                n -= 1

            endidx -= 1

        if m == 0:
            while n > 0:
                nums1[endidx] = nums2[n-1]
                n -= 1
                endidx -= 1
