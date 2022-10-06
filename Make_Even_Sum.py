n=int(input())
l=list(map(int,input().split()))
sum=0
for i in range(len(l)):
    sum+=l[i]
if(sum%2==0):
    print(1)
else:
    print(0)