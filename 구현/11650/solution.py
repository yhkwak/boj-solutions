# 11650 문제 풀이
import sys
input = sys.stdin.readline

n = int(input())

dots = []

for i in range(n):
    dot = tuple(map(int, input().split()))
    dots.append(dot)

dots.sort()

for dot in dots:
    print(*dot)

