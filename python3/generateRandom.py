#coding=utf-8
"""
Written by zxcode-123
------------------------------------------------------------
Usage: 生成随机数列
"""
from random import randint

def generateRandomArray(n,min,max):
    arr = []
    arr = [randint(min,max) for x in range(n)]
    return arr

def test():
    arr = generateRandomArray(10,0,20)
    print(arr)

    
if __name__ == '__main__':
    test()
