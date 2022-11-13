import math
a, b, c = list(map(int,input().split()))

def quadratic(a,b,c):
    key = (b ** 2) - (4 * a * c) # 計算判別式

    if key > 0: # key > 0 有兩根
        x1 = (-b + math.sqrt(key)) / (2 * a)
        x2 = (-b - math.sqrt(key)) / (2 * a)
    
    elif key == 0: # key == 0 為重根(兩根相同)
        x1 = -b / 2 * a
        x2 = x1
    
    elif key < 0: # key < 0 為無解
        return None, None
    
    return x1, x2

x1, x2 = quadratic(a, b, c)

print("您的輸入為 ", a, "、", b, " 和 ", c, "，解出兩根為 ", x1, " 和 ", x2, sep='')