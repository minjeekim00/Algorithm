n = int(input())

coin_types = [500, 100, 50, 10]
cnt = 0

for c in coin_types:

    cnt += n // c
    n %= c

print(cnt)


