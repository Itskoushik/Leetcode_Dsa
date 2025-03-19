class Solution:
    def numDecodings(self, s: str) -> int:
        # Dictionary to store computed results for dynamic programming (memoization)
        dp = {len(s): 1}

        # Depth-First Search (DFS) function with memoization
        def dfs(i):
            # If the result for index i is already computed, return it
            if i in dp:
                return dp[i]
            
            # If the current character is '0', it cannot be decoded
            if s[i] == "0":
                return 0
            
            # Decode the current digit separately
            res = dfs(i + 1)

            # Check if we can decode two digits together
            if (i + 1 < len(s) and 
                (s[i] == "1" or 
                (s[i] == "2" and s[i + 1] in "0123456"))):  
                res += dfs(i + 2)

            # Store the computed result in dp and return it
            dp[i] = res
            return res

        # Start DFS from index 0
        return dfs(0)
