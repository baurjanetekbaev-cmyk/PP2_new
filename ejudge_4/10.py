def num(a,b):
    for i in range(a):
        for x in b:
            yield x
b=input().split()
a=int(input())
print(*num(a,b))