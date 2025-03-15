from typing import List

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        # Dictionary to store the frequency count of each element in nums
        count = {}
        
        # Creating a list of lists to act as buckets for frequency-based grouping
        # The index represents the frequency, and the values are lists of elements with that frequency
        freq = [[] for i in range(len(nums) + 1)]

        # Count the occurrences of each number in nums
        for n in nums:
            count[n] = 1 + count.get(n, 0)  # Increment count for each occurrence

        # Group numbers into the frequency buckets based on their count
        for n, c in count.items():
            freq[c].append(n)

        # Initialize the result list
        res = []
        
        # Traverse the frequency list in reverse order to get the most frequent elements first
        for i in range(len(freq) - 1, 0, -1):
            for n in freq[i]:  # Extract elements from the current frequency bucket
                res.append(n)  # Add to result
                if len(res) == k:  # Stop when we have found k most frequent elements
                    return res
