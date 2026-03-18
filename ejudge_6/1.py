n = int(input())
numbers = map(int, input().split())
squ = sum(map(lambda x: x**2, numbers))
print(squ)