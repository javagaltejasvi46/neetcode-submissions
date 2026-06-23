# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def insertIntoBST(self, root: Optional[TreeNode], val: int) -> Optional[TreeNode]:
        node = TreeNode(val)
        temp = root
        if root == None: return node
        while True:
            if temp.val == node.val:
                return root
            if node.val < temp.val:
                if temp.left is None:
                    temp.left = node
                    return root
                temp= temp.left
            else:
                if temp.right is None:
                    temp.right = node
                    return root
                temp = temp.right
        
