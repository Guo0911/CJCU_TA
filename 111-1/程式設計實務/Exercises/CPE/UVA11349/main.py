t = int(input())

for i in range(t):
    n = int(input().replace('N = ', ''))

    check = True
    matrix = []
    for j in range(n):
        col = list(map(int, input().split()))
        for row in col:
            if (row < 0): # 確認每個元素是否都在範圍0 ~ 100
                check = False
        matrix.append(col)
    
    for col in range(round(n/2)):
        a = matrix[col][::-1]
        b = matrix[(n - (col+1))]

        if (a != b):
            check = False

    if check:
        print(f'Test #{i+1}: Symmetric.')
    else:
        print(f'Test #{i+1}: Non-symmetric.')