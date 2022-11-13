times = int(input()) # 測資數量
number = input() # 中獎號碼

word2bonus = {0: 0, 1: 0, 2: 0, 3: 500, 4: 2000, 5: 5000, 6: 50000, 7: 300000, 8: 1000000}
# 建立對應獎金的轉換字典 (也可以使用串列(list)或其他方式)

bonus = 0 # 存放中獎的總金額
for t in range(times): # 循環times次
    nums = input().split(',') # 讀入每一行對獎號碼，並以「,」分割成串列
    
    for num in nums: # 遍歷每一個需要兌獎的號碼
        same = 0 # 存放末尾n碼相同的數量
        for i in range(1, 9): # 檢查號碼的每個字
            if (num[-i] == number[-i]): # 檢查倒數第i個字是否相同
                same = i # 若相同，則紀錄末尾n碼相同
            else:
                break # 不同則跳出迴圈，當倒數第n碼不同，則無需繼續往前比較
        bonus += word2bonus[same] # 轉換中獎的獎金並加到總獎金

print(bonus) # 輸出總獎金