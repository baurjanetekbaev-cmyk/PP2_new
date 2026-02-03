a=int(input())
n=[]
add=input().split()
for i in range(a):
    n.append(int(add[i]))
max=n[0]
min=n[0]

for j in range(1,a):
    if(min>n[j]):
        min=n[j]
    if(max<n[j] ):
        max=n[j]
for c in range(a):
    if(n[c]==max):
        n[c]=min
for x in n:
    print(x,end=" ")
    