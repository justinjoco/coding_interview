"""
Product of Array Except Self

Given an array nums of n integers where n > 1,  return an array output such that output[i] is equal to the product of all the elements of nums except nums[i].

Example:

Input:  [1,2,3,4]
Output: [24,12,8,6]

Algorithm: 
Create running lists of the product of elements to the left and right of a given index
For each index from 1 to the length of nums:
    left[index] = left[index - 1] * nums[i-1]
FOr each index from the length of nums-1 to 0:
    right[index] = right[index+1] * nums[i+1]
For each index of the answer list
    Multiply the left[index] and right[index]
Return the answer list

Time complexity: O(n) -> goes through input list twice
Memory complexity O(n) -> auxiliary left and right arrays
"""


class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        L, R, answer = [0]*len(nums), [0]*len(nums), [0]*len(nums)
        length = len(nums)
        L[0] = 1
        for i in range(1, length):
            L[i] = nums[i-1]*L[i-1]
            
        R[length-1] = 1
        for i in reversed(range(length-1)):
            R[i] = R[i+1] * nums[i+1]
            
        for i in range(length):
            answer[i] = L[i] * R[i]
        
        return answer        