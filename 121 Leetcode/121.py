class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        # Initialize two pointers: left (buy day) and right (sell day)
        l, r = 0, 1  
        
        # Variable to store the maximum profit
        maxp = 0  

        # Iterate through the price list
        while r < len(prices):
            # If the current price is greater than the buying price, calculate profit
            if prices[l] < prices[r]:
                profit = prices[r] - prices[l]  # Profit if we buy at prices[l] and sell at prices[r]
                maxp = max(maxp, profit)  # Update max profit if current profit is greater
            else:
                # If the price at r is lower than at l, move the buy pointer to r
                l = r  
            
            # Move the sell pointer to the next day
            r += 1  

        # Return the maximum profit found
        return maxp
