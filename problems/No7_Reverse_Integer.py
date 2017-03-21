#!/usr/bin/python3
# -*- coding:utf-8 -*-


class Solution(object):
    def reverse(self, x):
        """
        :type x: int
        :rtype: int
        """
        MAX = 0x7fffffff
        MIN = ~0x7fffffff

        x = str(x)
        if x[0] == '-':
            ans = '-' + x[1:][::-1]
        else:
            ans = x[::-1]
        ans = int(ans)
        if ans > MAX or ans < MIN:
            return 0
        else:
            return ans
