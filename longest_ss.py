'''
Longest Substring Without Repeating Characters

Given a string, find the length of the longest substring without repeating characters.

Example 1:

Input: "abcabcbb"
Output: 3 
Explanation: The answer is "abc", with the length of 3. 
Example 2:

Input: "bbbbb"
Output: 1
Explanation: The answer is "b", with the length of 1.
Example 3:

Input: "pwwkew"
Output: 3
Explanation: The answer is "wke", with the length of 3. 
             Note that the answer must be a substring, "pwke" is a subsequence and not a substring.

Algorithm: Sliding Window
Set longest to 1
Initialize indices i and j
While i and j don't exceed the string length:
    If character at index j is not seen yet
        Add character to seen set
        Increment j
        Update longest if the gap between j and i is larger
    Otherwise
        Remove the character in the set whose value is equal to the character in s at point i (a window length away from j)
        Increment i

'''


class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if s == "" or s == None:
            return 0
        
        
        seen = set()
        longest = 1
        window_begin = 0
        window_end = 0
        while (window_begin < len(s) and window_end < len(s)):
            if s[window_end] not in seen:          
                seen.add(s[window_end])
                window_end+=1
                
                longest = max(longest, window_end-window_begin)
                
            else:
                seen.remove(s[window_begin])
                window_begin+=1
                
        return longest