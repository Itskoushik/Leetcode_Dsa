from typing import List

class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        res = []  # This will store the final list of valid combinations
        
        def dfs(i, cur, total):
            """
            Depth-First Search (DFS) recursive function to find combinations.
            
            Parameters:
            i (int): Current index in candidates list
            cur (List[int]): Current combination being formed
            total (int): Sum of elements in cur
            """
            # If the current total matches the target, add the combination to the result
            if total == target:
                res.append(cur.copy())  # Make a copy to avoid reference issues
                return
            
            # If index exceeds array bounds or sum exceeds target, return
            if i >= len(candidates) or total > target:
                return
            
            # Include the current candidate in the combination
            cur.append(candidates[i])
            dfs(i, cur, total + candidates[i])  # Continue with the same index to allow reuse
            
            # Backtrack: Remove the last added element and explore the next possibility
            cur.pop()
            dfs(i + 1, cur, total)  # Move to the next index
        
        # Start DFS from index 0 with an empty combination and total sum as 0
        dfs(0, [], 0)
        
        return res  # Return the list of all valid combinations
