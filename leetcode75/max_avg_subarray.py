from typing import List


class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        w = nums[len(nums) - k:len(nums)]
        s = sum(w)
        avg = s / k
        max = avg

        i = len(nums) - k - 1
        j = len(nums) - 1

        while i >= 0:
            s -= nums[j]
            s += nums[i]

            avg = s / k
            if avg > max:
                max = avg

            i -= 1
            j -= 1

        return max


if __name__ == '__main__':
    sol = Solution()

    # print(sol.findMaxAverage([1, 12, -5, -6, 50, 3], 4))
    print(sol.findMaxAverage([5], 1))
