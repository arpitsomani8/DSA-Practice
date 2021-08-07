# -*- coding: utf-8 -*-
"""
Created on Sat Aug  7 21:25:55 2021

@author: arpit
"""

n=int(input())
a=list(map(int,input().split()))[:n]

def rotate(a, n):
    i = 0
    j = n - 1
    while i!= j:
      a[i], a[j] = a[j], a[i]
      i+=1
    pass

rotate(a,n)
print(*a)