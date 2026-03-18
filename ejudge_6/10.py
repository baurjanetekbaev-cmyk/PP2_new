n = int(input())
numbers = map(int, input().split())
count_non_zero = sum(map(bool, numbers))
print(count_non_zero)