class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        stack = []
        node = root
        count = 0

        while stack or node:

            # Go to the leftmost node
            while node:
                stack.append(node)
                node = node.left

            # Visit the node
            node = stack.pop()
            count += 1

            if count == k:
                return node.val

            # Traverse the right subtree
            node = node.right