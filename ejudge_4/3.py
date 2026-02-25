def num(a):
    for i in range(a+1):
        if i%12==0:
            yield i
a=int(input())
for x in num(a):
    print(x,end=" ")