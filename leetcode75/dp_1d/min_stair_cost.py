from typing import List


class Solution:

    def minCostClimbingStairs(self, cost: List[int]) -> int:
        mins = cost[-2:]  # seed list of minimums with last two elements

        for i in reversed(range(len(cost) - 2)):
            one = mins[0]
            two = mins[1]
            mins.insert(0, cost[i] + min(one, two))  # add the lower of one step or two

        return min(mins[0], mins[1])  # chose whether to start at first or second element


if __name__ == '__main__':
    sol = Solution()

    c = [10, 15, 20]
    # c = [1, 100, 1, 1, 1, 100, 1, 1, 100, 1]

    res = sol.minCostClimbingStairs(c)
    print(res)
