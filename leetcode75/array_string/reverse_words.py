class Solution:
    def reverseWords(self, s: str) -> str:
        l = s.split(' ')
        return ' '.join(reversed([w.strip() for w in l if w != '']))


if __name__ == '__main__':
    sol = Solution()

    res = sol.reverseWords('a good   example')
    print(res)
