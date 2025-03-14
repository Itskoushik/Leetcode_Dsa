class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        # Create a DP array initialized with a large value (amount + 1) as a placeholder for impossible cases
        dp = [amount + 1] * (amount + 1)
        
        # Base case: 0 coins are needed to make an amount of 0
        dp[0] = 0
        
        # Iterate through all amounts from 1 to the given amount
        for a in range(1, amount + 1):
            # Check each coin denomination
            for c in coins:
                # If the current amount 'a' is at least 'c', meaning we can use this coin
                if a - c >= 0:
                    # Choose the minimum coins required by either keeping the previous value
                    # or using the current coin (1 + dp[a - c])
                    dp[a] = min(dp[a], 1 + dp[a - c])
        
        # If dp[amount] is still the large placeholder value, return -1 (no solution)
        return dp[amount] if dp[amount] != amount + 1 else -1
