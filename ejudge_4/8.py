def y(n):
    for num in range(2,n+1):
        iss=True
        for i in range(2,int(num**0.5)+1):
            if num%i==0:
                iss=False
                break 
        if iss:
            yield num
n=int(input())
for j in y(n):
    print(j,end=" ")