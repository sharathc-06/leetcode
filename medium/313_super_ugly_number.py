class Solution:
    def nthSuperUglyNumber(self, n: int, primes: List[int]) -> int:
        ugly = [1]

        pointers = [0] * len(primes)

        while len(ugly) < n:
            candidates = []

            for i in range(len(primes)):
                candidates.append(ugly[pointers[i]] * primes[i])

            next_ugly = min(candidates)
            ugly.append(next_ugly)

            for i in range(len(primes)):
                if candidates[i] == next_ugly:
                    pointers[i] += 1

        return ugly[-1]