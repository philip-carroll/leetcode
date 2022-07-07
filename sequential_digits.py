from guppy import hpy


class Solution(object):
    def possible_values(self):
        vals = []
        for i in range(2, 10):  # implicitly applies low and high constraint
            for j in range(1, 10):
                if i + j <= 10:
                    vals.append(list(range(j, i + j)))
        return [int(''.join(map(str, v))) for v in vals]

    def sequentialDigits(self, low, high):
        """
        :type low: int
        :type high: int
        :rtype: List[int]
        """
        return [p for p in self.possible_values() if low <= p <= high]


if __name__ == '__main__':
    s = Solution()
    print(s.sequentialDigits(1000000, 10000000000000))

    h = hpy()
    print(h.heap())
