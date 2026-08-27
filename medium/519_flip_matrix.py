import random

class Solution:

    def __init__(self, m: int, n: int):
        self.n = n
        self.total = m * n
        self.remaining = self.total
        self.mapping = {}

    def flip(self) -> List[int]:
        r = random.randint(0, self.remaining - 1)

        actual = self.mapping.get(r, r)

        last = self.remaining - 1

        self.mapping[r] = self.mapping.get(last, last)

        self.remaining -= 1

        return [actual // self.n, actual % self.n]

    def reset(self) -> None:
        self.remaining = self.total
        self.mapping = {}