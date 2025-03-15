from typing import List

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        # Dictionary to store the frequency of each number
        count = {}  
        # Create a list of empty lists, indexed by frequency
        freq = [[] for _ in range(len(nums) + 1)]  

        # Count occurrences of each number
        for n in nums:
            count[n] = 1 + count.get(n, 0)  # Increment count of `n`, default 0 if not found
        
        # Place numbers into frequency buckets
        for n, c in count.items():  # `n` is the number, `c` is its frequency
            freq[c].append(n)  # Append number to its frequency index
        
        # Result list to store the top `k` frequent numbers
        res = []
        
        # Iterate from highest frequency to lowest
        for i in range(len(freq) - 1, 0, -1):  # Start from max possible frequency
            for n in freq[i]:  # Get all numbers with this frequency
                res.append(n)  # Add to result list
                if len(res) == k:  # Stop when we have `k` elements
                    return res  # Return top `k` elements
