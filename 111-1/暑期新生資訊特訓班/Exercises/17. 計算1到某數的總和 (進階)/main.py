x = int(input())

sum = 0

if(x == 1):
    sum += 1
elif(x > 1):
    for i in range(1, (x + 1)):
        sum += i
elif(x < 1):
    for i in range(1, (x - 1), -1):
        sum += i

print('由 1 到', x, '的數值總和為 :', sum)

# -2
# 由 1 到 -2 的數值總和為 : -2