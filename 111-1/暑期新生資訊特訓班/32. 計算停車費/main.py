h1, m1 = map(int,input().split())
h2, m2 = map(int,input().split())

half_h = ((h2 - h1) * 2) # 將小時轉為半小時
if ((m2 - m1) >= 30):
    half_h += 1 # 07:02 ~ 07:32 => (((7 - 7) * 2) + 1)
elif((m1 - m2 ) > 30):
    half_h -= 2 # 07:33 ~ 08:02 => (((8 - 7) * 2) - 2)
elif((m1 - m2 ) > 0):
    half_h -= 1 # 07:32 ~ 08:02 => (((8 - 7) * 2) - 1)

sixty = (half_h - 8) # 超過 4 小時，half_h <= 8 代表沒有停超過 4 個小時
if(sixty < 0):
    sixty = 0 # 若不滿 4 小時，則要將時數歸 0，否則後續計算會出錯

forty = (half_h - sixty - 4) # 超過 2 小時
if(forty < 0):
    forty = 0 # 若不滿 2 小時，則要將時數歸 0，否則後續計算會出錯

thirty = (half_h - forty - sixty) # 剩餘時間

price = ((30 * thirty) + (40 * forty) + (60 * sixty)) # 計算價格

print(price) # 輸出