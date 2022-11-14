x = int(input())

sum = 0 # sum 也是一個函式名稱，這題只是簡單的題目，所以不用特別避開函式名稱

for i in range(1, (x + 1)): # 此處也可寫「for i in range(x + 1):」，只是少做一個數值 0 的加總
    sum += i # 作用相同於 sum = (sum + i)

print('由 1 到', x, '的數值總和為 :', sum)

# input:  10
# output: 由 1 到 10 的數值總和為 : 55