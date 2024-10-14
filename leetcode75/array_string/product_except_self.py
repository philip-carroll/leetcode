from typing import List


class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        res = []
        sum = 1
        zeros = nums.count(0)

        if zeros > 1:
            res = [0 for _ in nums]
        elif zeros == 1:
            for i in range(0, len(nums)):
                if nums[i] != 0:
                    sum = sum * nums[i]
                    res.append(0)
                else:
                    idx = i
            res.insert(idx, sum)
        else:
            for i in range(1, len(nums)):
                sum = sum * nums[i]
            res.append(sum)
            for i in range(1, len(nums)):
                res.append(int(res[i - 1] * (nums[i - 1] / nums[i])))

        return res


if __name__ == '__main__':
    sol = Solution()

    res = sol.productExceptSelf([1, 2, 3, 4])
    print(res)
    res = sol.productExceptSelf([-1, 1, 0, -3, 3])
    print(res)
