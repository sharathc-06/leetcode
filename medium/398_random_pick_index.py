import random

class Solution:
    def __init__(self, nums: List[int]):
        self.nums=nums
        self.cache={}
    def pick(self, target: int) -> int:
        if target not in self.cache:
            self.cache[target]=[i for i in range(
                len(self.nums)) if self.nums[i]==target]
        return choice(self.cache[target])

        return random.choice(indexes)