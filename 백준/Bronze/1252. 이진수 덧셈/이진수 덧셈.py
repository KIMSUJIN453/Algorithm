N, M = map(int, input().split())

mid = N + M

check = list(map(int, str(mid)))

for i in range(len(check)-1, -1, -1):
    if check[i] == 2:
        if i == 0:
            check[i] = 10
        else:
            check[i-1] += 1
            check[i] = 0
    elif check[i] == 3:
        if i == 0:
            check[i] = 11
        else:
            check[i-1] += 1
            check[i] = 1


print(''.join(map(str, check)))