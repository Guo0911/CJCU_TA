while True:
    d, x = map(int, input().split())
    
    temp = (x - (5 * d))
    b = (temp / -2)
    a = (b + d)

    print(int(a), int(b))

# x = 6d - a - b ; d = a - b
# 6d = a + b + x = 6(a - b)

# x = 6a - 6b - a - b = 5a - 7b
# x - 5d = (5a - 7b) - 5(a - b)
#        =>5a - 7b - 5a + 5b
#        =>-2b