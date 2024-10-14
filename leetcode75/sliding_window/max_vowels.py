class Solution:
    def maxVowels(self, s: str, k: int) -> int:
        vowels = ('a', 'e', 'i', 'o', 'u')
        max = 0

        vowelbin = [1 if s[i] in vowels else 0 for i in range(len(s))]
        vowelpos = [i for i in range(len(s)) if vowelbin[i] == 1]

        for pos in vowelpos:
            count = sum(vowelbin[pos:pos + k])
            if count == k:
                return k
            elif count > max:
                max = count

        return max


if __name__ == '__main__':
    sol = Solution()

    res = sol.maxVowels('aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa', 10)
    print(res)
