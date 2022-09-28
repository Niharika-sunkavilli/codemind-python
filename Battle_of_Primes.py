def prime(n):
    c=0
    if n==1:
        return False
    for i in range(2,n):
        if(n%i==0):
            c+=1
    if c==0:
        return True
    else:
        return False

m=int(input())
n=int(input())
a=m+n
i=a+1
while True:
    if(prime(i)):
        a=i
        break
    i+=1
print(i-(m+n))