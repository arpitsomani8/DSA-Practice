# -*- coding: utf-8 -*-
"""
Created on Sat Aug  7 15:09:51 2021

@author: arpit
"""

m,n=map(int,input().split())
a=list(map(int,input().split()))[:n]
b=list(map(int,input().split()))[:m]
uni=[]
inte=[]

def printUnion(a, b, m, n):
    i, j = 0, 0
    while i < m and j < n:
        if a[i] < b[j]:
            uni.append(a[i]) 
            i += 1
        elif b[j] < a[i]:
            uni.append(b[j])
            j+= 1
        else:
            uni.append(b[j])
            j += 1
            i += 1
 
    while i < m:
         uni.append(a[i])
         i += 1
 
    while j < n:
        uni.append(b[j])
        j += 1
    print("Union: ",uni)
    
def printIntersection(a, b, m, n):
    i, j = 0, 0
    while i < m and j < n:
        if a[i] < b[j]:
            i += 1
        elif b[j] < a[i]:
            j+= 1
        else:
            inte.append(b[j])
            print("Intersection: ",inte)
            j += 1
            i += 1
			
        
printUnion(a,b,m,n)
printIntersection(a,b,m,n)