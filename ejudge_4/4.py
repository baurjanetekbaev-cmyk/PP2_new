def num(a,b):
    for i in range(a,b+1):
        yield i*i
a,b=map(int,input().split())
for x in num(a,b):
    print(x,end="\n")