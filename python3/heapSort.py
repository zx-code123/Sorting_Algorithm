#coding=utf-8
"""
Written by zxcode-123
------------------------------------------------------------
Usage:堆排序
"""
from generateNearlyOrdered import generateNearlyOrderedArray

def heap(alist,length,index):
    left = 2*index + 1
    right = 2*index + 2
    maxId = index
    if(left < length and alist[left] > alist[maxId]):
        maxId = left
    if(right < length and alist[right] > alist[maxId]):
        maxId = right
    if(maxId != index):
        alist[maxId],alist[index] = alist[index],alist[maxId]
        heap(alist,length,maxId)

def heapSort(alist,length):
    for i in range(length//2-1,-1,-1):
        heap(alist,length,i)
    for i in range(length-1,-1,-1):
        alist[0],alist[i] = alist[i],alist[0]
        heap(alist,i,0)
    return alist

def test():
    arr = generateNearlyOrderedArray(10,10)
    print(arr)
    alist = heapSort(arr,10)
    print("------------------------------------------")
    print(alist)

if __name__ == '__main__':
    test()