class Solution:
    def maxRotateFunction(self, nums: List[int]) -> int:
        n = len(nums)

        total = sum(nums)

        current = 0

        for i in range(n):
            current += i * nums[i]

        answer = current

        for i in range(n - 1, 0, -1):
            current = current + total - n * nums[i]

            answer = max(answer, current)

        return answer