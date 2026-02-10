def number(a):
    v=0
    temp=a
    while temp>0:
        d=temp%10
        if d%2==0:
            v+=1
        temp=temp//10

    if v==l:
        return "Valid"
    else:
        return "No valid!"
    
n=input()
a=int(n)
l=len(str(a))

print(number(a))
