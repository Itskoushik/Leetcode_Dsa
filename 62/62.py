class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        # Initialize a row with all elements as 1 (base case)
        row = [1] * n  

        # Iterate over each row from bottom to top, except the last row
        for i in range(m - 1):
            # Create a new row to store computed values for the current row
            newRow = [1] * n  
            # Iterate from right to left, computing the number of unique paths
            for j in range(n - 2, -1, -1):  
                newRow[j] = newRow[j + 1] + row[j]  # Sum of right and bottom cells
            # Update row to the newly computed row
            row = newRow  

        # The top-left cell contains the total number of unique paths
        return row[0]
