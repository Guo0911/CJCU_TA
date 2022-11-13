x = int(input())

i = 2 # 若第 7 行使用 for 迴圈，則不需要此行

Prime_number = '' # 儲存質數的字串

while(i <= x): # 也可以改為 「for i in range(2, (x + 1))」

    check = True # 紀錄 i 是否為質數，預測為 True 代表是質數

    for j in range(2, ((i // 2) + 1)): # 可以思考為何只執行 2 到 (i // 2)
        if ((i % j) == 0): # 若 i % j = 0 則代表 i 可以被 j 整除，因此 i 不是質數
            check = False # 將記錄是否為質數的 Boolean 改為 False
            break # 跳出迴圈，因為已經確定不是質數了
    
    if(check): # 如果是 True 則 if(True) 會進入 if 內
        Prime_number += (str(i) + ' ') # 將質數新增到字串中
    
    i += 1 # 若第 7 行使用 for 迴圈，則不需要此行
    
ans = Prime_number.rstrip() # 消除最右邊的空白，也可以使用「ans[:-1]」

print(ans)