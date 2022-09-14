n=int(input())
sq=n*n
sum=0
while(sq>0):
    rem=sq%10
    sum=sum+rem;
    sq=sq//10
    
if(n==sum):
    print("Neon Number")
else:
    print("Not Neon Number")