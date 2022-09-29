a = int(input())
series = 1
for i in range(a):
    if series % n == 0:
            series += 2
    if i == a-1:
        print(series)
    else:
        print(series, ',', end="")
    series += 2
