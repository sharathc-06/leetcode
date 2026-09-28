class Solution:
    def find132pattern(self, nums: list[int]) -> bool:
        stack = []
        second = float('-inf')

        for x in reversed(nums):

            if x < second:
                return True

            while stack and stack[-1] < x:
                second = stack.pop()

            stack.append(x)

        return False