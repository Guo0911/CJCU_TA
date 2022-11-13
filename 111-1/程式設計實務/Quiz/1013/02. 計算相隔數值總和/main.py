while True:
    s, e, d = map(int, input().split())

    total = 0
    for i in range(s, (e+1)):
        if (((i-s) % d) == 0):
            total += i
    if (total == 0):
        print('Error')
    else:
        print(total)