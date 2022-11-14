x, y = list(map(int, input().split()))

for z in range(x, (y - 1), -1):
    for i in range(z, (z - y), -1):
        print(i, end = ' ')
    print(z - y)

# 每一行都要輸出由 z 到 (z - y) 的數值

"""
input:
10 3

output: 
10 9 8 7
9 8 7 6
8 7 6 5
7 6 5 4
6 5 4 3
5 4 3 2
4 3 2 1
3 2 1 0
"""