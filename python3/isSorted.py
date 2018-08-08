#coding=utf-8
"""
Written by zxcode-123
------------------------------------------------------------
Usage:判断数列是否有序（算法是否正确）
"""
from generateNearlyOrdered import generateNearlyOrderedArray
def isSortedArray(alist):
    for i in range(0,len(alist)-1):
        if(alist[i]>alist[i+1]):
            return False
        return True


def test():
    # 有序
    # arr = generateNearlyOrderedArray(10,0)
    # 无序
    arr = generateNearlyOrderedArray(10,3)
    flag = isSortedArray(arr)
    print(flag)

if __name__ == '__main__':
    test()
