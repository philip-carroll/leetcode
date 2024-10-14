class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        for c in s:
            i = t.find(c)
            if i > -1:
                t = t[i + 1:]
            else:
                return False

        return True


if __name__ == '__main__':
    sol = Solution()

    res = sol.isSubsequence(s="axc", t="ahbgdc")
    print(res)
