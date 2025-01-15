# 2292 문제 풀이
# 1           1       1
# 2 - 7       6       2
# 8 - 19      12      3
# 20 - 37     18      4
# 38 - 61     24      5

n = int(input())
ans = 0
num = 1

while True:
    num = num + (6 * ans)
    if n <= num:
        print(ans + 1)
        break
    ans += 1

