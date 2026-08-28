import random

class Solution:

    def __init__(self, nums: List[int]):
        self.original = nums[:]
        self.nums = nums[:]

    def reset(self) -> List[int]:
        return self.original[:]

    def shuffle(self) -> List[int]:
        nums = self.original[:]

        for i in range(len(nums) - 1, 0, -1):
            j = random.randint(0, i)

            nums[i], nums[j] = nums[j], nums[i]

        return nums