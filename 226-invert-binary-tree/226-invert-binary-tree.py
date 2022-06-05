# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        if not root:
            return None
        
        node = root
        queue = deque([root])
        
        while queue:
            node = queue.pop()
            
            if node.left:
                queue.appendleft(node.left)
            if node.right:
                queue.appendleft(node.right)
            
            node.left, node.right = node.right, node.left
        
        return root
                
            
        
        