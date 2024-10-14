class Solution:

    def reverseVowels(self, s: str) -> str:
        vowels = ('a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U')
        s = list(s)
        v = [c for c in s if c in vowels]

        for i in range(len(s)):
            if s[i] in vowels:
                s[i] = v.pop()

        return ''.join(s)


if __name__ == '__main__':
    sol = Solution()

    res = sol.reverseVowels('aA')
    print(res)
