m_to_d = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
day_cycle = ['Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday', 'Monday']
# 由測資得到1/6是Sunday，回推1/1是Tuesday，因此將Tuesday放在第0個元素，若不放第0個則最後需要將日期加到陣列中對應的位置

while True:
    m, d = map(int, input().split())
    
    if ((1 <= m <= 12) and (1 <= d <= m_to_d[m-1])):
        for j in range(m-1):
            d += m_to_d[j]
            
        print(day_cycle[(d-1)%7])
    else:
        print('Error')