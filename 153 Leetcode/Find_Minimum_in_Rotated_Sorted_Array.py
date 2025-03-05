class Solution:
    def findMin(self, nums: List[int]) -> int:
        res = nums[0]  # Initialize result with the first element
        l, r = 0, len(nums) - 1  # Set left and right pointers
        
        while l <= r:  # Binary search loop
            if nums[l] < nums[r]:  
                # If the current segment [l:r] is sorted, the smallest element is nums[l]
                res = min(res, nums[l])
                break  # No need to search further

            m = (l + r) // 2  # Find middle index
            res = min(res, nums[m])  # Update result with nums[m]

            if nums[m] >= nums[l]:  
                # If nums[m] is greater than nums[l], it means the left half is sorted.
                # The minimum must be in the right half.
                l = m + 1
            else:  
                # If nums[m] is smaller than nums[l], the minimum is in the left half.
                r = m - 1
        
        return res  # Return the minimum found
