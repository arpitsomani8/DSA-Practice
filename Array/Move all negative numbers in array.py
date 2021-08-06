# -*- coding: utf-8 -*-
"""
Created on Fri Aug  6 21:29:10 2021

@author: arpit
"""


n=int(input())
a = list(map(int,input().split()))[:n]
def negative(a,n) :
	j = 0
	for i in range(0, n) :
		if (a[i] < 0) :
			 temp = a[i]
			 a[i] = a[j]
			 a[j]= temp
			 j = j + 1
	return a
	
print(negative(a,n))
