class Solution:
    def heightChecker(self, heights: list[int]) -> int:
        expected = sorted(heights)

        count = 0

        for actual, correct in zip(heights, expected):
            if actual != correct:
                count += 1

        return count