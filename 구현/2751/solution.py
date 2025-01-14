# 2751 문제 풀이
import sys
input = sys.stdin.readline

n = int(input())
a = []

for _ in range(n):
    a.append(int(input()))

a.sort()

for i in a:
    print(i)

