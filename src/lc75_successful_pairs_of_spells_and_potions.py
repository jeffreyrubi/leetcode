from typing import List

class Solution:
    def successfulPairs(self, spells: List[int], potions: List[int], success: int) -> List[int]:
        # Sort the potions array
        # Do binary search until l==r, check success to see if it should be included.
        # Update the count with l/l+1 -> potions
        # Do that for all spells

        total = []
        potions.sort()
        for spell in spells:
            l, r = 0, len(potions) - 1
            while l < r:
                m = (r + l) // 2

                if spell * potions[m] >= success:
                    # look for smaller m
                    r = m - 1
                else:
                    # look for bigger m
                    l = m + 1

            if spell * potions[l] >= success:
                # count l -> end
                total.append(len(potions) - l)
            else:
                # exclude l -> end
                if l == len(potions) - 1:
                    total.append(0)
                else:
                    total.append(len(potions) - (l + 1))
        return total

            
