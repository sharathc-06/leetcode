class Solution:
    def convertToBase7(self, num: int) -> str:
        if num == 0:
            return "0"

        negative = num < 0
        num = abs(num)

        result = []

        while num > 0:
            result.append(str(num % 7))
            num //= 7

        result.reverse()

        answer = "".join(result)

        if negative:
            answer = "-" + answer

        return answer