# -*- coding: utf-8 -*-
"""
Created on Fri Aug  6 18:06:25 2021

@author: arpit
"""

n=int(input())
a = list(map(int,input().split()))[:n]
k_min=int(input())
k_max=int(input())
a.sort()
p=-1*k_max
val_k_min=a[k_min-1]
val_k_max=a[p]
print(val_k_min,val_k_max)