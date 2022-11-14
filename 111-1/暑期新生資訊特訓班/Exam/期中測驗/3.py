def triangle(a, b, c):
    if (((a + b) > c) and ((a + c) > b) and ((b + c) > a)):
        return True
    else:
        return False

while True:
    m, a, b, c = map(int, input().split())

    if (m == 1):
        if ((a < 0) or (b < 0) or (c < 0)):
            print(f'您選擇1，輸入格式錯誤，請輸入大於0的數值')
        elif triangle(a,b,c):
            print(f'您選擇1，三邊長{a}、{b}、{c}可構成三角形')
        else:
            print(f'您選擇1，三邊長{a}、{b}、{c}無法構成三角形')

    elif (m == 2):
        if ((a < 0) or (b < 0) or (c < 0)):
            print(f'您選擇2，輸入格式錯誤，請輸入大於0的數值')
        elif ((((a + b) * c) % 2) == 0):
            print(f'您選擇2，上底{a}、下底{b}、高{c}，梯形面積為{((a + b) * c // 2)}')
        else:
            print(f'您選擇2，上底{a}、下底{b}、高{c}，梯形面積為{((a + b) * c / 2)}')

    else:
        print(f'您選擇{m}，沒有此選項')