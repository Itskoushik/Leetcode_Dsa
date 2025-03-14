from typing import List

class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        # Initialize a list to store the length of the longest increasing subsequence (LIS) 
        # ending at each index, initially set to 1 since the smallest LIS is the element itself.
        LIS = [1] * len(nums)

        # Iterate backwards through the list to build the LIS array dynamically.
        for i in range(len(nums) - 1, -1, -1):
            # Check for elements ahead of nums[i] to find increasing subsequences.
            for j in range(i + 1, len(nums)):
                # If nums[j] is greater than nums[i], it can extend the LIS at index i.
                if nums[i] < nums[j]:
                    # Update LIS[i] to store the maximum possible LIS ending at i.
                    LIS[i] = max(LIS[i], 1 + LIS[j])

        # Return the maximum value from the LIS array, which gives the length 
        # of the longest increasing subsequence in nums.
        return max(LIS)
