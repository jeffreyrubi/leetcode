from typing import List

class Solution:
    def suggestedProducts(self, products: List[str], searchWord: str) -> List[List[str]]:
        # sort the product in alphabetical order => O(nlogn)
        products.sort()

        s = 0
        l = len(products) - 1
        result = []

        # Go through the searchWord by character and update small and large
        for i in range(len(searchWord)):
            res = []
            # update s to the earliest match
            while s <= l and (i >= len(products[s]) or searchWord[i] != products[s][i]):
                s += 1
            while s <= l and (i >= len(products[l]) or searchWord[i] != products[l][i]):
                l -= 1
            
            for i in range(s, min(l+1, s+3)):
                res.append(products[i])
            result.append(res)
        return result