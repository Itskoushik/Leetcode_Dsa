class Solution:  
    # Define a class `Solution` which contains the function to find the maximum depth of a binary tree.
    
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        # Define a function `maxDepth` that takes the root of a binary tree as input and returns an integer (maximum depth).
        
        if not root:
            # If the tree is empty (i.e., root is None), return depth as 0 since there are no nodes.
            return 0
        
        return 1 + max(self.ma
