n=int(input())
f=0
for i in range(1,n):
    if n==i*i:
        f=1
if(f==1):
    print(True)
else:
    print(False)