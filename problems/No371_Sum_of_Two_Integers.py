#!/usr/bin/python3
# -*- coding:utf-8 -*-


class Solution(object):
    def getSum(self, a, b):
        MAX_INT = 0x7FFFFFFFFFFFFFF
        # MIN_INT = 0x800000000000000
        MASK = 0x1000000000000000

        while (b):
            s = (a ^ b) % MASK
            c = ((a & b) << 1) % MASK
            a, b = s, c
        if a <= MAX_INT:
            return a
        else:
            return a | (~MASK + 1)
