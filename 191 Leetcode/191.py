class Solution:
    def hammingWeight(self, n: int) -> int:
        res = 0  # Initialize a counter to store the number of 1s in the binary representation
        
        while n:  # Loop runs until all bits in `n` become 0
            n &= (n - 1)  # This operation removes the rightmost set bit (1) in `n`
            res += 1  # Increment the counter for each set bit removed
        
        return res  # Return the total count of 1s in the binary representation

