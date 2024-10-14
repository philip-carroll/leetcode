from typing import List


class Solution:
    def increasingTriplet(self, nums: List[int]) -> bool:

        mini = float('inf')
        minj = float('inf')

        for i in range(len(nums)):
            if nums[i] < mini:
                mini = nums[i]
                for j in range(i + 1, len(nums)):
                    if nums[i] < nums[j]:
                        if nums[j] < minj:
                            minj = nums[j]
                            for k in range(j + 1, len(nums)):
                                if nums[j] < nums[k]:
                                    # print(nums[i], nums[j], nums[k])
                                    return True

        return False


if __name__ == '__main__':
    sol = Solution()

    res = sol.increasingTriplet([1, 2, 3, 4, 5])
    print(res)
