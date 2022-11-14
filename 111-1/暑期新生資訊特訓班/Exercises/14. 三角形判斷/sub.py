x, y, z = list(map(float, input().split()))

if((x + y) > z) and ((x + z) > y) and ((y + z) > x): # 判斷三個條件是否都成立
    print('可以構成三角形')
else: # 若不成立則執行 else 內的程式碼
    print('無法構成三角形')