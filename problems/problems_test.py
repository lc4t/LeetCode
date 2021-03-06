#!/usr/bin/python3
# -*- coding:utf-8 -*-
import nose
from problems.No1_Two_Sum import Solution as No1
from problems.No2_Two_Numbers import Solution as No2
from problems.No3_Longest_Substring_Without_Repeating_Characters \
    import Solution as No3
from problems.No4_Median_of_Two_Sorted_Arrays import Solution as No4
from problems.No5_Longest_Palindromic_Substring import Solution as No5
from problems.No6_ZigZag_Conversion import Solution as No6
from problems.No7_Reverse_Integer import Solution as No7
from problems.No8_String_to_Integer_atoi import Solution as No8
from problems.No9_Palindrome_Number import Solution as No9
from problems.No10_Regular_Expression_Matching import Solution as No10
from problems.No11_Container_With_Most_Water import Solution as No11
from problems.No292_Nim_Game import Solution as No292
from problems.No344_Reverse_String import Solution as No344
from problems.No371_Sum_of_Two_Integers import Solution as No371
from problems.No412_Fizz_Buzz import Solution as No412
from problems.No136_Single_Number import Solution as No136


def checkto1(func, ans, *key):
    test = func(*key)
    Message = ''
    for i in range(0, len(key), 1):
        Message += 'input%d: %s\n' % (i, str(key[i]))
    Message += 'expected: %s\n' % str(ans)
    Message += 'my: %s\n' % str(test)
    print(Message)
    assert test == ans


def test_1():
    func = No1().twoSum
    checkto1(func, [0, 1], [2, 7, 11, 15], 9)
    checkto1(func, [1, 2], [3, 2, 4], 6)
    checkto1(func, [0, 3], [0, 4, 3, 0], 0)
    checkto1(func, [2, 4], [-1, -2, -3, -4, -5], -8)

# Definition for singly-linked list.


class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None


class MakeList(object):
    def __init__(self, li):
        self.node_list = []
        for i in li:
            self.node_list.append(ListNode(i))
        length = len(self.node_list)
        for i in range(0, length - 1):
            self.node_list[i].next = self.node_list[i + 1]

    def get(self):
        return self.node_list[0]


def test_2():
    func = No2().addTwoNumbers

    l1 = MakeList([2, 4, 3]).get()
    l2 = MakeList([5, 6, 4]).get()
    checkto1(func, [7, 0, 8], l1, l2)

    l1 = MakeList([1, 8]).get()
    l2 = MakeList([0]).get()
    checkto1(func, [1, 8], l1, l2)


def test_3():
    func = No3().lengthOfLongestSubstring
    checkto1(func, 3, 'abcabcbb')
    checkto1(func, 1, 'bbbbb')
    checkto1(func, 3, 'pwwkew')


def test_4():
    func = No4().findMedianSortedArrays
    checkto1(func, 2.0, [1, 3], [2])
    checkto1(func, 2.5, [1, 2], [3, 4])
    checkto1(func, 1.0, [], [1])
    checkto1(func, 2.0, [1, 2], [1, 2, 3])
    checkto1(func, 2.0, [1], [2, 3])
    checkto1(func, 2.0, [3], [1, 2])
    checkto1(func, 2.5, [2], [1, 3, 4])
    checkto1(func, 2.5, [1], [2, 3, 4])
    checkto1(func, 3.5, [1, 2], [3, 4, 5, 6])
    checkto1(func, 2.5, [2, 4], [1, 3])
    checkto1(func, 3.5, [1, 2, 6], [3, 4, 5])
    checkto1(func, 3.5, [1, 4, 5], [2, 3, 6])
    checkto1(func, 3.0, [1, 2, 3, 4, 5], [1, 2, 3, 4, 5])


def test_5():
    func = No5().longestPalindrome
    checkto1(func, 'bab', 'babad')
    checkto1(func, 'bb', 'cbbd')
    checkto1(func, 'bb', 'bb')
    checkto1(func, 'b', 'b')
    checkto1(func, 'bb', 'abb')
    checkto1(func, 'tattarrattat', 'tattarrattat')


def test_6():
    func = No6().convert
    checkto1(func, 'PAHNAPLSIIGYIR', 'PAYPALISHIRING', 3)
    checkto1(func, '0817926354', '0123456789', 5)


def test_7():
    func = No7().reverse
    checkto1(func, 0, 0)
    checkto1(func, -321, -123)
    checkto1(func, 9, 900000)


def test_8():
    func = No8().myAtoi
    checkto1(func, 0, '')


def test_9():
    func = No9().isPalindrome
    checkto1(func, 0, -2147483648)


def test_10():
    func = No10().isMatch
    checkto1(func, False, 'aa', 'a')
    checkto1(func, True, 'aa', 'aa')
    checkto1(func, False, 'aaa', 'aa')
    checkto1(func, True, 'aa', 'a*')
    checkto1(func, True, 'aa', '.a')
    checkto1(func, True, 'ab', '.*')
    checkto1(func, True, 'aab', 'c*a*b')
    checkto1(func, True, 'aaa', 'aaa')
    checkto1(func, False, 'a', 'ab*a')
    checkto1(func, True, 'aaa', 'a*a')
    checkto1(func, False, 'aaba', 'ab*a*c*a')
    checkto1(func, True, 'bbbba', '.*a*a')
    checkto1(func, True, 'ab', '.*..')
    checkto1(func, True, 'ab', '.*..c*')
    checkto1(func, True, 'abbabaaaaaaacaa', 'a*.*b.a.*c*b*a*c*')


def test_11():
    func = No11().maxArea
    checkto1(func, 1, [1, 1])


def test_136():
    func = No136().singleNumber
    checkto1(func, 1, [1])


def test_292():
    func = No292().canWinNim
    checkto1(func, True, 1)
    checkto1(func, True, 2)
    checkto1(func, True, 3)
    checkto1(func, False, 4)
    checkto1(func, True, 5)
    checkto1(func, True, 6)
    checkto1(func, True, 7)
    checkto1(func, False, 8)


def test_344():
    func = No344().reverseString
    checkto1(func, 'olleh', 'hello')


def test_371():
    func = No371().getSum
    checkto1(func, -2, -1, -1)
    checkto1(func, 3, 1, 2)
    checkto1(func, 0, -1, 1)
    checkto1(func, 2, 3, -1)


def test_412():
    func = No412().fizzBuzz
    ans = [
        "1",
        "2",
        "Fizz",
        "4",
        "Buzz",
        "Fizz",
        "7",
        "8",
        "Fizz",
        "Buzz",
        "11",
        "Fizz",
        "13",
        "14",
        "FizzBuzz"]
    checkto1(func, ans, 15)


if __name__ == '__main__':
    nose.runmodule()
