from typing import List


class Solution:
    def kidsWithCandies(self, candies: List[int], extraCandies: int) -> List[bool]:
        most = max(candies)
        return [True if c + extraCandies >= most else False for c in candies]


if __name__ == '__main__':
    sol = Solution()

    res = sol.kidsWithCandies([2, 3, 5, 1, 3], 3)
    print(res)
    res = sol.kidsWithCandies([4, 2, 1, 1, 2], 1)
    print(res)
    res = sol.kidsWithCandies([12, 1, 12], 10)
    print(res)
