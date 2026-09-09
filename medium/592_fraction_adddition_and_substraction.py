from fractions import Fraction

class Solution:
    def fractionAddition(self, expression: str) -> str:
        result = Fraction(0, 1)

        i = 0

        while i < len(expression):
            sign = 1

            if expression[i] == '+':
                i += 1
            elif expression[i] == '-':
                sign = -1
                i += 1

            j = expression.find('/', i)

            numerator = int(expression[i:j])

            i = j + 1

            
            j = i

            while j < len(expression) and expression[j].isdigit():
                j += 1

            denominator = int(expression[i:j])

            result += Fraction(sign * numerator, denominator)

            i = j

        return f"{result.numerator}/{result.denominator}"
