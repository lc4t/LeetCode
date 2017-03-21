#!/usr/bin/python3
# -*- coding:utf-8 -*-


class Solution(object):
    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: str
        """
        n = len(s)
        i = 0
        self.ans = ''
        if s == s[::-1]:
            return s
        while(i < 2 * n - 1):
            index = i // 2
            # print('start pos %d' % i)
            if i % 2 == 0:
                substr = s[index]
                offset = 0
                while(self.check(substr)):
                    offset += 1
                    left = index - offset
                    if left < 0:
                        break
                    right = index + offset
                    if right > n:
                        break
                    substr = s[left:right + 1]
                    # print('[%d]%s[%d:%d]=%s' % (i, s, left, right, substr))
            else:
                offset = 0
                substr = s[index:index + 2]
                while(self.check(substr)):
                    offset += 1
                    left = index - offset
                    if left < 0:
                        break
                    right = index + 2 + offset
                    if right > n:
                        break
                    substr = s[left:right]
                    # print('[%d]%s[%d:%d]=%s' % (i, s, left, right, substr))
            i += 1
        return self.ans

    def check(self, substr):
        # print('check: %s' % substr)
        if len(substr) == 1:
            b = True
        else:
            b = substr[::-1] == substr
        if b is True and len(substr) > len(self.ans):
            # print('update %s->%s' % (self.ans, substr))
            self.ans = substr
        return b

# a = Solution()
# a.longestPalindrome('tattarrattat')
