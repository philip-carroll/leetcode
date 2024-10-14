from typing import List


class Solution:
    def canPlaceFlowers(self, flowerbed: List[int], n: int) -> bool:
        while n > 0:
            s = ''.join(str(f) for f in flowerbed)
            if s == '0' or s.startswith('00'):
                flowerbed[0] = 1
            elif s.endswith('00'):
                flowerbed[-1] = 1
            else:
                pos = s.find('000')
                if pos > -1:
                    flowerbed[pos + 1] = 1
                else:
                    return False

            n -= 1

        return True


if __name__ == '__main__':
    sol = Solution()

    res = sol.canPlaceFlowers([0], 1)
    print(res)
