from itertools import groupby

class Solution:
    def countAndSay(self, n: int) -> str:
        current = "1"
        
        for _ in range(n - 1):
            next_seq = []
            # Group consecutive identical characters and count their frequencies
            for char, group in groupby(current):
                count = sum(1 for _ in group)
                next_seq.append(str(count))
                next_seq.append(char)
            current = "".join(next_seq)
            
        return current