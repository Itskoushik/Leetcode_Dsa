class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        res = max(nums)  # Initialize the result with the maximum single element in nums
        curmin, curmax = 1, 1  # Track the minimum and maximum product subarrays

        for n in nums:
            temp = curmax * n  # Store curmax * n before updating curmax

            # Update curmax: It can be the current number itself, product of curmax, or product of curmin
            curmax = max(n * curmax, n * curmin, n)
            
            # Update curmin: Similar to curmax, but we track the minimum value
            curmin = min(temp, n * curmin, n)
            
            # Update the result with the maximum product found so far
            res = max(res, curmax)

        return res  # Return the maximum product subarray
