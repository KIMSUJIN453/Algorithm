def choice(cnt, my_str):
    global visited

    if cnt > M:
        print(' '.join(my_str))
        return

    for i in range(N):
        if visited[i] == 0:
            visited[i] = 1
            choice(cnt+1, my_str+str(i+1))
            visited[i] = 0


N, M = map(int, input().split())
visited = [0] * N
char = ''
choice(1, char)