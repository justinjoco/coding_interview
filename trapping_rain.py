"""
Trapping Rain Water

Given n non-negative integers representing an elevation map where the width of each bar is 1, compute how much water it is able to trap after raining.

The above elevation map is represented by array [0,1,0,2,1,0,1,3,2,1,2,1]. In this case, 6 units of rain water (blue section) are being trapped. Thanks Marcos for contributing this image!

Example:

Input: [0,1,0,2,1,0,1,3,2,1,2,1]
Output: 6

Algorithm:
Two pointers: left and right
Left starts at 0; Right starts at the end
Intialize the max heights of the left and right as 0
While the left and right pointers haven't crossed each other
    If the height at the left pointer is greater than the left's max height
        Update left max height to that of the left pointer
    If the height at the right pointer is greater than the right's max height
        Update right max height to that of the right pointer
    If the left's max height is less than the right's max height
        Add the difference between the left's max height and the left pointer's current height to the answer
        Move left pointer one step to the right
    Otherwise,
        Add the difference between the right's max height and the right pointer's current height to the answer
        Move right pointer one step to the left
Return answer
"""

class Solution:
    def trap(self, height: List[int]) -> int:
        left = 0
        right = len(height) - 1
        water = 0
        left_max = 0
        right_max = 0
        while (left < right):
            if height[left] >=left_max:
                left_max = height[left]
            if height[right] >=right_max:
                right_max = height[right]
            if left_max < right_max:
                water += max(0, left_max - height[left])
                left+=1
            else:
                water += max(0, right_max - height[right])
                right-=1
                
        return water