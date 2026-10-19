class Solution:
    def combine(self, n: int, k: int) -> list[list[int]]:
        result = []
        
        def backtrack(start: int, path: list[int]):
            # If the combination is of length k, add a copy to the result
            if len(path) == k:
                result.append(list(path))
                return
            
            # Optimization: only loop up to n - (k - len(path)) + 1
            needed = k - len(path)
            for i in range(start, n - needed + 2):
                path.append(i)
                backtrack(i + 1, path)
                path.pop()
                
        backtrack(1, [])
        return result