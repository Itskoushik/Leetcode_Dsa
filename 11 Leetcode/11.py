class Solution:
    def maxArea(self, height: List[int]) -> int:
        res = 0  # Variable to store the maximum area found
        l, r = 0, len(height) - 1  # Two pointers: left (l) at the start, right (r) at the end

        while l < r:  # Iterate until the two pointers meet
            # Calculate the area between the two vertical lines
            area = (r - l) * min(height[l], height[r])
            res = max(res, area)  # Update the maximum area if the current one is greater

            # Move the pointer pointing to the smaller height to try increasing the area
            if height[l] < height[r]:
                l += 1  # Move left pointer forward
            else:
                r -= 1  # Move right pointer backward

        return res  # Return the maximum area found
