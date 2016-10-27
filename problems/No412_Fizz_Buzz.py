#!/usr/bin/python3
# -*- coding:utf-8 -*-


class Solution(object):
    def fizzBuzz(self, n):
        ans = []
        for i in range(1, n + 1):
            s = ''
            if i % 3 == 0:
                s = 'Fizz'
            if i % 5 == 0:
                s += 'Buzz'
            if s == '':
                s = str(i)
            ans.append(s)
        return ans
