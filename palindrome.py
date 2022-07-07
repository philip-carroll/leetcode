class Solution(object):
    def isPalindrome(self, x):
        """
        :type x: int
        :rtype: bool
        """
        if x >= 0:
            l = [int(i) for i in str(x)]
            ln = len(l)
            if ln > 1:
                if ln % 2 == 0:  # Even
                    h = int(ln / 2)
                    h1 = l[0:h]
                    h2 = l[-h:]
                else:  # Odd
                    h = int((ln - 1) / 2)
                    h1 = l[0:h]
                    h2 = l[-h:]

                return h1 == list(reversed(h2))
            else:
                return True
        else:
            return False


if __name__ == '__main__':
    s = Solution()
    print(s.isPalindrome(1001))
