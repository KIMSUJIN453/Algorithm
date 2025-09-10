def find_card(cnt, s, start):   # 횟수와 합, 시작 인덱스
    global M
    global result

    if cnt == 3:
        if s <= M and s > result:
            result = s
        return

    for i in range(start, len(cards)):
        find_card(cnt+1, s+cards[i], i+1)


N, M = map(int, input().split())
cards = list(map(int, input().split()))

result = 0
find_card(0, 0, 0)

print(result)