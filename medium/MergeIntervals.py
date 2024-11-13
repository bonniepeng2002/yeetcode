class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        # sort the intervals, and build it up from the back

        # sort the intervals by start
        # if start2 is < end1, merge them and iteratively accummulate in masterIntervals
        # using quicksort, O(nlogn)

        intervals = sorted(intervals)

        masterIntervals = [intervals[0]]
        for i in range(1, len(intervals)):
            [start1, end1] = intervals[i]
            if start1 <= masterIntervals[-1][1]:
                if end1 > masterIntervals[-1][1]:
                    masterIntervals[-1][1] = end1
            else:
                masterIntervals.append(intervals[i])

        return masterIntervals
            

