"""
Merge Intervals

Given a collection of intervals, merge all overlapping intervals.

Example 1:

Input: [[1,3],[2,6],[8,10],[15,18]]
Output: [[1,6],[8,10],[15,18]]
Explanation: Since intervals [1,3] and [2,6] overlaps, merge them into [1,6].
Example 2:

Input: [[1,4],[4,5]]
Output: [[1,5]]
Explanation: Intervals [1,4] and [4,5] are considered overlapping.

Algorithm:
Sort the given list with the start interval as the key
Initialize an empty merged list
For each interval within the sorted interval list:
	Add the interval into the merged list if the list is empty or the current interval begins later than the latest interval's end in the merged list
	Otherwise, the latest interval's end value is the higher value between the current interval's end and the latest interval's
Return the merged list

Time complexity: O(nlogn) : sorting
Space: O(n): Because of the merged list
"""



class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        sorted_list = sorted(intervals, key= lambda be: be[0])
        result = []
        for interval in sorted_list:         
            if not result or result[-1][1] < interval[0]:
                result.append(interval)
            else:
                result[-1][1] = (max(result[-1][1], interval[1]))
        return result