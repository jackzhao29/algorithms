#coding:utf-8
"""
调用栈
"""

__author__ = "coldface"
__date__ = "2018-03-11"

def bye():
	print "ok bye!"

def greet1(name):
	print "how are you, "+name+"?"

def greet(name):
	print "hello, "+name+"!"
	greet1(name)
	print "greeting ready to say bye..."
	bye()

def fact(x):
	if x == 1:
		return 1
	else:
		return x * fact(x-1)

if __name__ == '__main__':
	greet("测试")