class Solution:  
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        # Create a dictionary to store the index of each element in nums1
        nums1Idx = {n: i for i, n in enumerate(nums1)}  

        # Initialize result array with -1 (default value when no greater element is found)
        res = [-1] * len(nums1)  

        # Stack to keep track of elements in nums2 for which we are finding the next greater element
        stack = []  

        # Iterate through each element in nums2
        for i in range(len(nums2)):  
            cur = nums2[i]  # Current element in nums2
            
            # Process stack elements that are smaller than the current element
            while stack and cur > stack[-1]:  
                var = stack.pop()  # Remove the top element from stack
                idx = nums1Idx[var]  # Get its index from nums1 using the dictionary
                res[idx] = cur  # Update result array with the next greater element
            
            # If current element is in nums1, add it to the stack for future comparison
            if cur in nums1Idx:  
                stack.append(cur)  
        
        # Return the final result array
        return res  

