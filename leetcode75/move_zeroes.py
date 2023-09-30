from typing import List


class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        zero_indexes = [i for i in range(len(nums)) if nums[i] == 0]
        for i in sorted(zero_indexes, reverse=True):
            nums.append(nums.pop(i))

        return nums


if __name__ == '__main__':
    sol = Solution()

    # print(sol.moveZeroes([0, 1, 0, 3, 12]))
    # print(sol.moveZeroes([0, 0, 1]))
    print(sol.moveZeroes([0]))
