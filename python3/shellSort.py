#coding=utf-8
"""
Written by zxcode-123
------------------------------------------------------------
Usage:希尔排序
"""
from generateNearlyOrdered import generateNearlyOrderedArray
# 方法一
def shellSort(alist):
    length = len(alist)
    n = length//2
    while(n>0):
        for i in range(n,length):
            temp = alist[i]
            for j in range(i,-1,-n):
                if(j<0):
                    break
                if(temp < alist[j-n]):
                    alist[j] = alist[j-n]               
                else:
                    break
            alist[j] = temp
        n = n//2
    return alist
# --------------------------------------------------------------------
# 方法二
def shellSort1(alist):
    n = len(alist)
    gap = n//2
    while(gap>0):
        for i in range(gap):
            gapInsetionSort(alist, i, gap)
        gap = gap//2
    return alist
# start子数列开始的起始位置， gap表示间隔
# 希尔排序的辅助函数
def gapInsetionSort(alist, start , gap):
    for i in range(start+gap,len(alist),gap):
        temp = alist[i]
        position = i
        while position > start and alist[position-gap]>temp:
            alist[position] = alist[position-gap]
            position = position-gap 
        alist[position] = temp
def test():
    arr = generateNearlyOrderedArray(10,10)
    print(arr)
    alist = shellSort1(arr)
    print("------------------------------------------")
    print(alist)

if __name__ == '__main__':
    test()
