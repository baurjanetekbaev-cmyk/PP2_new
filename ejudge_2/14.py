a=int(input())
n=[]
res=0
s=input().split()
for i in range(a):
    n.append(int(s[i]))
for j in range(a):
    count=n.count(n[j])
    if count>res:
        res=count
        m=n[j]
    elif count==res:
        m=min(m,n[j])


print(m)