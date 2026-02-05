from typing import List

class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        if not digits:
            return []
        
        phone_map = {
            '2': 'abc', '3': 'def', '4': 'ghi', '5': 'jkl',
            '6': 'mno', '7': 'pqrs', '8': 'tuv', '9': 'wxyz'
        }

        def backtrack(index: int):
            nonlocal digits

            if index < len(digits) - 1:
                combinations = []
                next_combinations = backtrack(index+1)
                for letter in phone_map[digits[index]]:
                     for nc in next_combinations:
                        combinations.append(letter + nc)
                return combinations 
            else:
                # last digit
                return list(phone_map[digits[index]])
        
        return backtrack(0)