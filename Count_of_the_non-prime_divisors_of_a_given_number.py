def isprime(n):
    c=0
    if n==1:
        return False
        
    for i in range(2,int(n**0.5)+1):
        if(n%i==0):
            c+=1
    if(c==0):
        return True
    else:
        return False

n=int(input())
c=0
for i in range(1,n+1):
    if(n%i==0):
        if(not(isprime(i))):
            c+=1
print(c)
        
