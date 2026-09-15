class Solution:
    def solveEquation(self, equation: str) -> str:
        left, right = equation.split("=")

        def parse(s):
            x = 0
            const = 0
            sign = 1
            i = 0

            while i < len(s):
                if s[i] == "+":
                    sign = 1
                    i += 1
                elif s[i] == "-":
                    sign = -1
                    i += 1

                j = i
                while j < len(s) and s[j].isdigit():
                    j += 1

                if j < len(s) and s[j] == "x":
                    num = int(s[i:j]) if j > i else 1
                    x += sign * num
                    i = j + 1
                else:
                    num = int(s[i:j])
                    const += sign * num
                    i = j

            return x, const

        lx, lc = parse(left)
        rx, rc = parse(right)

        x = lx - rx
        c = rc - lc

        if x == 0:
            return "Infinite solutions" if c == 0 else "No solution"

        return f"x={c // x}"