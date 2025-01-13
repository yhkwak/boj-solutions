# 2798 문제 풀이
a = input().split()
n, m = int(a[0]), int(a[1])

card = input().split()
card = [int(card[i]) for i in range(n)]

ans = 0
for i in range(n-2):
    for j in range(i + 1, n - 1):
        for k in range(j + 1, n):
            sum = card[i] + card[j] + card[k]
            if ans < sum <= m:
                ans = sum

print(ans)



