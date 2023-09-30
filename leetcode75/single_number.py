from typing import List


class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        dictionary = {}

        for x in nums:
            if x not in dictionary:
                dictionary[x] = 1
            else:
                dictionary[x] = dictionary[x] + 1

        number = list(dictionary.keys())[list(dictionary.values()).index(1)]

        return number


if __name__ == '__main__':
    sol = Solution()
    print(sol.singleNumber([0, 1, 1, 2, 3, 3, 0, 4, 4]))
