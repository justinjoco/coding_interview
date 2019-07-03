'''
Container With Most Water

Given n non-negative integers a1, a2, ..., an , where each represents a point at coordinate (i, ai). n vertical lines are drawn such that the two endpoints of line i is at (i, ai) and (i, 0). Find two lines, which together with x-axis forms a container, such that the container contains the most water.

Note: You may not slant the container and n is at least 2.


The above vertical lines are represented by array [1,8,6,2,5,4,8,3,7]. In this case, the max area of water (blue section) the container can contain is 49.


Example:

Input: [1,8,6,2,5,4,8,3,7]
Output: 49

Algorithm: Sliding window/ two pointers
Set left and right pointers to beginning and end of list
Initalize max area as the distance between left and right and the minimum between the two heights 
While left and right pointers haven't passed each other:
    If the height at the left pointer is lower than the height at the right
        Move left pointer once to the right
    Otherwise,
        Move right pointer once to the left
    Set max area as the max between the current max area and the rectangle created by the two pointers and their respective heights 
Return max area

Time complexity: O(n): Go through list only once
Memory complexity: O(1) : No extra space for data structures allocated
'''


class Solution:
    def maxArea(self, height: List[int]) -> int:
        left = 0
        right = len(height) - 1
        max_area = min(height[left], height[right]) * (right - left)
        while (left < right):
            if height[left] < height[right]:
                left +=1
            else:
                right-=1
            max_area = max(max_area, min(height[left], height[right]) * (right - left))     
            
            
            
        return max_area
        