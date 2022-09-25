n=int(input())
a=0
for i in range(1,n):
    if(i*(i+1)==n):
        a=1
        break
if(a==1):
    print("YES")
else:
    print("NO")