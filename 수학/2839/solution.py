# 2839 문제 풀이
n = int(input())
cnt = 0

if n % 5 == 0:
    print(n // 5)
elif n > 0:
    while True:
        n -= 3
        cnt += 1
        if n % 5 == 0:
            print(n // 5 + cnt)
            break
        elif n == 1 or n == 2:
            print(-1)
            break
        elif n == 0:
            print(cnt)
