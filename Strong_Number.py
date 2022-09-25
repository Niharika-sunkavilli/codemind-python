n=int(input())
a=n
sum=0
while(n>0):
    rem=n%10
    f=1
    for i in range(1,rem+1):
        f=f*i
    sum+=f
    n=n//10

if(a==sum):
    print("The number", a ,"is a strong number")
else:
    print("The number", a ,"is not a strong number")