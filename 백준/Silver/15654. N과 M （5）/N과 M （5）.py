def choice(cnt, l):
    if cnt == M:
        print(*l)
        return

    for i in range(N):
        if visited[i] == 0:
            visited[i] = 1
            choice(cnt+1, l+[arr[i]])
            visited[i] = 0


N, M = map(int, input().split())
arr = list(map(int, input().split()))
arr.sort()

visited = [0] * N

choice(0, [])