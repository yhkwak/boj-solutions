# 10814 문제 풀이
import sys
input = sys.stdin.readline

n = int(input())
members = []

for _ in range(n):
    member = input().split()
    member[0] = int(member[0])
    members.append(member)

members.sort(key=lambda x: x[0])

for member in members:
    print(*member)
