def number(a):
    for i in[2,3,5]:
        while a%i==0:
            a=a//i
    if a==1:
        return "Yes"
    else:
        return "No"
a=int(input())
print(number(a))

