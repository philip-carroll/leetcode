class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        res = []
        word1 = list(word1)
        word2 = list(word2)

        while len(word1) > 0 and len(word2) > 0:
            res.append(word1.pop(0))
            res.append(word2.pop(0))

        if len(word1) > 0:
            res += word1
        else:
            res += word2

        return ''.join(res)


if __name__ == '__main__':
    sol = Solution()

    print(sol.mergeAlternately('ab', 'pqrs'))
