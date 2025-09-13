import heapq
import sys
input = sys.stdin.readline

hq = []
N = int(input())
for _ in range(N):
    num = int(input())
    if num != 0:
        heapq.heappush(hq, num)
    elif num == 0:
        if not hq:
            print('0')
        else:
            print(heapq.heappop(hq))