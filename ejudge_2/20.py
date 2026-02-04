a={}
n=int(input())
for i in range(n):
    com=input().split()

    if[0]=="set":
        key=com[1]
        value=com[2]
        a[key]=value
    elif com[0]=="get":
        key=com[1]
        if key in a:
            print(a[key])
        else:
            print(f"KE: no key {key} found in the document")
