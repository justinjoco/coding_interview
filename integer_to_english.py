"""
Integer to English Words

Convert a non-negative integer to its english words representation. Given input is guaranteed to be less than 231 - 1.

Example 1:

Input: 123
Output: "One Hundred Twenty Three"
Example 2:

Input: 12345
Output: "Twelve Thousand Three Hundred Forty Five"
Example 3:

Input: 1234567
Output: "One Million Two Hundred Thirty Four Thousand Five Hundred Sixty Seven"
Example 4:

Input: 1234567891
Output: "One Billion Two Hundred Thirty Four Million Five Hundred Sixty Seven Thousand Eight Hundred Ninety One"

Algorithm:
Break the number into chunks of 3 digits
For each chunk:
    Parse the chunk
    Add the place label (billion, million, thousand, none)
Accumulate the strings parsed from the chunks
Add spaces if a previous chunk returns a valid parsed string (ie not empty)

Time complexity: O(n): goes through number once
Space Complexity: O(1) due to constant size of map
"""



from collections import defaultdict
class Solution:
    def numberToWords(self, num: int) -> str:
        if num == 0:
            return "Zero"
        mult_by_1000 = 0
        map = defaultdict(int)
        
        while num >0:
            chunk = num % 1000
            if mult_by_1000 == 0:
                map["Ones"] = chunk
            elif mult_by_1000 == 1:
                map["Thousand"] = chunk
            elif mult_by_1000 == 2:
                map["Million"] = chunk
            else:
                map["Billion"] = chunk
            
            num //= 1000
            mult_by_1000 +=1
    
        billion = self.parse(map["Billion"], "Billion")
        million = self.parse(map["Million"], "Million") 
        thousand = self.parse(map["Thousand"], "Thousand")
        ones = self.parse(map["Ones"], "Ones")
                          
        result = ""
        if billion:
            result += billion
        if million:
            result += " " if result else ""
            result += million
        if thousand:
            result += " " if result else ""
            result += thousand
        if ones:
            result += " " if result else ""
            result += ones
            
        return result
    
    def parse(self, chunk, key):
        
        if chunk == 0 and key != "Ones":
            return ""
        
        ones_map = {0: "",
                    1: "One",
                    2: "Two",
                    3: "Three",
                    4: "Four",
                    5: "Five",
                    6: "Six",
                    7: "Seven",
                    8: "Eight",
                    9: "Nine"
                   }     
        less_than_twenty_map = {
            10: "Ten",
            11: "Eleven",
            12: "Twelve",
            13: "Thirteen",
            14: "Fourteen",
            15: "Fifteen",
            16: "Sixteen",
            17: "Seventeen",
            18: "Eighteen",
            19: "Nineteen"
        }
        tens_map = {
            2: "Twenty",
            3: "Thirty", 
            4: "Forty",
            5: "Fifty", 
            6: "Sixty",
            7: "Seventy", 
            8: "Eighty",
            9: "Ninety"    
        }
        
        ret_string = ""
        if chunk >= 100:
            ret_string += ones_map[chunk//100] + " Hundred " 
        if chunk%100 >= 10 and chunk%100 < 20:
            ret_string += less_than_twenty_map[chunk%100]   
        elif chunk%100 >= 20 and chunk%10 > 0:
            ret_string += tens_map[chunk%100//10] + " " + ones_map[chunk%10]
        elif chunk%100 >= 20:
            ret_string += tens_map[chunk%100//10]
        else:
            ret_string += ones_map[chunk%10]
        
        ret_string = ret_string.strip()
        if key == "Ones":
            return ret_string
        else:
            return ret_string + " " + key
        
        