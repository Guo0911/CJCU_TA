while True:
    m, n, x, y = map(int, input().split())

    if ((m > 0) and (n > 0) and (x > 0) and (y > 0)):
        num = []
        num2 = []
        for i in range(m, n+1):
            if ((i % x) == 0):
                if ((i % y) != 0):
                    num.append(i)
                    num2.append(i**2)
            elif ((i % y) == 0):
                if ((i % x) != 0):
                    num.append(i)
                    num2.append(i**2)

        Sum = sum(num)
        Sum2 = sum(num2)

        print(f'您輸入的數值為{m}、{n}、{x}、{y}，{m}~{n}之間可被{x}或{y}整除，但不可被{x}及{y}同時整除的整數和為{Sum}，平方和為{Sum2}')
    else:
        print(f'您輸入的數值為{m}、{n}、{x}、{y}，請輸入1~100000的整數')