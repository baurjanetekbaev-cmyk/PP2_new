n=int(input())
d={}
for i in range(n):
    num=input()
    if num in d:
        d[num]+=1
    else:
        d[num]=1
a=0
for j in d:
    if d[j]==3:
        a+=1
print (a)