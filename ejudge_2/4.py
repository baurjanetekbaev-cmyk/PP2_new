a=int(input())
n=[]
b=0
nums=input().split() #we can write in one line
for i in range(a):
    n.append(int(nums[i]))
    
for j in range(a):
    if(n[j]>0):
        b+=1
    else:
        b=b
print(b)