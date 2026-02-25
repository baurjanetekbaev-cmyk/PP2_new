def r(a):
    while 0<=a:
        yield a
        a=a-1
a=int(input())
for x in r(a):
    print(x)