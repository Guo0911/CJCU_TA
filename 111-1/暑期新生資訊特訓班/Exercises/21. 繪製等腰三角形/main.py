width = int(input())

for i in range(1, (width + 1), 2): # i = 目前的寬度 = [1, 3, ,5, 7, 9]
    for j in range(((width - i)//2)):
        print(' ', end = '')
    for j in range(i):
        print('*', end = '')
    print()