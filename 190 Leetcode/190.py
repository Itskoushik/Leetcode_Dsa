class Solution:
    def reverseBits(self, n: int) -> int:
        res = 0  # Initialize result variable to store the reversed bits
        
        # Loop through all 32 bits of the given number
        for i in range(32):
            bit = (n >> i) & 1  # Extract the i-th bit from n
            res = res | (bit << (31 - i))  # Shift the extracted bit to its reversed position and update res
        
        return res  # Return the final reversed integer
