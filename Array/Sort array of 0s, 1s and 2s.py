# -*- coding: utf-8 -*-
"""
Created on Fri Aug  6 18:35:11 2021

@author: arpit
"""
# Sort an array of 0s, 1s and 2s.
# Variation of famous Dutch national flag problem.

n=int(input())
a = list(map(int,input().split()))[:n]
def sortt(a,n):
	low=0
	high= n-1
	mid=0
	while mid <= high:
		if a[mid] == 0:
			a[low], a[mid] = a[mid], a[low]
			low = low + 1
			mid = mid + 1
		elif a[mid] == 1:
			mid = mid + 1
		else:
			a[mid], a[high] = a[high], a[mid]
			high = high - 1
	return a

print(sortt(a,n))
			