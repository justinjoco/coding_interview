'''
letter_combos.py

Time comp: O(3^n*4^m)
Space comp: O(3^n*4^m)

Algorithm:

Backtracking is an algorithm for finding all solutions by exploring all potential candidates. If the solution candidate turns to be not a solution (or at least not the last one), backtracking algorithm discards it by making some changes on the previous step, i.e. backtracks and then try again.

Here is a backtrack function backtrack(combination, next_digits) which takes as arguments an ongoing letter combination and the next digits to check.

If there is no more digits to check that means that the current combination is done.
If there are still digits to check :
Iterate over the letters mapping the next available digit.
Append the current letter to the current combination combination = combination + letter.
Proceed to check next digits : backtrack(combination + letter, next_digits[1:]).

'''

class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
       
        letter_combos = {
            "2":["a","b","c"],
            "3":["d","e","f"],
            "4":["g","h","i"],
            "5":["j","k","l"],
            "6":["m","n","o"],
            "7":["p","q","r","s"],
            "8":["t","u","v"],
            "9":["w","x","y","z"]          
        }
        
        def backtrack(combo, next_digits):
            if len(next_digits) == 0:
                output.append(combo)
            else:
                for letter in letter_combos[next_digits[0]]:
                    backtrack(combo + letter, next_digits[1:])
            
            
        output = []
        if digits:
            backtrack("",digits)
            
        return output