#!/usr/bin/python3
# -*- coding:utf-8 -*-
import string


class Solution(object):
    def myAtoi(self, s):
        """
        :type str: str
        :rtype: int
        """
        MAX = 2147483647
        MIN = -2147483648
        flag = ''
        ans = ''
        space = 0
        for i in s:
            if i == '-' or i == '+':
                if flag == '':
                    flag = i
                else:
                    return 0
            elif i == ' ':
                space += 1
                if space > 1 and (flag != '' or ans != ''):
                    break
            elif i in string.digits:
                ans += i
            elif i in string.ascii_letters:
                break
            else:
                continue
        ans = flag + ans
        if ans == '+' or ans == '-' or ans == '':
            return 0
        else:
            ans = int(ans)
        if ans > MAX:
            return MAX
        elif ans < MIN:
            return MIN
        else:
            return ans
