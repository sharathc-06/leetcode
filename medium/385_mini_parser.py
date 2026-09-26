class Solution:
    def deserialize(self, s: str) -> NestedInteger:

        if s[0] != '[':
            return NestedInteger(int(s))

        stack = []
        num = ""
        negative = False

        for i, c in enumerate(s):

            if c == '[':
                stack.append(NestedInteger())

            elif c == '-':
                negative = True

            elif c.isdigit():
                num += c

            elif c in ',]':
                if num:
                    value = int(num)
                    if negative:
                        value = -value

                    stack[-1].add(NestedInteger(value))

                    num = ""
                    negative = False

                if c == ']':
                    current = stack.pop()

                    if stack:
                        stack[-1].add(current)
                    else:
                        return current