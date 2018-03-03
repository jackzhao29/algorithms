# -*- coding: utf-8 -*-
"""
二分查找算法
"""
__author__ = "coldface"
__date__ = "2018-03-03"

def binary_search(list, item):
	low = 0
	heigh = len(list) - 1
	while low <= heigh:
		mid = (low + heigh) / 2
		guess = list[mid]
		if guess == item:
			return mid
		elif guess < item:
			low = mid + 1
		else:
			heigh = mid - 1
	return None

my_list = [12,16,23,25,28,30,31,35,40]
item = 30

print binary_search(my_list,item)