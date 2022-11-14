from math import factorial

n = factorial(int(input())) # n = 輸入數值的階層

for i in range(len(str(n))): # 如果 n = 10000, 則 len(n) = 5, 因此當 i 執行到 4 時 j 為 10000
    j = 10 ** i
    
    if((n % j) != 0): # 504000 % 10000 != 0 => i = 4
        i -= 1
        break

print(i)

# input: 7
# output: 1