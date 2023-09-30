from typing import List


class Solution:
    def largestAltitude(self, gain: List[int]) -> int:
        m = 0
        max = 0

        for i in gain:
            m += i
            if m > max:
                max = m

        return max


if __name__ == '__main__':
    sol = Solution()

    print(sol.largestAltitude([-5, 1, 5, 0, -7]))
    # print(sol.largestAltitude([-4, -3, -2, -1, 4, 3, 2]))
