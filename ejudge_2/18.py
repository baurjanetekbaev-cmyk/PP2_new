a=int(input())
n={}
for i in range(1,a+1):
    s=input()
    if s not in n:
        n[s]=i
for key in sorted(n):
    print(key,n[key]) 