from typing import List

class Solution:

    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        groups = {}

        for item in strs:
            sorted_item = ''.join(sorted(item.lower()))
            if sorted_item in groups:
                groups[sorted_item].append(item)
            else:
                groups[sorted_item] = [item]
            
        return list(groups.values())