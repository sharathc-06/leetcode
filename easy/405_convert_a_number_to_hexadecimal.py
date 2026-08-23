class Solution:
    def toHex(self, num: int) -> str:
        if num == 0:
            return "0"

        hex_chars = "0123456789abcdef"
        result = []

        num &= 0xFFFFFFFF

        while num:
            result.append(hex_chars[num & 15])
            num >>= 4

        return "".join(result[::-1])