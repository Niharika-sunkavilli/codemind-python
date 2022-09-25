n=int(input())
f=0
g=0
c=0
while(n>0):
    rem=n%10
    c+=1
    if(rem%2==0):
        f+=1
    elif(rem%2!=0):
        g+=1
    
    n=n//10
        
if(f==c):
    print("Even")
elif(g==c):
    print("Odd")
else:
    print("Mixed")




