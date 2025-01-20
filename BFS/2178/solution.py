# 2178 문제 풀이

import sys
from collections import deque
input = sys.stdin.readline

n, m = map(int, input().split())
map = [list(map(int, list(input().rstrip()))) for _ in range(n)]

dy = [0, 1, 0, -1]
dx = [1, 0, -1 ,0]

def bfs(y, x):
    q = deque()
    q.append((y, x))
    while q:
        ey, ex = q.popleft()
        for i in range(4):
            ny = ey + dy[i]
            nx = ex + dx[i]

            if 0 <= ny < n and 0 <= nx < m:
                if map[ny][nx] == 1:
                    map[ny][nx] = map[ey][ex] + 1
                    q.append((ny, nx))
    return map[n-1][m-1]

print(bfs(0, 0))




