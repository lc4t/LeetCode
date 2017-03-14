#!/usr/bin/python3
# -*- coding:utf-8 -*-


class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        left = 0
        right = 0
        ans = 0
        current = 0
        hash_map = {}
        length = len(s)
        left = 0
        for i in range(0, length):
            right = i
            if left == right:
                current = 1     # now ans
                hash_map[s[right]] = right  # store path
                ans = ans if ans >= current else current    # update ans
                continue
            if s[right] in hash_map:
                left = hash_map[s[right]] + 1   # left start in here
                hash_map = {}
                for i in range(left, right + 1):    # update hashmap
                    hash_map[s[i]] = i
                current = right - left + 1
                ans = ans if ans >= current else current
                continue
            else:
                hash_map[s[right]] = right
                current = right - left + 1
                ans = ans if ans >= current else current
        return ans
