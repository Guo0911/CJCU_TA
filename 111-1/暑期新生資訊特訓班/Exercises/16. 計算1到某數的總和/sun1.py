x = int(input())

sum = 0

temp = x # 儲存 x 的原始數值

while(x > 0): # 避免「無窮迴圈」
    sum += x
    x -= 1

print('由 1 到', temp, '的數值總和為 :', sum)