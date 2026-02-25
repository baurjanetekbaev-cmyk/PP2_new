def num(a):
    z=0
    n=1
    for i in range(a):
        yield z
        z,n=n,z+n
a=int(input())
print(",".join(map(str,num(a))))