class Solution:
    def nextGreaterElement(self, n: int) -> int:
        digits = list(str(n))

        i = len(digits) - 2

        # Find first decreasing digit
        while i >= 0 and digits[i] >= digits[i + 1]:
            i -= 1

        if i < 0:
            return -1

        # Find the smallest digit greater than digits[i]
        j = len(digits) - 1

        while digits[j] <= digits[i]:
            j -= 1

        # Swap
        digits[i], digits[j] = digits[j], digits[i]

        # Reverse everything after i
        digits[i + 1:] = reversed(digits[i + 1:])

        result = int("".join(digits))

        if result > 2**31 - 1:
            return -1

        return result