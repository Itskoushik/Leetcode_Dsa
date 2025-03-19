class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        charSet = set()  # Set to store unique characters in the current window
        l = 0  # Left pointer of the sliding window
        res = 0  # Variable to store the length of the longest substring
        
        # Iterate through the string using a right pointer (r)
        for r in range(len(s)):
            # If character at r already exists in the set, shrink the window from the left
            while s[r] in charSet:
                charSet.remove(s[l])  # Remove character at the left pointer
                l += 1  # Move the left pointer forward
            
            charSet.add(s[r])  # Add the new character to the set
            res = max(res, r - l + 1)  # Update the maximum length
        
        return res  # Return the length of the longest substring

