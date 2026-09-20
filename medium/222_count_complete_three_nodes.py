class Solution:
    def countNodes(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0

        def height_left(node):
            h = 0
            while node:
                h += 1
                node = node.left
            return h

        def height_right(node):
            h = 0
            while node:
                h += 1
                node = node.right
            return h

        left_height = height_left(root)
        right_height = height_right(root)

        # Perfect binary tree
        if left_height == right_height:
            return (2 ** left_height) - 1

        return 1 + self.countNodes(root.left) + self.countNodes(root.right)