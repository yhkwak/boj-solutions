# 10773 문제 풀이
import sys
input = sys.stdin.readline

k = int(input())

nums = []

for _ in range(k):
    num = int(input())

    if num == 0:
        nums.pop()
    else:
        nums.append(num)

sum = 0

for num in nums:
    sum += num

print(sum)

