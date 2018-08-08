#coding=utf-8
"""
Written by zxcode-123
------------------------------------------------------------
Usage:选择排序
"""
from generateNearlyOrdered import generateNearlyOrderedArray

def selectionSort(alist):
    n = len(alist)

    for i in range(n-1):
        minIndex = i
        for j in range(i+1,n):
            if(alist[j]<alist[minIndex]):
                minIndex = j
        alist[i],alist[minIndex] = alist[minIndex],alist[i]
    return alist

def test():
    arr = generateNearlyOrderedArray(10,10)
    print(arr)
    alist = selectionSort(arr)
    print("------------------------------------------")
    print(alist)

if __name__ == '__main__':
    test()