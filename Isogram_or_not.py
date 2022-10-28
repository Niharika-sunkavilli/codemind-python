n=input()
c=0
for i in range(len(n)):
    if(n.count(n[i])==1):
        c+=1
if(c==len(n)):
    print("True")
else:
    print("False")