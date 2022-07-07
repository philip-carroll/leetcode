class Solution(object):
    def maxArea(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        maxArea = 0

        for i in range(0, len(height)):
            for j in range(0, len(height)):
                if j > i:
                    hi = height[i]
                    hj = height[j]
                    area = (j - i) * min(hi, hj)
                    if area > maxArea:
                        maxArea = area

        return maxArea


if __name__ == '__main__':
    sol = Solution()
    print(sol.maxArea([1, 8, 6, 2, 5, 4, 8, 3, 7]))
    print(sol.maxArea([1, 1]))
