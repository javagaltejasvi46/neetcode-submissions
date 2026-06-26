# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def rightSideView(self, roots: Optional[TreeNode]) -> List[int]:
        result = []
        def levelOrder(root):
        
            if not root:
                return []

            queue = deque([root])
            result = []

            while queue:
                level_size = len(queue)
                level = []

                for _ in range(level_size):
                    node = queue.popleft()

                    level.append(node.val)

                    if node.left:
                        queue.append(node.left)

                    if node.right:
                        queue.append(node.right)

                result.append(level)

            return result

        temp = levelOrder(roots)
        for i in temp :
            result.append(i[-1])
        return result
            
