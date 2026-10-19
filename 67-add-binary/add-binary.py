class Solution:
    def addBinary(self, a: str, b: str) -> str:
        i, j = len(a) - 1, len(b) - 1
        carry = 0
        result = []
        
        while i >= 0 or j >= 0 or carry:
            total = carry
            
            if i >= 0:
                total += int(a[i])
                i -= 1
            if j >= 0:
                total += int(b[j])
                j -= 1
                
            # Append the current bit (total % 2) and update the carry (total // 2)
            result.append(str(total % 2))
            carry = total // 2
            
        # Since we added digits from right to left, reverse the result list and join
        return "".join(reversed(result))