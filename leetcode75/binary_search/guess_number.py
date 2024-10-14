# The guess API is already defined for you.
# @param num, your guess
# @return -1 if num is higher than the picked number
#          1 if num is lower than the picked number
#          otherwise return 0
picked = 2


def guess(num: int) -> int:
    if num > picked:
        return -1
    elif num < picked:
        return 1
    else:
        return 0


class Solution:
    def guessNumber(self, n: int) -> int:
        if n > 1:
            l, h = 0, n
            while True:
                m = (l + h) // 2
                res = guess(m)
                if res == -1:
                    if h - l == 1:
                        return h
                    else:
                        h = m
                elif res == 1:
                    if h - l == 1:
                        return h
                    else:
                        l = m
                else:
                    return m
        else:
            return n


if __name__ == '__main__':
    sol = Solution()

    res = sol.guessNumber(2)
    print(res)
