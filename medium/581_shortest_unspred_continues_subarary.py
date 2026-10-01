class Solution:
    def findUnsortedSubarray(self, nums: list[int]) -> int:
        sorted_nums = sorted(nums)

        left = 0
        right = len(nums) - 1

        while left < len(nums) and nums[left] == sorted_nums[left]:
            left += 1

        if left == len(nums):
            return 0

        while nums[right] == sorted_nums[right]:
            right -= 1

        return right - left + 1