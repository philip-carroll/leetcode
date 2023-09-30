class Solution:
    def removeStars(self, s: str) -> str:
        star = 0
        l = list(reversed(s))
        res = []

        for i in range(len(l)):
            if l[i] == '*':
                star += 1
            elif star > 0:
                star -= 1
            else:
                res.append(l[i])

        return ''.join(reversed(res))


if __name__ == '__main__':
    sol = Solution()

    print(sol.removeStars('leet**cod*e'))
    # print(sol.removeStars('erase*****'))
