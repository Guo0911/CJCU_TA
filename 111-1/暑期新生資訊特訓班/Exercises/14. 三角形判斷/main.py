x, y, z = list(map(float, input().split()))

# 這題需要判斷 x, y, z 是否任意兩邊長相加後會大於另一邊長
# 因此可使用多重判斷(判斷式內有其他判斷式)或同學可在一個 if 內使用「and」進行多條件判斷，如檔案「sub.py」的寫法

if(x + y) > z: # 首先判斷 x + y 是否大於 z

    if(x + z) > y: # 若上述條件符合才繼續判斷 x + z 是否大於 y

        if(y + z) > x: # 前兩項條件符合，則判斷最後一組的 y + z 是否大於 x
            print('可以構成三角形')
        else: # 若 y + z 不大於 x 則執行 else 內的程式碼
            print('無法構成三角形')

    else: # 若 x + z 不大於 y 則執行 else 內的程式碼
        print('無法構成三角形')

else: # 若 x + y 不大於 z 則執行 else 內的程式碼
    print('無法構成三角形')