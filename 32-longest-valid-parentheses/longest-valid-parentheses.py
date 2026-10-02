class Solution:
    def longestValidParentheses(self, s: str) -> int:
        # Stack stores indices of characters
        # Initialize with -1 to serve as a base boundary for valid substrings
        stack = [-1]
        max_len = 0
        
        for i, char in enumerate(s):
            if char == '(':
                stack.append(i)
            else:
                stack.pop()
                if not stack:
                    # If stack is empty, push current index as the new boundary
                    stack.append(i)
                else:
                    # Calculate the length of the current valid parentheses substring
                    max_len = max(max_len, i - stack[-1])
                    
        return max_len