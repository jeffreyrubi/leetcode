class Solution:
    
    def getSum(self, a: int, b: int) -> int:

        # Brutal Force: Loop through the bits pairwise and do the addition with XOR. O(n+1)
        # Optimize: Do 
        # 1. 
        mask = 0xffffffff
        while b & mask:
            carry = (a & b) << 1
            a = a ^ b
            b = carry & mask
        a &= mask  # Force 32-bit
        if a & 0x80000000:
            return ~(a ^ mask)
        return a
    