#!/usr/bin/python3
# -*- coding:utf-8 -*-


class Solution(object):
    def convert(self, s, numRows):
        """
        :type s: str
        :type numRows: int
        :rtype: str
        """
        i = 0
        length = len(s)
        if length <= 2 or numRows == 1:
            return s
        ans = ''

        ans = ans + s[0::2 * (numRows - 1)]
        i = 1
        while(i <= numRows - 2):
            index = i
            while(index < length):
                ans += s[index]
                offset = 2 * (numRows - 2 - i + 1)
                if index + offset < length:
                    ans += s[index + offset]
                index += 2 * (numRows - 1)
            i += 1
        ans = ans + s[numRows - 1::2 * (numRows - 1)]

        return ans
