month = int(input())

if(month >= 1) and (month <= 3): # 如果 month 大於等於 1 且 小於等於 3 時執行 if 內的程式碼，可以理解為 1 <= month >= 3
    print('春')
elif(month >= 4) and (month <= 6): # 如果 month 大於等於 4 且 小於等於 6 時執行 if 內的程式碼，可以理解為 4 <= month >= 6
    print('夏')
elif(month >= 6) and (month <= 9): # 如果 month 大於等於 6 且 小於等於 9 時執行 if 內的程式碼，可以理解為 6 <= month >= 9
    print('秋')
elif(month >= 9) and (month <= 12): # 如果 month 大於等於 9 且 小於等於 12 時執行 if 內的程式碼，可以理解為 9 <= month >= 12
    print('冬')
else: # 上述 if 及 elif 條件皆不成立，因此執行 else 內的程式碼
    print('請輸入1~12範圍內的數值')