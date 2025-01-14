# 1181 문제 풀이
import sys
input = sys.stdin.readline

n = int(input())
words = set()

for _ in range(n):
    words.add(input().strip())

words = list(words)
words.sort(key = lambda x: (len(x), x))

for word in words:
    print(word)




