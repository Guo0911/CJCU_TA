import math
def check(p, c): # 檢查p點是否在圓c內，p包含[x軸座標, y軸座標]，c包含[圓心的x軸座標, 圓心的y軸座標, 圓的半徑]
    x = p[0] - c[0] # 計算x軸的差距
    y = p[1] - c[1] # 計算y軸的差距
    distance = math.sqrt(math.pow(x, 2) + math.pow(y, 2)) # 畢氏定理
    if (distance <= c[2]): # 距離是否小於半徑
        return True
    else:
        return False

circle = list(map(int, input().split(','))) # 讀入圓的資訊 
c1 = [circle[0], circle[1], circle[2]] # 將第一個圓的x軸座標, y軸座標, 半徑放入c1的串列中
c2 = [circle[3], circle[4], circle[5]] # 將第二個圓的x軸座標, y軸座標, 半徑放入c2的串列中

times = int(input()) # 測資數量
for t in range(times): # 循環times次
    output = {'inside': 0, 'outside': 0, 'c1': 0, 'c2': 0} # 該行測資的點位置資訊
    point = list(map(int, input().split(','))) # 讀入所有點的座標
    for i in range(0, len(point), 2): # 因為每兩個為一組(x,y)，因此每次迴圈執行後i需要+2
        p = [point[i], point[i+1]] # 建立點p的座標串列

        result = [check(p, c1), check(p, c2)] # 計算p是否在第一個圓和第二個圓，若是則為True
        if (result[0] and result[1]): # 若result的兩個結果都是True，代表點p同時在兩個圓內
            output['inside'] += 1
        elif (result[0] and not result[1]): # 當result = [True, False]代表點p只在第一個圓內
            output['c1'] += 1
        elif (not result[0] and result[1]): # 當result = [False, True]代表點p只在第二個圓內
            output['c2'] += 1
        else: # 當result的兩個結果都是False，則代表點p在兩個圓外
            output['outside'] += 1
    
    print(f"{output['inside']},{output['outside']},{output['c1']},{output['c2']}")
