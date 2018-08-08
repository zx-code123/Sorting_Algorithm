#coding=utf-8
"""
Written by zxcode-123
------------------------------------------------------------
Usage:归并排序
"""
from generateNearlyOrdered import generateNearlyOrderedArray

def merge(left,right):
    temp = []
    i = j = 0
    while(i<len(left) and j<len(right)):
        if(left[i]<right[j]):
            temp.append(left[i])
            i = i + 1
        else:
            temp.append(right[j])
            j = j+1
    if(i == len(left)):
        for k in right[j:]:
            temp.append(k)
    else:
        for k in left[i:]:
            temp.append(k)
    return temp 

def mergeSort(alist):
    n = len(alist)
    mid = n//2
    if(n <= 1):
        return alist
    
    left = mergeSort(alist[:mid])
    right = mergeSort(alist[mid:])
    
    return merge(left,right)

def test():
    arr = generateNearlyOrderedArray(10,10)
    print(arr)
    alist = mergeSort(arr)
    print("------------------------------------------")
    print(alist)

if __name__ == '__main__':
    test()
