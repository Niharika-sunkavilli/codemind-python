n=int(input())
a=0
b=1
while(b<n):
    c=a+b
    a=b
    b=c
    
if(n-a==b-n):
    print(a,b)
elif(n-a>b-n):
    print(b)
else:
    print(a)