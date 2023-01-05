n=input()
s=n[::-1]
a=""
for i in range(len(s)):
    if s[i]!=' ':
        a=s[i]+a
    else:
        print(a,end=" ")
        a=""
print(a)
