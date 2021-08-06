n=int(input())
a = list(map(int,input().split()))[:n]
p=0
q=len(a)-1
while p<q:
	a[p],a[q]=a[q],a[p]
	p=p+1
	q=q-1
print(a) 