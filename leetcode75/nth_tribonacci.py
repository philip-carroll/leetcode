class Solution:
    def tribonacci(self, n: int) -> int:
        if n == 0:
            return 0
        elif n == 1 or n == 2:
            return 1
        else:
            return self.tribonacci(n - 1) + self.tribonacci(n - 2) + self.tribonacci(n - 3)

    def tribonacci_iterative(self, n: int) -> int:
        if n == 0:
            return 0
        elif n == 1 or n == 2:
            return 1
        else:
            res = 0
            p1 = 0
            p2 = 1
            p3 = 1

            while n > 2:
                res = p1 + p2 + p3

                p1 = p2
                p2 = p3
                p3 = res

                n -= 1

            return res


if __name__ == '__main__':
    sol = Solution()

    n = 31

    # res = sol.tribonacci(n)
    res = sol.tribonacci_iterative(n)
    print(res)
