n=int(input())
l=list(map(int,input().split()))
a=[]
for i in range(0,n):
    c=l[i]*l[i]
    a.append(c)
#print(a)
a.sort()
for i in range(0,n):
    print(a[i],end=" ")
#print(a)