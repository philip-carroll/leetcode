class Solution(object):
    def findSubstrings(self, stamp, target):
        res = {}

        # first find all substrings
        for i in range(len(stamp)):
            for j in range(1, len(stamp) + 1):
                if j > i:
                    s = stamp[i:j]
                    idx = {it: (i, s) for it in range(len(target)) if target.startswith(s, it)}
                    if len(s) not in res:
                        res[len(s)] = {}
                    for k, v in idx.items():
                        # TODO: figure out how to find the right instance
                        # ensure the stamp won't spill over the start or end of the target
                        if (len(stamp) + k - v[0]) <= len(target) and k - v[0] >= 0:
                            # retain the first instance of the substring
                            if k not in res[len(s)]:
                                res[len(s)][k] = [v]
                            else:
                                res[len(s)][k].append(v)
        print('0: %s' % res)

        # seed rem with ????
        rem = {}
        for ik, iv in res.items():
            for jk, jv in iv.items():
                if ik not in rem:
                    rem[ik] = {}
                # rem[ik][jk] = (res[ik][jk][0], '?' * len(res[ik][jk][1]))
                rem[ik][jk] = [(r[0], '?' * len(r[1])) for r in res[ik][jk]]

        # then strip out substrings that completely overlap single substrings of greater length
        # for i in sorted(res.keys()):
        #     for ii, (ix, iv) in res[i].items():
        #         for j in sorted(res.keys()):
        #             for ji, (jx, jv) in res[j].items():
        #                 # is i longer than j and j contained within i?
        #                 if i > j and (ji in range(ii, ii + len(iv))) and (
        #                         ji + len(jv) - 1 in range(ii, ii + len(iv))):
        #                     rem[j][ji] = (jx, jv)
        # print('1: %s' % rem)

        for i in sorted(res.keys()):
            for ii, il in res[i].items():
                for (ix, iv) in il:
                    for j in sorted(res.keys()):
                        for ji, jl in res[j].items():
                            for (jx, jv) in jl:
                                # is i longer than j and j contained within i?
                                if i > j and (ji in range(ii, ii + len(iv))) and (
                                        ji + len(jv) - 1 in range(ii, ii + len(iv))):
                                    rem[j][ji] = (jx, jv)
        print('1: %s' % rem)

        # then strip out substrings that completely overlap multiple substrings of greater length
        for i in sorted(res.keys()):
            for ii, il in res[i].items():
                for (ix, iv) in il:
                    for j in sorted(res.keys()):
                        for ji, jl in res[j].items():
                            i = 0
                            for (jx, jv) in jl:
                                if i > j and '?' in rem[j][ji][i][1]:
                                    # is the start of j contained within i
                                    if (ji in range(ii, ii + len(iv))) and not (
                                            ji + len(jv) - 1 in range(ii, ii + len(iv))):
                                        iend = ii + len(iv)
                                        overlap = iend - ji
                                        s = '?' * (len(jv) - overlap)
                                        rem[j][ji] = (jx, 'x')
                                        rem[j - overlap][ji + overlap] = (jx + overlap, s)
                                        print('S: %s' % rem)

                                    # is the end of j contained within i
                                    if (ji + len(jv) - 1 in range(ii, ii + len(iv))) and not (
                                            ji in range(ii, ii + len(iv))):
                                        overlap = ii - ji
                                        s = '?' * (len(jv) - overlap)
                                        rem[j][ji] = (jx, 'x')
                                        rem[j - overlap][ji] = (jx + overlap, s)
                                        print('E: %s' % rem)
                            i = i + 1

        for ik, iv in rem.items():
            for jk, jv in iv.items():
                if '?' not in jv[1]:
                    del res[ik][jk]
                    if not res[ik]:
                        del res[ik]
                else:
                    if jv[1] != len(jv[1]) * '?':
                        # is j at start and last character is ?
                        if jk == 0 and jv[0] == 0 and jv[1][-1] == '?':
                            res[ik][jk] = (jv[0], jv[1][:-1])
                        # is j at end and first character is ?
                        elif jk + len(jv[1]) == len(target) and jv[1][0] == '?':
                            res[ik][jk + len(jv[1][:1])] = (jv[0] + len(jv[1][:1]), jv[1][1:])
                            del res[ik][jk]
                        else:
                            del res[ik][jk]
                            if not res[ik]:
                                del res[ik]

        return res

    def doStamp(self, s, stamp, index):
        return s[:index] + stamp + s[index + len(stamp):]

    def movesToStamp(self, stamp, target):
        """
        :type stamp: str
        :type target: str
        :rtype: List[int]
        """
        res = []
        iterations = 0
        s = '?' * len(target)
        substrings = self.findSubstrings(stamp, target)

        l = []
        for ik, iv in substrings.items():
            for jk, jv in iv.items():
                l.append((jk,) + jv)
                # l.append((14, 4, 'a'))
        print('L0: %s' % l)

        n = len(l)
        for i in range(n):
            for j in range(n):
                if i != j:
                    if i < j:
                        firstunique = list(range(l[i][0], l[i][0] + len(l[i][2])))
                        first = list(range(l[i][0] - l[i][1], l[i][0] - l[i][1] + len(stamp)))
                        secondunique = list(range(l[j][0], l[j][0] + len(l[j][2])))
                        second = list(range(l[j][0] - l[j][1], l[j][0] - l[j][1] + len(stamp)))
                    else:
                        firstunique = list(range(l[j][0], l[j][0] + len(l[j][2])))
                        first = list(range(l[j][0] - l[j][1], l[j][0] - l[j][1] + len(stamp)))
                        secondunique = list(range(l[i][0], l[i][0] + len(l[i][2])))
                        second = list(range(l[i][0] - l[i][1], l[i][0] - l[i][1] + len(stamp)))

                    if (firstunique[0] in second and first[0] > secondunique[0]) or (
                            firstunique[-1] in second and first[-1] < secondunique[-1]):
                        lj = l[j]
                        l[j] = l[i]
                        l.remove(l[i])
                        l.insert(i, lj)
                        print(i)
                        print(j)
                        print(first)
                        print(second)
                        print('L: %s' % l)

        for t in l:
            m = t[0] - t[1]
            res.append(m)
            s = self.doStamp(s, stamp, m)
            print(s)
            iterations += 1
            if iterations <= 10 * len(target):
                if s == target:
                    return res
            else:
                return []
        return []

    def testMoves(self, stamp, target, moves):
        s = '?' * len(target)

        for i in moves:
            s = self.doStamp(s, stamp, i)

        return s

        # last moves will be exact substring match
        # second last moves will be n-1 substrings
        # third last moves will be n-2 substrings

        # 'abca', 'aabcaca' |  'abc', 'ababc'
        # '???????'         |  '?????'

        # 0    n-3 a??????  |
        # 5    n-2 a??abca  |
        # None n-1          |  0 n-1 ab???
        # 1    n   aabcaca  |  2 n   ababc


