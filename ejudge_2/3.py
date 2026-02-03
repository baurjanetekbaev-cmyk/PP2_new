a=int(input())
n=[]
nums=input().split() #we can write in one line
for i in range(a):
    n.append(int(nums[i]))
    
print (sum(n))