from typing import List

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        # Dictionary to store previously seen numbers and their indices
        prevmap = {}

        # Iterate through the list with index and value
        for i, n in enumerate(nums):
            # Calculate the difference needed to reach the target
            diff = target - n

            # If the difference is already in the dictionary, return the indices
            if diff in prevmap:
                return [prevmap[diff], i]

            # Otherwise, store the current number with its index
            prevmap[n] = i

        # Return an empty list (this line is theoretically unreachable for valid input)
        return []
