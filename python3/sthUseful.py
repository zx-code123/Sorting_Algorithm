#coding=utf-8
"""
Written by zxcode-123
------------------------------------------------------------
Usage:测试算法性能（耗费时间）
"""
from isSorted import isSortedArray

t1 = timeit.Timer('testSort("某种排序算法函数", alist)', 'from __main__ import testSort, 某种排序算法函数, alist')
print('某种排序算法：%s s' %t1.timeit(number=1))

# func表示要检测的算法函数，alist为传入的数列
def testSort(func, alist):
  alist =  func(alist)
  assert isSortedArray(alist), "排序算法错误\n"


# 数列中元素相互交换

# Python 语言对于交换两个数列的元素非常简单：
alist[i], alist[j] = alist[j], alist[i]

# 数列的拷贝

# 对于数列的拷贝，在 Python 语言中可以直接使用数列的切片：
# 直接使用切片
# list = [8,6,2,3,1,5,7,4]
alist=list[:]
