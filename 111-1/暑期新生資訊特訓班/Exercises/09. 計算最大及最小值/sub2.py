number = list(map(int, input().split()))

Max = max(number)

Min = min(number)

print("您輸入的數值為 :", str(number)[1:-1].replace(',', '') )

print("最大值 : ", Max, " 及最小值 : ", Min, sep = '')

"""
print('\n----------------------------------\n')
print('串列的格式     :', number)
print('取字串 1 ~ -1  :', str(number)[1:-1])
print('去除字串中的,  :', str(number)[1:-1].replace(',', ''))
print('呼叫第一個值   :', number[0])
"""