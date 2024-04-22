a=input()
p=[]
for i in range(len(a)):
    for j in range(1,len(a)+1):
        b=a[i:j]
        c=b[::-1]
        if b==c and b != "":
            p.append(b)
p=set(p)
p=list(p)
print(p)