N = int(input())
year = 2024
month = 8

if N == 1:
    print(year, month)
else:
    plus_month = month + (N-1)*7
    year += plus_month // 12
    month = plus_month % 12
    if month == 0:
        year -= 1
        month = 12
    print(year, month)