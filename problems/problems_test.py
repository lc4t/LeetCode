#!/usr/bin/python3
# -*- coding:utf-8 -*-
import nose
from problems.No1_Two_Sum import Solution as No1
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
    "FizzBuzz"
    ]
    checkto1(func, ans, 15)




if __name__ == '__main__':
    nose.runmodule()
