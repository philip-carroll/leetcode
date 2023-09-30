from typing import List


class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        for i in range(len(nums)):
            if i > 0:
                left = sum(nums[:i])
            else:
                left = 0
            right = sum(nums[i + 1:])
            if left == right:
                return i

        return -1


if __name__ == '__main__':
    sol = Solution()

    # nums = [1, 7, 3, 6, 5, 6]
    nums = [-1, -1, -1, 1, 1, 1]

    res = sol.pivotIndex(nums)
    print(res)
