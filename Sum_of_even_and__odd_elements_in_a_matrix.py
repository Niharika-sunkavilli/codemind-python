m,n=map(int,input().split())
even=odd=0
for i in range(m):
    l=list(map(int,input().split()))
    for i in range(n):
        if l[i]%2==0:
            even+=l[i]
        else:
            odd+=l[i]
print(even,odd)