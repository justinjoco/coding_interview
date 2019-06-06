'''
valid_parenthesese.py

Algorithm:
Break string into a char list
Iterate through char list:
    If bracket is open, add bracket to stack
    If bracket is closed, pop bracket from stack
        If popped open bracket is not the closed bracket's respective open bracket, return False
        If stack is empty, return False

If stack is not empty, return False
Else, return True

Time complexity: O(n)
Space complexity O(n)
'''

class Solution:
    def isValid(self, s: str) -> bool:
        bracket_list = list(s)
        
        bracket_map = {"{":"}", "[":"]", "(":")"}
        
        open_set = set(bracket_map.keys())
        closed_set = set(bracket_map.values())
    
        stack = []
        for bracket in bracket_list:
            if bracket in open_set:
                stack.append(bracket)
            else:
                if stack:
                    open_bracket = stack.pop()
                    if bracket_map[open_bracket] != bracket:
                        return False
                else:
                    return False
                
        if stack:
            return False
        else:
            return True