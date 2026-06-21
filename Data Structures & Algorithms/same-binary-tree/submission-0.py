# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        
        a,b=p,q
        def traverse(nodea,nodeb):
            if not nodea and not nodeb:
                return True 
            if not nodea or not nodeb:
                return False
            if nodea.val != nodeb.val:
                return False
            return (
                traverse(nodea.left,nodeb.left)
                and
                traverse(nodea.right,nodeb.right)
            )

            
        return traverse(a,b)
            


        