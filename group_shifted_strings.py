"""
Group Shifted Strings

Given a string, we can "shift" each of its letter to its successive letter, for example: "abc" -> "bcd". We can keep "shifting" which forms the sequence:

"abc" -> "bcd" -> ... -> "xyz"
Given a list of strings which contains only lowercase alphabets, group all strings that belong to the same shifting sequence.

Example:

Input: ["abc", "bcd", "acef", "xyz", "az", "ba", "a", "z"],
Output: 
[
  ["abc","bcd","xyz"],
  ["az","ba"],
  ["acef"],
  ["a","z"]
]

Time complexity: O(nk) ; n = num of strings, k = max length of string
Memory complexity: O(k)

Algorithm:
For each each string
	Get the circular differences between each adjacent character in string
	Map tuple of the circular differences to a list of strings

Return the map's values
"""

from collections import defaultdict
class Solution:
    def groupStrings(self, strings: List[str]) -> List[List[str]]:
        map = defaultdict(list)
        
        for string in strings:
            if len(string) <=1:
                map[(27)].append(string)
            else:
                diffs = []
                for i in range(len(string)-1):
                    diff = (ord(string[i])  - ord(string[i+1])) %26 
                    diffs.append(diff)
                map[tuple(diffs)].append(string)
                    
        
        
        return list(map.values())