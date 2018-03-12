#coding:utf-8


"""
列表元素求和
"""
def sum(arr):
	total = 0
	for n in arr:
		total += n
	return total

print sum([2,3,5])

"""
计算列表元素个数


defined = 'count' in globals()
def number(arr):
	if(len(arr) == 0):
		return count
	arr.pop()
	count = count + 1
	number(arr)

print number([3,4,2,5,8])
"""

"""
输出列表中最大的元素
"""
def find(arr):
	max = arr[0]
	for n in arr:
		if (max < n):
			max = n
	return max

print find([6,2,5,3,9,1])

"""
快排
"""
def quicksort(array):
	if len(array) < 2:
		return array
	else:
		pivot = array[0]
		less = [i for i in array[1:] if i <= pivot]
		greater = [i for i in array[1:] if i > pivot]

	return quicksort(less) + [pivot] + quicksort(greater)

print quicksort([8,2,6,4,7,5,1]) 
