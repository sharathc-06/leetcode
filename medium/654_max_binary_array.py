class Solution:
    def constructMaximumBinaryTree(self, nums: list[int]) -> 'TreeNode':

        def build(left, right):
            if left > right:
                return None

            max_index = left

            for i in range(left + 1, right + 1):
                if nums[i] > nums[max_index]:
                    max_index = i

            root = TreeNode(nums[max_index])

            root.left = build(left, max_index - 1)
            root.right = build(max_index + 1, right)

            return root

        return build(0, len(nums) - 1)