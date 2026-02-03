a=int(input())
n=[]
b=1
add=input().split()
for i in range(a):
    n.append(int(add[i]))
max=n[0]
for j in range(1,a):
    if(max<n[j]):
        max=n[j]
        b=j+1
print(b)