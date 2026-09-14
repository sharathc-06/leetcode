class Solution:
    def canIWin(self, maxChoosableInteger: int, desiredTotal: int) -> bool:
        total = maxChoosableInteger * (maxChoosableInteger + 1) // 2
        
        if total < desiredTotal:
            return False
        if desiredTotal <= maxChoosableInteger:
            return True

        memo = {}

        def win(used, remaining):
            if used in memo:
                return memo[used]

            for i in range(1, maxChoosableInteger + 1):
                bit = 1 << i

                if not (used & bit):
                    if i >= remaining or not win(used | bit, remaining - i):
                        memo[used] = True
                        return True

            memo[used] = False
            return False

        return win(0, desiredTotal)