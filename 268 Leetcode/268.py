class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        res = len(nums)  # Initialize `res` with `n` (the length of the list)
        
        for i in range(len(nums)):  # Iterate over the indices of the list
            res += (i - nums[i])  # Adjust `res` by adding the difference between index and value
        
        return res  # The final value of `res` gives the missing number
