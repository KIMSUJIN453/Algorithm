def choice(cnt, s, l):
    if cnt == M:
        print(*l)
        return

    for i in range(s, N):
        choice(cnt+1, i, l+[nums[i]])

N, M = map(int, input().split())
nums = list(map(int, input().split()))

nums.sort()
choice(0, 0, [])