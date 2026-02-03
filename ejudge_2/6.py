a=int(input())
n=[]
nums=input().split()
for i in range(a):
    n.append(int(nums[i]))

c=n[0]
for j in range(1,a):
    if(n[j]>c):
        c=n[j]
print(c)