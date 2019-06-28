"""
Longest Palindromic Substring

Given a string s, find the longest palindromic substring in s. You may assume that the maximum length of s is 1000.

Example 1:

Input: "babad"
Output: "bab"
Note: "aba" is also a valid answer.
Example 2:

Input: "cbbd"
Output: "bb"

Algorithm:
Iterate through string
Expand around the center for each letter and pair
    Check that right part of the string mirrors the left part of the string
    Record the length of each iteration of expandAroundCenter
    Keep the longer length
    Set the starting and ending indices of the string based on longer length
Return substring with given starting and ending indices

"""
class Solution:
    def longestPalindrome(self, s: str) -> str:
        if (s is None or len(s) <1): return ""
        start = 0
        end = 0
        for i, val in enumerate(s):
            len1 = self._expandAroundCenter(s, i,i)
            len2 = self._expandAroundCenter(s, i,i+1)
            length = max(len1,len2)
            
            if (length > end-start):
                start = i - (length-1)//2
                end = i + length//2
        
        return s[start: end+1]
        
        
    def _expandAroundCenter(self, s:str, left:int, right:int):
        
        L = left
        R = right
        while (L >=0 and R < len(s) and s[L] == s[R]):
            L-=1
            R+=1
        return R - L - 1