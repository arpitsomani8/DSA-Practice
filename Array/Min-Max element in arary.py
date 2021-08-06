# -*- coding: utf-8 -*-
"""
Created on Fri Aug  6 17:53:08 2021

@author: arpit
"""

n=int(input())
a = list(map(int,input().split()))[:n]
maxx=max(a)
minn=min(a)
print(maxx,minn)