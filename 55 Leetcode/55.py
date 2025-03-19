class Solution:
    def canJump(self, nums: List[int]) -> bool:
        # Initialize the goal as the last index of the array
        goal = len(nums) - 1

        # Iterate backwards through the array
        for i in range(len(nums) - 1, -1, -1):
            # If the current index plus its jump value reaches or exceeds the goal, update the goal
            if i + nums[i] >= goal:
                goal = i
        
        # If we can reach index 0, return True, otherwise return False
        return True if goal == 0 else False
