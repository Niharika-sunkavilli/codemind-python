n,x=map(int,input().split())
#print(n,x)
z=n
c=0
while(n>0):
    rem=n%10
    c+=1
    n=n//10
#print(c)
a=z%(pow(10,x))
#print(a)
m=c-x
b=z//(pow(10,m))
#print(b)

print(abs(a-b))