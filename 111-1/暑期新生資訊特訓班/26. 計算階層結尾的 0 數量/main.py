from math import factorial

n = factorial(int(input())) # n = 輸入數值的階層

i = 0

while (i < len(str(n))): # 如果 n = 10000, 則 len(n) = 5, 因此當 i 執行到 4 時 j 為 10000
    j = 10 ** i
    
    if(n % j) != 0:
        i -= 1
        break

    i += 1

print(i)

# input: 7
# output: 1