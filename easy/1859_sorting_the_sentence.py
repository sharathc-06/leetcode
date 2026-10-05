class Solution:
    def sortSentence(self, s: str) -> str:
        words = s.split()

        result = [None] * len(words)

        for word in words:
            position = int(word[-1])
            actual_word = word[:-1]

            result[position - 1] = actual_word

        return ' '.join(result)