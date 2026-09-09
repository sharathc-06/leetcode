class Solution:
    def findMinDifference(self, timePoints: List[str]) -> int:
        times = []

        for time in timePoints:
            hour, minute = map(int, time.split(":"))
            times.append(hour * 60 + minute)

        times.sort()

        answer = float('inf')

        for i in range(1, len(times)):
            answer = min(answer, times[i] - times[i - 1])

       
        answer = min(answer, 1440 - times[-1] + times[0])

        return answer
