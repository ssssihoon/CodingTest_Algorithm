import sys
sys.setrecursionlimit(10000)
def dfs(x, y):
    dx = [0,0,-1,1]
    dy = [1,-1,0,0]


    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        if (0 <= nx < M) and (0 <= ny < N):
            if visited[ny][nx] == 1:
                visited[ny][nx] = -1
                dfs(nx, ny)


T = int(input())

for i in range(T):
    M, N, K = map(int, input().split())
    visited = [[0]*M for k in range(N)]
    count = 0

    for j in range(K):
        X, Y = map(int, input().split())
        visited[Y][X] = 1

    for x in range(M):
        for y in range(N):
            if visited[y][x] == 1:
                dfs(x, y)
                count += 1
    print(count)