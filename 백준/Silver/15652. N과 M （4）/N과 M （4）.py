def choice(cnt, s, l):
    if cnt == M:
        print(' '.join(map(str, l)))
        return

    for i in range(s, N+1):
        choice(cnt+1, i, l+[i])

N, M = map(int, input().split())

choice(0, 1, [])