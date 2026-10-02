class Solution:
    def exclusiveTime(self, n: int, logs: list[str]) -> list[int]:
        result = [0] * n
        stack = []
        previous_time = 0

        for log in logs:
            function_id, action, timestamp = log.split(':')
            function_id = int(function_id)
            timestamp = int(timestamp)

            if action == "start":
                if stack:
                    result[stack[-1]] += timestamp - previous_time

                stack.append(function_id)
                previous_time = timestamp

            else:
                function_id = stack.pop()

                result[function_id] += timestamp - previous_time + 1

                previous_time = timestamp + 1

        return result