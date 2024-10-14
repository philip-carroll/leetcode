from typing import List


class Solution:
    def countBits(self, n: int) -> List[int]:
        res = []
        for i in range(n + 1):
            res.append(bin(i).count('1'))

        return res


if __name__ == '__main__':
    sol = Solution()

    n = 2

    res = sol.countBits(n)
    print(res)
