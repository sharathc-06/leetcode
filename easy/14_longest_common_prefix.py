class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        window = 1

        while True:
            if window > len(strs[0]):
                break

            prefix = strs[0][:window]

            for word in strs:
                if len(word) < window or word[:window] != prefix:
                    return strs[0][:window - 1]

            window += 1

        return strs[0]