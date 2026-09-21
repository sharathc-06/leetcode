class Solution:
    def flatten(self, root: Optional[TreeNode]) -> None:
        if not root:
            return

        self.flatten(root.left)
        self.flatten(root.right)

        left = root.left
        right = root.right

        root.left = None
        root.right = left

        current = root

        while current.right:
            current = current.right

        current.right = right