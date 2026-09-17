class Solution:
    def monotoneIncreasingDigits(self, n: int) -> int:
        digits = list(str(n))

        i = len(digits) - 1

        while i > 0:
            if digits[i] < digits[i - 1]:
                digits[i - 1] = str(int(digits[i - 1]) - 1)
                digits[i:] = ['9'] * (len(digits) - i)
            i -= 1

        return int("".join(digits))