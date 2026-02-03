a=int(input())
n=[]
s=input().split()
for i in range(a):
    n.append(int(s[i]))
for x in n:
    print(pow(x,2),end=" ")