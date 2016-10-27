#!/usr/bin/python3
# -*- coding:utf-8 -*-


class Solution(object):
    def twoSum(self, nums, target):
        length = len(nums)
        research = {}
        for i in range(0, length, 1):
            if target - nums[i] in research:
                return [research[target - nums[i]], i]
            else:
                research[nums[i]] = i
