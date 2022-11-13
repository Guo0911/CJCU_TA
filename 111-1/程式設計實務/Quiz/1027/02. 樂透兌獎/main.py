bouns = {0: 0, 1: 0, 2: 0, 3: 100, 4: 500, 5: 700, 6: 1000}

while True:
    total = 0
    num = list(map(int, input().split()))
    times = int(input())
    for t in range(times):
        num2 = list(map(int, input().split()))
        time_of_num = 0
        for n in num:
            time_of_num += num2.count(n)
            
        total += bouns[time_of_num]

    print(total)
