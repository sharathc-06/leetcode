class Solution:
    def relativeSortArray(
        self,
        arr1: list[int],
        arr2: list[int]
    ) -> list[int]:

        count = {}

        for num in arr1:
            count[num] = count.get(num, 0) + 1

        result = []

        # Put elements according to arr2
        for num in arr2:
            if num in count:
                result.extend([num] * count[num])
                del count[num]

        # Remaining elements in ascending order
        for num in sorted(count):
            result.extend([num] * count[num])

        return result