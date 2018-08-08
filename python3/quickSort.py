#coding=utf-8
"""
Written by zxcode-123
------------------------------------------------------------
Usage:归并排序
"""
from generateNearlyOrdered import generateNearlyOrderedArray
from random import randint
# 方法一  随机去基准点pivot
def quickSort1(alist,left,right):
    

    mid = partitionQS(alist, left,right)

    quickSort(alist,left,mid-1)
    quickSort(alist,mid+1,right)
    return alist

def partitionQS(alist, left,right):
    pos = randint(left,right)
    alist[pos],alist[left] = alist[left],alist[pos]
    v = alist[left]
    i = left
    j = left + 1
    while(j<=r):
        if(alist[j]<v):
            alist[j],alist[i+1] = alist[i+1],alist[j]
            i = i +1
        j = j + 1
    alist[left],alist[i] = alist[i],alist[left]
    return i

# 方法一  三数取中(基准点pivot)
def quickSort(alist,left,right):
    dealPivot(alist,left,right)
    i = left
    j = right
    v = alist[right-1]
    while(i <= j):
        while(alist[i] < v):
            i = i+1
        while(alist[j]>v):
            j = j - 1
        alist[i],alist[j] = alist[j],alist[i]
        i = i +1
        j = j-1
    if(left < j):
        quickSort(alist,left,j);
    if(right>i):
        quickSort(alist,i,right)
    return alist

def dealPivot(alist,left,right):
    mid = (left+right)//2
    if(alist[left]>alist[mid]):
        alist[left],alist[mid] = alist[mid],alist[left]
    if(alist[left]>alist[right]):
        alist[left],alist[right] = alist[right],alist[left]
    if(alist[mid]>alist[right]):
        alist[mid],alist[right] = alist[mid],alist[right]
    alist[mid],alist[right-1] = alist[mid],alist[right-1]


def test():
    arr = generateNearlyOrderedArray(10,10)
    print(arr)
    alist = quickSort(arr,0,9)
    print("------------------------------------------")
    print(alist)

if __name__ == '__main__':
    test()
