m,n=map(int,input().split())
a=[]
max=0
for i in range(m):
    l=list(map(int,input().split()))
    a.append(l)
for i in range(m):
    sum=0
    for j in range(n):
        sum+=a[i][j]
            
    if(sum>max):
        max=sum
print(max)