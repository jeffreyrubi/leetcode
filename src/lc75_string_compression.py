from typing import List

class Solution:
    def compress(self, chars: List[str]) -> int:
        last_c = None
        last_count = 0
        next_pos = 0

        for c in chars:
            if c == last_c:
                last_count += 1
            else:
                # Add len(last_count+1) to result
                if last_count > 1:
                    for digit in str(last_count):
                        chars[next_pos] = digit
                        next_pos += 1
                
                # Reset the count
                last_c = c
                last_count = 1

                # update chars and advance the next_pos
                chars[next_pos] = c
                next_pos += 1

        # Add the last_count for the last character
        if last_count > 1:
            for digit in str(last_count):
                chars[next_pos] = digit
                next_pos += 1
        
        return next_pos

            