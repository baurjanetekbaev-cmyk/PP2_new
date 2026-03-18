n = int(input())
numbers = map(int, input().split())
even = sum(map(lambda x: x % 2 == 0, numbers))
print(even)