class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        # Use a set to keep track of unique characters in the current window
        charSet = set()
        # Left pointer of the sliding window
        l = 0
        # Variable to store the length of the longest substring
        res = 0

        # Iterate through the string with the right pointer
        for r in range(len(s)):
            # If a duplicate character is found, move the left pointer
            while s[r] in charSet:
                charSet.remove(s[l])  # Remove leftmost character from the set
                l += 1  # Move the left pointer forward
            
            # Add the current character to the set
            charSet.add(s[r])
            # Update the result with the maximum length found so far
            res = max(res, r - l + 1)
        
        return res  # Return the length of the longest substring without repeating characters
