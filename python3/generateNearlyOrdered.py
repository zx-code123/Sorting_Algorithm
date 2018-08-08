#coding=utf-8
"""
Written by zxcode-123
------------------------------------------------------------
Usage: 生成基本有序的数列
"""

from random import randint
def generateNearlyOrderedArray(n, swapTimes):
    """
    n: 生成基本有序的数列的长度
    swapTimes:随机交换次数(为0时不交换，那么为有序数列)
    """
    arr = []
    for i in range(n):
        arr.append(i)

    for j in range(swapTimes):
        posX = randint(0,n-1);
        posY = randint(0,n-1);
        arr[posX],arr[posY] = arr[posY],arr[posX]

    return arr

def test():
    arr = generateNearlyOrderedArray(10,10)
    print(arr)

    
if __name__ == '__main__':
    test()