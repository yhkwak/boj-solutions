# 1546 문제 풀이
n = int(input())
scores = input().split()

for i in range(n):
    scores[i] = int(scores[i])

scores.sort()

m = scores[n-1]

scores = [(i / m * 100) for i in scores]

sum = 0
for i in scores:
    sum = sum + i
print(sum / n)


