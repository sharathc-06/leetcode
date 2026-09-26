class Solution:
    def lengthLongestPath(self, input: str) -> int:
        stack = {0: 0}
        answer = 0

        for line in input.split('\n'):
            depth = line.count('\t')
            name = line.lstrip('\t')

            # Length of path before this item
            current_length = stack[depth] + len(name)

            if '.' in name:
                answer = max(answer, current_length)
            else:
                # +1 for '/'
                stack[depth + 1] = current_length + 1

        return answer