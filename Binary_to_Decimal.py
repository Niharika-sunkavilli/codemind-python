t=int(input())
for i in range(t):
    n=input()
    a=n[::-1]
    l=list(a)
    s=0
    for i in range(len(a)):
        s=s+int(l[i])*pow(2,i)
    print(s)