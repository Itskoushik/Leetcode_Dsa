class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        min_heap = nums[:k]  
        heapq.heapify(min_heap)  # Convert first k elements into a Min-Heap
        
        for num in nums[k:]:  # Process the remaining elements
            if num > min_heap[0]:  # If num is larger than heap's root
                heapq.heappushpop(min_heap, num)  # Replace the smallest element
        
        return min_heap[0]  # Root of the Min-Heap is the Kth largest element

