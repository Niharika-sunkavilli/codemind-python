m,n=map(int,input().split())
a=[]
max=0
for i in range(m):
    l=list(map(int,input().split()))
    a.append(l)
for i in range(n):
    sum=0
    for j in range(m):
        sum+=a[j][i]
    if(sum>max):
        max=sum
print(max)