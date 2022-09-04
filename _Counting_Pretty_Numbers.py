def pretty(n):
    while(n>0):
        rem=n%10
        if(rem==2 or rem==3 or rem==9):
            return True
        else:
            return False
t=int(input())
for i in range(t):
    c=0
    a,b=map(int,input().split())
    for i in range(a,b+1):
        if(pretty(i)):
            c+=1
    print(c)