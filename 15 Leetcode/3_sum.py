class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        res = []  # List to store unique triplets
        nums.sort()  # Sort the array to use the two-pointer approach
        
        for i, a in enumerate(nums):
            # Skip duplicate values to avoid duplicate triplets
            if i > 0 and a == nums[i - 1]:
                continue
            
            l, r = i + 1, len(nums) - 1  # Left and right pointers
            
            while l < r:
                threesum = a + nums[l] + nums[r]  # Calculate the sum of triplet
                
                if threesum > 0:
                    r -= 1  # Decrease sum by moving the right pointer left
                elif threesum < 0:
                    l += 1  # Increase sum by moving the left pointer right
                else:
                    res.append([a, nums[l], nums[r]])  # Found a valid triplet
                    l += 1  # Move left pointer to the right
                    
                    # Skip duplicate values to avoid duplicate triplets
                    while l < r and nums[l] == nums[l - 1]:
                        l += 1
        
        return res  # Return the list of unique triplets
