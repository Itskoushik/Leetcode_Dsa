class Solution:
    def search(self, nums: List[int], target: int) -> int:
        # Initialize two pointers: 
        # l (left) at the beginning, r (right) at the end of the array
        l, r = 0, len(nums) - 1
        
        # Perform binary search
        while l <= r:
            # Find the middle index
            mid = (l + r) // 2

            # If the middle element is the target, return its index
            if nums[mid] == target:
                return mid

            # Check if the left half is sorted
            if nums[l] <= nums[mid]:
                # If the target lies in the left sorted half
                if nums[l] <= target < nums[mid]:
                    r = mid - 1  # Move search to the left half
                else:
                    l = mid + 1  # Move search to the right half
            else:
                # Otherwise, the right half must be sorted
                if nums[mid] < target <= nums[r]:
                    l = mid + 1  # Move search to the right half
                else:
                    r = mid - 1  # Move search to the left half
        
        # If target is not found, return -1
        return -1
