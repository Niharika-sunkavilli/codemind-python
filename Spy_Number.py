n=int(input())
p=1
s=0
while(n>0):
    rem=n%10
    p=p*rem
    s=s+rem
    n=n//10
    
if(p==s):
    print("Spy Number")
else:
    print("Not Spy Number")