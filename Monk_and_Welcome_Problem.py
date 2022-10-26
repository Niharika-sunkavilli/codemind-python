a=int(input())
m=list(map(int,input().split()))
n=list(map(int,input().split()))
for i in range(len(m)):
    s=0
    for j in range(len(n)):
        s=m[i]+n[i]
    print(s,end=" ")