# -*- coding:utf-8 -*-

"""
# @Datetime    : 2018/5/14 下午5:31
# @Author      : fanchunke
# @File        : binary_search.py
# @Description :
                可以使用
                `python binary_search.py ../data/tinyW.txt ../data/tinyT.txt`
                进行测试
"""

import sys


class BinarySearch(object):

    def __init__(self):
        pass

    @classmethod
    def rank(cls, key, array_list):
        if not isinstance(array_list, list):
            raise Exception("not a valid list")

        lo = 0
        hi = len(array_list) - 1
        while (lo <= hi):
            mid = lo + (hi - lo) / 2
            if key < array_list[mid]:
                hi = mid - 1
            elif key > array_list[mid]:
                lo = mid + 1
            else:
                return mid

        return -1


if __name__ == '__main__':

    white_file = sys.argv[1]
    key_file = sys.argv[2]

    with open(white_file) as wf:
        white_list = [int(line.strip("\n")) for line in wf.readlines()]
        white_list = sorted(white_list)

    with open(key_file) as kf:
        key_list = [int(line.strip("\n")) for line in kf.readlines()]

    for key in key_list:
        if BinarySearch.rank(key, white_list) < 0:
            print key
