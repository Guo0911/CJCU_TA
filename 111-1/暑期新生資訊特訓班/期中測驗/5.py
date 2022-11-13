def prime(x):
    if (x == 2) or (x == 3):
        return True
    if (x % 6 != 1) and (x % 6 != 5):
        return False
    for i in range(5, int(x ** 0.5) + 1, 6):
        if (x % i == 0) or (x % (i + 2) == 0):
            return False
    return True

while True:
    n = int(input())

    if (100000 >= n > 1):
        num = 0
        total = 0
        for i in range(3, (n + 1), 2):
            check = prime(i)
            
            if check:
                num += 1
                total += i
        if (n >= 2):
            num += 1
            total += 2
        
        if ((total % num) == 0):
            Avg = total // num
        else:
            Avg = round((total / num), 6)

        print(f'您輸入的數值為{n}，1~{n}之間的質數個數為{num}，質數總和為{total}，質數平均值為{Avg}')
    elif (100000 >= n > 0):
        print(f'您輸入的數值為{n}，1~{n}之間的質數個數為0，質數總和為0，質數平均值為0')
    else:
        print(f'您輸入的數值為{n}，請輸入1~100000的整數')