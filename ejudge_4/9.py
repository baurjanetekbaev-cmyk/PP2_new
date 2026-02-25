def num(a):
    for i in range(a+1):
        yield 2**i
a=int(input())
for x in num(a):
    print(x,end=" ")