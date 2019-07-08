"""
Word Break

Given a non-empty string s and a dictionary wordDict containing a list of non-empty words, determine if s can be segmented into a space-separated sequence of one or more dictionary words.

Note:

The same word in the dictionary may be reused multiple times in the segmentation.
You may assume the dictionary does not contain duplicate words.
Example 1:

Input: s = "leetcode", wordDict = ["leet", "code"]
Output: true
Explanation: Return true because "leetcode" can be segmented as "leet code".
Example 2:

Input: s = "applepenapple", wordDict = ["apple", "pen"]
Output: true
Explanation: Return true because "applepenapple" can be segmented as "apple pen apple".
             Note that you are allowed to reuse a dictionary word.
Example 3:

Input: s = "catsandog", wordDict = ["cats", "dog", "sand", "and", "cat"]
Output: false

Algorithm: Dynamic programming to remember the solutions to previous string breaking
Create a dp array that's of length n+1, all elements as False
Set first element as True bc null strings are part of the dictionary
Let i represent the forward index, and j be the following index
For each index i from 0 to n+1,
    For each index of j from 0 to i
        If the string from 0 to j can be broken up
            If the string indexed from to j to i is within the word dictionary
                We now know that this new string indexed from 0 to i can be broken up
                Break from inner loop
Return the boolean of the dp at index n


Time complexity: O(n^2): Goes through list at least n times
Space complexity: O(n): DP array to remember previous solutions



"""


class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        
        dict_set = set(wordDict) 
        n = len(s)
        answer = [False] * (n+1)
        answer[0] = True
        for i in range(n+1):
            for j in range(i, -1, -1):
                if answer[j] and s[j:i] in dict_set:
                    answer[i] = True
                    break
            
        return answer[n]