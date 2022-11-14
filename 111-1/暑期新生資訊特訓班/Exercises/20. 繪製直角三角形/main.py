height = int(input()) # 假設 height = 3

for i in range(height): #    i = [0, 1, 2]
    for j in range(i + 1): # j = [1, 2, 3]
        print('*', end = '')
    print()