n = int(input())
numbers = map(int, input().split())
distinct_sorted = sorted(set(numbers))
print(*distinct_sorted)