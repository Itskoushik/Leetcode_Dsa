class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        # Base case: if the tree is empty (root is None), return None
        if not root:
            return None
        
        # Swap the left and right child of the current node
        tmp = root.left  # Store left child in a temporary variable
        root.left = root.right  # Assign right child to left
        root.right = tmp  # Assign temporary left child to right

        # Recursively call the function on the left subtree
        self.invertTree(root.left)
        
        # Recursively call the function on the right subtree
        self.invertTree(root.right)
        
        # Return the root of the inverted tree
        return root
