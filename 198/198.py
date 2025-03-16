from typing import List

class Solution:
    def rob(self, nums: List[int]) -> int:
        # Initialize two variables to keep track of maximum money robbed up to two previous houses
        rob1, rob2 = 0, 0  

        # Iterate through each house's money in the list
        for n in nums:
            # Calculate the maximum money that can be robbed at the current step
            # Either rob the current house (n + rob1) or skip it and take rob2 (previous max)
            temp = max(n + rob1, rob2)

            # Move the previous values forward for the next iteration
            rob1 = rob2  # Update rob1 to the previous rob2 value
            rob2 = temp  # Update rob2 to the new maximum value

        # Return the maximum amount of money that can be robbed
        return rob2  
