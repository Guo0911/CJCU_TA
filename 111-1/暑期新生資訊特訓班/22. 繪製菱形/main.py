width = int(input())

for i in range(1, (width + 1), 2):
    for j in range((width - i)//2):
        print(' ', end = '')
    for j in range(i):
        print('*', end = '')
    print()


for i in range((width - 2), 0, -2):
    for j in range((width - i)//2):
        print(' ', end = '')
    for j in range(i):
        print('*', end = '')
    print()