if __name__ == '__main__':
    sol = Solution()

    # print(sol.findSubstrings('abca', 'aabcaca'))

    # print(sol.movesToStamp('oz', 'ooozz'))
    # print(sol.movesToStamp('cab', 'cabbb'))
    # print(sol.movesToStamp('abca', 'aabcaca'))
    # print(sol.movesToStamp('e', 'eeeeeeeeee'))
    # print(sol.movesToStamp('uskh', 'uskhkhhskh'))
    # print(sol.movesToStamp('aaca', 'aaaacaaaca'))  # has overlapping strings that need to be wiped
    # print(sol.movesToStamp('ffebb', 'fffeffebbb'))  # has overlapping strings that need to be sub-wiped
    # print(sol.movesToStamp('k', 'kkkkkkkkkkkkkkk'))
    # print(sol.movesToStamp('ffc', 'ffffcfffffffffc'))
    # print(sol.movesToStamp('dfe', 'ddfdfedfdfeefee'))
    # print(sol.movesToStamp('babefafaea', 'bababefafaeaaea'))
    # print(sol.movesToStamp('babe', 'babeabeabebabbbabeee'))
    # print(sol.movesToStamp('uzavnaucpu', 'uzuzuzavnaucpuu'))
    # print(sol.movesToStamp('febe', 'febeebfebebeefebebee'))
    # print(sol.movesToStamp('bfedb', 'bfedbfedbdbfedbdbbdb'))
    print(sol.movesToStamp('abeba', 'aabebabebabebaaebaaa'))

    # stamp = 'uzavnaucpu'
    # target = 'uzuzuzavnaucpuu'
    # print(sol.testMoves(stamp, target, [5, 0, 2, 4]))
