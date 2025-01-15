# 1920 문제 풀이
import sys
input = sys.stdin.readline

n = int(input())
a = set(map(int, input().split()))

m = int(input())
b = list(map(int, input().split()))


for i in b:
    if a.__contains__(i):
        print(1)
    else:
        print(0)


