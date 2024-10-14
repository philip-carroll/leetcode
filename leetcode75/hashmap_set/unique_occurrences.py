from typing import List


class Solution:
    def uniqueOccurrences(self, arr: List[int]) -> bool:
        occurences = {}
        for i in arr:
            if i in occurences:
                occurences[i] += 1
            else:
                occurences[i] = 1

        unique = set(occurences.values())
        return len(unique) == len(occurences)


if __name__ == '__main__':
    sol = Solution()

    res = sol.uniqueOccurrences([1, 2])
    print(res)
