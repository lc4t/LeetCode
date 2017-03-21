#!/usr/bin/python3
# -*- coding:utf-8 -*-


class Solution(object):
    def isMatch(self, s, p):
        """
        :type s: str raw string
        :type p: str re string
        :rtype: bool
        """
        lens = len(s)
        lenp = len(p)
        ans = [[False for i in range(lenp + 1)] for j in range(lens + 1)]

        ans[0][0] = True
        for i in range(0, lens + 1):
            for j in range(1, lenp + 1):
                print(i, j)
                if p[j - 1] == '*':
                    ans[i][j] = ans[i][j - 2] or (i > 0 and (
                        s[i - 1] == p[j - 2] or p[j - 2] == '.') and
                                                  ans[i - 1][j])
                else:
                    ans[i][j] = (i > 0) and ans[i - 1][j - 1] and \
                        (s[i - 1] == p[j - 1] or p[j - 1] == '.')
        return ans[lens][lenp]
