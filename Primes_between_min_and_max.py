def prime(n):
    if n==1:
        return False
    c=0
    for i in range(2,n//2+1):
        if n%i==0:
            c+=1
    if c==0:
        return True
    else:
        return False

n=int(input())
l=list(map(int,input().split()))
x=min(l)
x1=l.index(x)
y=max(l)
y1=l.index(y)
c=0
for i in range(n):
    if(i>=x1 and i<=y1) or (i>=y1 and i<=x1):
        if(prime(l[i])):
            c+=1;
print(c)