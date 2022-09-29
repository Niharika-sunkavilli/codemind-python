n=input()
c=0
for i in n:
    if i.isspace():
        continue
    else:
        c+=1
print(c)