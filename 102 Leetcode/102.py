# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val  # Initialize node value
#         self.left = left  # Initialize left child
#         self.right = right  # Initialize right child

from collections import deque  # Import deque for efficient queue operations

class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        res = []  # Result list to store level-wise node values

        q = deque()  # Initialize a queue for BFS traversal
        q.append(root)  # Add the root node to the queue

        while q:  # Continue until the queue is empty
            qlen = len(q)  # Get the number of nodes at the current level
            level = []  # List to store values of the current level
            
            for i in range(qlen):  # Process all nodes at the current level
                node = q.popleft()  # Remove the front node from the queue
                
                if node:  # If the node is not null
                    level.append(node.val)  # Add node value to the level list
                    q.append(node.left)  # Add left child to the queue
                    q.append(node.right)  # Add right child to the queue
            
            if level:  # If the level list is not empty (ignoring null levels)
                res.append(level)  # Append the level to the result list
        
        return res  # Return the final level order traversal result

