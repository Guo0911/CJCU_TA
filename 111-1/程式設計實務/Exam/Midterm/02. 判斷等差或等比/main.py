times = int(input()) # 測資數量
for t in range(times): # 循環times次
    n = list(map(int, input().split(',')))
    # 讀入每一行對獎號碼，並以「,」分割成串列，且每個數值都轉為int型態
    
    equivariance, ratio = set(), set() # 儲存測資中數值相差與比例的集合(set)
    for i in range(1, len(n)): # 迴圈令i從1開始到n串列的長度
        ratio.add(n[i] / n[i-1]) # 將兩數的比例加到ratio中
        equivariance.add(n[i] - n[i-1]) # 將兩數相差的數值加到ratio中

    if ((len(ratio) == 1) and (len(equivariance) == 1)):
        print('皆是')
    elif (len(ratio) == 1):
        print('等比')
    elif (len(equivariance) == 1):
        print('等差')
    else:
        print('皆不是')
