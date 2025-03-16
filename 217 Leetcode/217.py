
class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        # Initialize a hash set to store unique numbers
        hashset = set()  

        # Iterate through each number in the list
        for n in nums:
            # If the number is already in the set, a duplicate exists
            if n in hashset:
                return True  
            
            # Otherwise, add the number to the set
            hashset.add(n)  

        # If no duplicates were found, return False
        return False  
