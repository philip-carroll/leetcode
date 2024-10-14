from typing import List


class Solution:
    def compress(self, chars: List[str]) -> int:
        temp = chars.copy()

        last = ''
        count = 0
        popped = 0
        for i in range(len(temp)):
            if temp[i] == last:
                count += 1
                chars.pop(i - popped)
                popped += 1
            else:
                last = temp[i]
                if i > 0:  # first element will always be new
                    if count > 1:  # only insert count if greater than 1
                        for c in list(str(count)):
                            chars.insert(i - popped, c)
                            popped -= 1
                            count = 1
                else:
                    count += 1

        if count > 1:
            chars.extend(list(str(count)))

        print(chars)
        return len(chars)


if __name__ == '__main__':
    sol = Solution()

    res = sol.compress(['x', "a", "a", 'a', "b", "b", "c", "c", "c"])
    print(res)
    res = sol.compress(['a'])
    print(res)
    res = sol.compress(["a", "b", "b", "b", "b", 'c', "b", "b", "b", "b", "b", "b", "b", "b", "b", "b", "b", "b"])
    print(res)
