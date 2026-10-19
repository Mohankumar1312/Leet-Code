class Solution:
    def combinationSum2(self, candidates: list[int], target: int) -> list[list[int]]:
        candidates.sort()
        result = []
        
        def backtrack(start: int, current_sum: int, path: list[int]):
            if current_sum == target:
                result.append(list(path))
                return
            
            for i in range(start, len(candidates)):
                # Skip duplicates at the same recursion level
                if i > start and candidates[i] == candidates[i - 1]:
                    continue
                
                # If adding the current candidate exceeds the target, stop exploring further
                if current_sum + candidates[i] > target:
                    break
                
                path.append(candidates[i])
                # Each number can only be used once, so we pass i + 1
                backtrack(i + 1, current_sum + candidates[i], path)
                path.pop()
                
        backtrack(0, 0, [])
        return result