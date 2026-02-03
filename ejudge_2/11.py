a=input().split()
n=[]
for i in range(3):
    n.append(int(a[i]))

r1=n[1]-1
r2=n[2]-1

b=input().split()
sum =n[0]
n1=[]
for j in range(sum):
    n1.append(int(b[j])) 
while r1<r2:
    n1[r1],n1[r2]=n1[r2],n1[r1]
    r1+=1
    r2-=1
for x in n1:
    print(x,end=" ")