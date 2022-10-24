n=int(input())
l=list(map(int,input().split()))
e=o=0
for i in range(0,n):
    if i%2==0:
        e+=l[i]
        #print(i)
    else:
        o+=l[i]
        #print(".",i)
    
d=e-o
if d==0:
    print("YES")
else:
    print("NO")