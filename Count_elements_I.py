m,n=map(int,input().split())
a=list(map(int,input().split()))
b=list(map(int,input().split()))
z=[]
for i in range(len(a)):
    for j in range(len(b)):
        if(a[i]==b[j]):
            z.append(a[i])
x=set(z)
print(len(x))
