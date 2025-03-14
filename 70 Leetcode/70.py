class Solution:
    def climbStairs(self, n: int) -> int:
        # Initialize two variables to store the number of ways to reach the last two steps.
        # one represents the number of ways to reach the (n-1)th step.
        # two represents the number of ways to reach the (n-2)th step.
        one, two = 1, 1

        # Loop from 0 to n-2 (since the first step is already considered).
        for i in range(n - 1):
            # Store the value of one temporarily before updating it.
            temp = one
            
            # The number of ways to reach the current step (one) is the sum of the previous two steps.
            one = one + two
            
            # Move the previous step counter forward.
            two = temp
        
        # The final value of 'one' gives the total number of ways to reach the nth step.
        return one
