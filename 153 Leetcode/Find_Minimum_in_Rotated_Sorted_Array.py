class Solution:
    def findMin(self, nums: List[int]) -> int:
        res = nums[0]  # Initialize result with the first element
        l, r = 0, len(nums) - 1  # Set left and right pointers
        
        while l <= r:
            # If the current segment is sorted, the leftmost element is the smallest
            if nums[l] < nums[r]:
                res = min(res, nums[1])  # **BUG: Should be nums[l] instead of nums[1]**
                break

            m = (l + r) // 2  # Calculate middle index
            res = min(res, nums[m])  # Update result with the middle element
            
            # Determine which side to search next
            if nums[m] >= nums[l]:  
                # Left half is sorted, so min must be in the right half
                l = m + 1
            else:  
                # Right half is unsorted, so min must be in the left half
                r = m - 1
        
        return res
