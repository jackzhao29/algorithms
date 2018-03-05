# -*- coding: utf-8 -*-
"""
选择排序
"""

__author__ = "coldface"
__date__ = "2018-03-05"


#找出数组中最新元素的函数
def findSmallest(arr):
	smallest = arr[0] #存储最小的值
	smallest_index = 0 #存储最小元素的索引
	for i in range(1, len(arr)):
		if arr[i] < smallest:
			smallest = arr[i]
			smallest_index = i
	return smallest_index

#选择排序算法
def selectionSort(arr):
	newArr = []
	for i in range(len(arr)):
		#找出数组中最小的元素，并将其加入到新的数组中
		smallest = findSmallest(arr)
		newArr.append(arr.pop(smallest))
	return newArr

print selectionSort([5,3,6,2,10])