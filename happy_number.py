n=int(input())
while True:
    sum=0
    rem=0
    if n>=0 and n<=9:
        if(n==1 or n==7):
            print(True)
            break
        else:
            print(False)
            break
    else:
        while n>0:
            rem=n%10
            n=n//10
            sum=sum+rem*rem
        n=sum