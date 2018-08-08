#coding=utf-8
"""
Written by zxcode-123
------------------------------------------------------------
Usage:插入排序
"""
from generateNearlyOrdered import generateNearlyOrderedArray

def insertionSort(alist):
    n = len(alist)
    for i in range(1,n):
        temp = alist[i]
        for j in range(i,-1,-1):
             # j为当前位置，试探j-1位置
            if(temp < alist[j-1]):
                alist[j] = alist[j-1]
            else:
                # 位置确定为j
                break
        alist[j] = temp
    return alist

def test():
    arr = generateNearlyOrderedArray(10,10)
    print(arr)
    alist = insertionSort(arr)
    print("------------------------------------------")
    print(alist)

if __name__ == '__main__':
    test()