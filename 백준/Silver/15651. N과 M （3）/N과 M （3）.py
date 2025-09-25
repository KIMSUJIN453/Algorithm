from collections import deque

def choice(cnt, q):
    if cnt == M:
        print(' '.join(map(str, q)))
        return

    for i in range(1, N+1):
        q.append(i)
        choice(cnt+1, q)
        q.pop()


N, M = map(int, input().split())
q = deque()
choice(0, q)