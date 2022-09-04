m=int(input())
n=int(input())
sum=0
for i in range(1,m//2+1):
    if(m%i==0):
        sum+=i
if(sum==n):
    print("Amicable")
else:
    print("Not Amicable")