class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        # Create a 2D DP table initialized with zeros
        # The table has dimensions (len(text1) + 1) x (len(text2) + 1)
        # dp[i][j] represents the length of the longest common subsequence 
        # between text1[i:] and text2[j:]
        dp = [[0 for j in range(len(text2) + 1)] for i in range(len(text1) + 1)]

        # Traverse the strings in reverse order (bottom-up DP approach)
        for i in range(len(text1) - 1, -1, -1):  # Iterate from the last character of text1 to the first
            for j in range(len(text2) - 1, -1, -1):  # Iterate from the last character of text2 to the first
                if text1[i] == text2[j]:  # If characters match, take the diagonal value and add 1
                    dp[i][j] = 1 + dp[i + 1][j + 1]
                else:  # If they don't match, take the maximum of the right and bottom cell
                    dp[i][j] = max(dp[i][j + 1], dp[i + 1][j])

        # The answer is stored in dp[0][0], which considers the entire text1 and text2
        return dp[0][0]
