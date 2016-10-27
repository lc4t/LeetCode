#!/usr/bin/python3
# -*- coding:utf-8 -*-


class Solution(object):
    def canWinNim(self, n):
        if n % 4 == 0:
            return False
        else:
            return True
