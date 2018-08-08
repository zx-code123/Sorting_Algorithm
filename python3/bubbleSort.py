#coding=utf-8
"""
Written by zxcode-123
------------------------------------------------------------
Usage:冒泡排序
"""
from generateNearlyOrdered import generateNearlyOrderedArray
# 初始版本
def bubbleSort(alist):
    n = len(alist)
    for i in range(n-1,0,-1):
        for j in range(i):
            if(alist[j]>alist[j+1]):
                alist[j],alist[j+1] = alist[j+1],alist[j]
    return alist
# 改进版本
def bubbleSortPlus(alist):
    n = len(alist)
    exchange = False
    for i in range(n-1,0,-1):
        for j in range(i):
            if(alist[j]>alist[j+1]):
                alist[j],alist[j+1] = alist[j+1],alist[j]
        # 如果发现整个排序过程中没有交换，提前结束
        if not exchange:
            break
    return alist
def test():
    arr = generateNearlyOrderedArray(10,10)
    print(arr)
    alist = bubbleSort(arr)
    print("------------------------------------------")
    print(alist)

if __name__ == '__main__':
    test()