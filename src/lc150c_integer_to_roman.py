class Solution:
    def intToRoman(self, num: int) -> str:
        # Greedy approach: use largest values first
        # Include subtractive cases (4, 9, 40, 90, etc.)
        # Time: O(1), Space: O(1) - bounded by max num (3999)
        
        val_symbols = [
            (1000, "M"),
            (900, "CM"),
            (500, "D"),
            (400, "CD"),
            (100, "C"),
            (90, "XC"),
            (50, "L"),
            (40, "XL"),
            (10, "X"),
            (9, "IX"),
            (5, "V"),
            (4, "IV"),
            (1, "I"),
        ]
        
        result = []
        for val, symbol in val_symbols:
            while num >= val:
                result.append(symbol)
                num -= val
        
        return "".join(result)