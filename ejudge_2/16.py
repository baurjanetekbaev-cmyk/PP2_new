a=int(input())
n=[]
s=input().split()
for i in range(a):
    n.append(int(s[i]))
c=set()
for x in n:
    if x in c:
        print("NO")
    else:
        print("YES")
        c.add(x)