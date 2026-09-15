class Solution:
    def maximumSwap(self, num: int) -> int:
        digits = list(str(num))
        last = {}

        for i, d in enumerate(digits):
            last[d] = i

        for i, d in enumerate(digits):
            for bigger in range(9, int(d), -1):
                if str(bigger) in last and last[str(bigger)] > i:
                    j = last[str(bigger)]
                    digits[i], digits[j] = digits[j], digits[i]
                    return int("".join(digits))

        return num