m_to_d = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
day_cycle = ['Sunday', 'Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday']
# 由測資得到1/6是Sunday，回推1/1是Tuesday，因此將Tuesday放在第0個元素，若不放第0個則最後需要將日期加到陣列中對應的位置

while True:
    data = list(map(int, input().split(',')))
    for i in range(0, len(data), 2):
        m, d = data[i], data[i+1]
        
        if ((1 <= m <= 12) and (1 <= d <= m_to_d[m-1])):
            for j in range(m-1):
                d += m_to_d[j]
                
            print(day_cycle[(d-1)%7])
        else:
            print('Error')