a=int(input())
n=[]
s=input().split()
for i in range(a):
    n.append(int(s[i]))
n.sort()
n.reverse()

for x in n:
    print(x,end=" ")