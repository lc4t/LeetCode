#!/usr/bin/python3
# -*- coding:utf-8 -*-


class Solution(object):
    def findMedianSortedArrays(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: float
        """
        # print('1: %s' % str(nums1))
        # print('2: %s' % str(nums2))
        len1 = len(nums1)
        len2 = len(nums2)
        if len1 == 0:
            return self.get_median(len2, nums2)
        if len1 > len2:
            return self.findMedianSortedArrays(nums2, nums1)
        if len1 == 1 and len2 == 1:
            return (nums1[0] + nums2[0]) / (2 + 0.0)
        # len1 <= len2
        median_1 = self.get_median(len1, nums1)
        median_2 = self.get_median(len2, nums2)

        if len1 == 1:
            if len2 % 2 == 0:
                if nums1[0] < nums2[len2 // 2 - 1]:
                    return nums2[len2 // 2 - 1] + 0.0
                elif nums1[0] > nums2[len2 // 2]:
                    return nums2[len2 // 2] + 0.0
                else:
                    return nums1[0] + 0.0
            else:
                if nums1[0] < nums2[len2 // 2 - 1]:
                    return (nums2[len2 // 2 - 1] + nums2[len2 // 2]) / 2.0
                elif nums1[0] < nums2[len2 // 2 + 1]:  # true for last if
                    return (nums1[0] + nums2[len2 // 2]) / 2.0
                else:
                    return (nums2[len2 // 2] + nums2[len2 // 2 + 1]) / 2.0

        if len1 % 2 == 0 and len2 % 2 == 0:
            if nums1[len1 // 2 - 1] < nums2[len2 // 2 - 1] and \
                    nums1[len1 // 2] > nums2[len2 // 2]:
                return (nums2[len2 // 2 - 1] + nums2[len2 // 2]) / 2.0
            if nums2[len2 // 2 - 1] < nums1[len1 // 2 - 1] and \
                    nums2[len2 // 2] > nums1[len1 // 2]:
                return (nums1[len1 // 2 - 1] + nums1[len1 // 2]) / 2.0

        if median_1 == median_2:
            return median_1
        elif median_1 < median_2:
            return self.findMedianSortedArrays(nums1[len1 // 2:],
                                               nums2[0:len2 - len1 // 2])
        else:
            if len1 % 2 == 0:
                return self.findMedianSortedArrays(nums1[0:len1 // 2],
                                                   nums2[len1 // 2:])
            else:
                return self.findMedianSortedArrays(nums1[0:len1 // 2 + 1],
                                                   nums2[len1 // 2:])

    def get_median(self, length, nums):
        right = length // 2
        if right == 0:
            median = nums[0]
        elif length % 2 == 0:   # median is /2, /2 -1
            median = (nums[right] + nums[right - 1]) / 2.0
        else:   # length % 2 == 1
            median = nums[right]
        return median
