
"""
Compare Version Numbers

Compare two version numbers version1 and version2.
If version1 > version2 return 1; if version1 < version2 return -1;otherwise return 0.

You may assume that the version strings are non-empty and contain only digits and the . character.

The . character does not represent a decimal point and is used to separate number sequences.

For instance, 2.5 is not "two and a half" or "half way to version three", it is the fifth second-level revision of the second first-level revision.

You may assume the default revision number for each level of a version number to be 0. For example, version number 3.4 has a revision number of 3 and 4 for its first and second level revision number. Its third and fourth level revision number are both 0.

Time complexity: O(n) -> Goes through each list once
Memory complexity: O(n) -> Makes auxiliary lists

Algorithm:
Turn each string into a list of numbers, with '.' as delimiter
Get the length difference between the lists
Zero pad the smaller list until it's the same length as the bigger one
Compare the list values
"""


class Solution:
    def compareVersion(self, version1: str, version2: str) -> int:
        list1 = [int(num) for num in version1.split(".")]
        list2 = [int(num) for num in version2.split(".")]

        diff = len(list2) - len(list1)
        if diff > 0:
            list1+=[0]*diff
        else:
            list2+= [0]*abs(diff)
        
        if list1 > list2:
            return 1
        elif list1 < list2:
            return -1
        else:
            return 0