class Solution:
    def decodeString(self, s: str) -> str:
        num_stack = []
        str_stack = []

        current = ""
        num = 0

        for c in s:

            if c.isdigit():
                num = num * 10 + int(c)

            elif c == '[':
                num_stack.append(num)
                str_stack.append(current)

                num = 0
                current = ""

            elif c == ']':
                repeat = num_stack.pop()
                previous = str_stack.pop()

                current = previous + current * repeat

            else:
                current += c

        return current