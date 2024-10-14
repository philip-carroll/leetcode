from collections import defaultdict


class Solution(object):
    def closeStrings(self, word1, word2):
        """
        :type word1: str
        :type word2: str
        :rtype: bool
        """
        if len(word1) == len(word2):
            w1 = defaultdict(int)
            w2 = defaultdict(int)

            for i in range(len(word1)):
                w1[word1[i]] += 1

            for i in range(len(word2)):
                w2[word2[i]] += 1

            # print(w1.keys())
            # print(sorted(w1.values()))
            # print(w2.keys())
            # print(sorted(w2.values()))

            return sorted(w1.keys()) == sorted(w2.keys()) and sorted(w1.values()) == sorted(w2.values())

        return False


if __name__ == '__main__':
    sol = Solution()

    res = sol.closeStrings('abc', 'bca')
    print(res)
    res = sol.closeStrings('a', 'aa')
    print(res)
    res = sol.closeStrings('cabbba', 'abbccc')
    print(res)
    res = sol.closeStrings('uau', 'ssx')
    print(res)
    res = sol.closeStrings('kyq', 'kqy')
    print(res)
