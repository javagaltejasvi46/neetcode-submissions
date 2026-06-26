# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        
        current_max = root.val
        def traverse(node, current_max):
            if not node:
                return 0
            
            is_good = 1 if node.val >= current_max else 0
            new_max = max(current_max, node.val)
            
            return is_good + traverse(node.left, new_max) + traverse(node.right, new_max)
        result = traverse(root,current_max)          

        return result