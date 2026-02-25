def num(a):
    for i in range(1,a+1):
        yield i**2
n=int(input())
for x in num(n):
    print(x)



