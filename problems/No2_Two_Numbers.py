#!/usr/bin/python3
# -*- coding:utf-8 -*-


class Solution(object):
    def addTwoNumbers(self, l1, l2):
        ans = []
        q = []
        q.append(0)
        flag = 0
        while(flag != 3):
            flag = 0
            if l1 is None:
                left_num = 0
                flag += 1
            else:
                left_num = l1.val
                l1 = l1.next
            if l2 is None:
                right_num = 0
                flag += 2
            else:
                right_num = l2.val
                l2 = l2.next
            add_ans = q.pop() + left_num + right_num
            if add_ans == 0 and flag == 3:
                break

            q.append(add_ans // 10)   # goto next digital
            ans.append(add_ans % 10)    # calc ans
        return ans
