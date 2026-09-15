class Solution:
    def constructArray(self, n: int, k: int) -> List[int]:
        result = []
        left = 1
        right = k + 1

        while left <= right:
            if len(result) % 2 == 0:
                result.append(left)
                left += 1
            else:
                result.append(right)
                right -= 1

        for i in range(k + 2, n + 1):
            result.append(i)

        return result