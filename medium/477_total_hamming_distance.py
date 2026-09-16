class Solution:
    def totalHammingDistance(self, nums: List[int]) -> int:
        ans = 0

        for bit in range(32):
            ones = 0

            for num in nums:
                ones += (num >> bit) & 1

            zeros = len(nums) - ones
            ans += ones * zeros

        return ans