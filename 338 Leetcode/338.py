
class Solution:
    def countBits(self, n: int) -> List[int]:
        dp = [0] * (n + 1)  # Initialize an array of size (n+1) to store the number of 1s for each number
        offset = 1  # Offset represents the most recent power of 2

        for i in range(1, n + 1):
            if offset * 2 == i:  # If `i` reaches the next power of 2
                offset = i  # Update offset to the current power of 2
            
            # The number of 1s in `i` is 1 + the number of 1s in `i - offset`
            dp[i] = 1 + dp[i - offset]

        return dp  # Return the list containing the count of 1s for all numbers from 0 to n

