from collections import defaultdict


class Solution(object):
    def movesToStamp(self, stamp, target):
        """
        :type stamp: str
        :type target: str
        :rtype: List[int]
        """
        moves = []
        max_iterations = 10 * len(target)
        iterations = 0
        restart = True

        subs = defaultdict(list)
        for i in range(1, len(stamp) + 1):
            for j in range(len(stamp)):
                for k in range(j + 1, len(stamp) + 1):
                    if len(stamp[j:k]) == i:
                        subs[i].append('?' * j + stamp[j:k] + '?' * (len(stamp) - k))
        print(subs)

        while restart:
            restart = False
            for k, v in sorted(subs.items(), reverse=True):
                if restart:
                    break
                else:
                    for s in v:
                        idx = target.find(s)
                        if idx > -1:
                            restart = True
                            target = self.doStamp(target, stamp, idx)
                            moves.append(idx)
                            iterations += 1
                            print(target)
                            if target == '?' * len(target):
                                moves.reverse()
                                return moves
                            elif iterations > max_iterations:
                                return []

        return []

    def doStamp(self, s, stamp, index):
        return s[:index] + '?' * len(stamp) + s[index + len(stamp):]


if __name__ == '__main__':
    sol = Solution()

    # print(sol.movesToStamp('oz', 'ooozz'))
    # print(sol.movesToStamp('cab', 'cabbb'))
    # print(sol.movesToStamp('abca', 'aabcaca'))
    # print(sol.movesToStamp('e', 'eeeeeeeeee'))
    print(sol.movesToStamp('uskh', 'uskhkhhskh'))
    # print(sol.movesToStamp('aaca', 'aaaacaaaca'))
    # print(sol.movesToStamp('ffebb', 'fffeffebbb'))
    # print(sol.movesToStamp('k', 'kkkkkkkkkkkkkkk'))
    # print(sol.movesToStamp('ffc', 'ffffcfffffffffc'))
    # print(sol.movesToStamp('dfe', 'ddfdfedfdfeefee'))
    # print(sol.movesToStamp('babefafaea', 'bababefafaeaaea'))
    # print(sol.movesToStamp('babe', 'babeabeabebabbbabeee'))
    # print(sol.movesToStamp('uzavnaucpu', 'uzuzuzavnaucpuu'))
    # print(sol.movesToStamp('febe', 'febeebfebebeefebebee'))
    # print(sol.movesToStamp('bfedb', 'bfedbfedbdbfedbdbbdb'))
    # print(sol.movesToStamp('abeba', 'aabebabebabebaaebaaa'))
    # print(sol.movesToStamp('scpkdxyxnwfhxpf', 'scpkdxyxnwfhxpfffpff'))
    # print(sol.movesToStamp('bbbbb', 'bbbbbbbbbbbbbbb'))
    # print(sol.movesToStamp('bfb', 'bbbbfbbfbbfbbfbbfbbbfbfbb'))
    # print(sol.movesToStamp('aye', 'eyeye'))
