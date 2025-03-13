class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        cur = root  # Start traversal from the root of the Binary Search Tree (BST)
        
        while cur:  # Continue searching while the current node is not None
            if p.val > cur.val and q.val > cur.val:  
                # If both p and q are greater than the current node, move to the right subtree
                cur = cur.right  
            elif p.val < cur.val and q.val < cur.val:  
                # If both p and q are smaller than the current node, move to the left subtree
                cur = cur.left  
            else:  
                # If one node is on the left and the other is on the right, or if cur is p or q,
                # then cur is the lowest common ancestor
                return cur  

