# 4153 문제 풀이
answer = []

while True:
    line = []

    for i in input().split():
        i = int(i)
        line.append(i)

    if not line == [0, 0, 0]:
        line.sort()

        if line[2] ** 2 == line[0] ** 2 + line[1] ** 2:
            answer.append("right")
        else:
            answer.append("wrong")

    else:
        break

print(*answer)

