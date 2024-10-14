class Solution:

    def gcdOfStrings(self, str1: str, str2: str) -> str:
        strlen = len(str1)
        for i in range(strlen, 0, -1):
            for j in range(strlen - i + 1):
                if str1[j:i + j] in str2 and str1.replace(str1[j:i + j], '') == '' and str2.replace(str1[j:i + j],
                                                                                                    '') == '':
                    return str1[j:i + j]

        return ''


if __name__ == '__main__':
    sol = Solution()

    res = sol.gcdOfStrings('ABCABC', 'ABC')
    print(res)
    res = sol.gcdOfStrings('ABABAB', 'ABAB')
    print(res)
    res = sol.gcdOfStrings('LEET', 'CODE')
    print(res)
    res = sol.gcdOfStrings("TAUXXTAUXXTAUXXTAUXXTAUXX", "TAUXXTAUXXTAUXXTAUXXTAUXXTAUXXTAUXXTAUXXTAUXX")
    print(res)
