'''
Two Sum

Given an array of integers, return indices of the two numbers such that they add up to a specific target.
You may assume that each input would have exactly one solution, and you may not use the same element twice.

Example:
Given nums = [2, 7, 11, 15], target = 9,
Because nums[0] + nums[1] = 2 + 7 = 9,
return [0, 1].
'''
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        
        #Create map that maps complement to indices
        comp_map = {}
        
        #Keep tracking of complements already seen
        seen = set()
        
        #Go through list and create map that maps complement to a set of indices
        for ind, val in enumerate(nums):
            comp = target - val
            if comp not in seen:
                seen.add(comp)
                comp_map[comp] = set([ind])
            else:
                comp_map[comp].add(ind)
            
        #Go through given list again
        #Check if a number in the list is a key in the comp map.
        #Return the number's index in the list and the complement's index from comp map (return two indices if a number's complement is the same number itself)
        for ind, val in enumerate(nums):
            if val in comp_map.keys():
                pop = comp_map[val].pop()
                if pop == ind:
                    if len(comp_map[val]) >0: return [pop, comp_map[val].pop()]
                else:
                    return [ind, pop]
                           
        #Return empty list if there's no complement              
        return []
