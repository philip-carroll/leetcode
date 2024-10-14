from typing import List


class Solution:
    def findDifference(self, nums1: List[int], nums2: List[int]) -> List[List[int]]:
        nums1 = set(nums1)
        nums2 = set(nums2)
        diff1 = list(nums1 - nums2)
        diff2 = list(nums2 - nums1)

        return [diff1, diff2]


if __name__ == '__main__':
    sol = Solution()

    print(sol.findDifference([1, 2, 3], [2, 4, 6]))
