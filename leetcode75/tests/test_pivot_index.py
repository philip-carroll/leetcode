from unittest import TestCase
from leetcode75.pivot_index import Solution


class TestSolution(TestCase):
    def setUp(self):
        self.sol = Solution()

    def test_pivot_index(self):
        nums = [1, 7, 3, 6, 5, 6]
        self.assertEqual(self.sol.pivotIndex(nums), 3)

        nums = [1, 2, 3]
        self.assertEqual(self.sol.pivotIndex(nums), -1)

        nums = [2, 1, -1]
        self.assertEqual(self.sol.pivotIndex(nums), 0)
