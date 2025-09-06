
class Solution:
    
    def lengthOfLongestSubstring(self, s: str) -> int:
        return self.sliding_window(s)

    def sliding_window(self, s:str) -> int:
        last_seen = {}
        max_length = 0
        left = 0    

        for right, c in enumerate(s):
            if c in last_seen and left <= last_seen[c]:
                # advance left
                left = last_seen[c] + 1
            
            # mark last seen position
            last_seen[c] = right
            max_length = max(max_length, right-left+1)

        return max_length

    def version_1(self, s: str) -> int:
        if len(s) < 2:
            return len(s)
        
        cur_startpos = 0
        substring_max_length = 1

        while cur_startpos < len(s)-1:
            cur_endpos = cur_startpos

            # while there are still extra character to check
            while cur_endpos < (len(s) - 1):
                cur_substring = s[cur_startpos:cur_endpos+1]
                cur_substring_map = {c: i+cur_startpos for i, c in enumerate(cur_substring)}

                extra_c = s[cur_endpos+1]
                if extra_c in cur_substring_map:
                    # advance next possible startpos
                    cur_startpos = cur_substring_map[extra_c] + 1

                    # reset cur_endpos
                    cur_endpos = cur_startpos
                else:
                    # increment cur_endpos
                    cur_endpos = cur_endpos + 1
                    substring_max_length = max(substring_max_length, len(cur_substring)+1)

            cur_startpos = cur_startpos + 1

        return substring_max_length

