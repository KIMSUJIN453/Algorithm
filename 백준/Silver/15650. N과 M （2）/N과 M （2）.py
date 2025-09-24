def choice(cnt, my_str, s):
    if cnt == M:
        print(' '.join(my_str))
        return

    for i in range(s, N+1):
        if len(my_str) >= 1 and int(my_str[-1]) >= i:
            continue
        choice(cnt+1, my_str+str(i), s+1)

N, M = map(int, input().split())

choice(0, '', 1)