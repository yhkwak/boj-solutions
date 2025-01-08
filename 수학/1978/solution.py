# 1978 문제 풀이
def is_prime_number(x):
    if x == 1:
        return False
    else:
        for i in range(2, x):
            if x % i == 0:
                return False
        return True


n = int(input())
nums = input().split()
cnt = 0

for i in range(n):
    if is_prime_number(int(nums[i])):
        cnt += 1

print(cnt)
