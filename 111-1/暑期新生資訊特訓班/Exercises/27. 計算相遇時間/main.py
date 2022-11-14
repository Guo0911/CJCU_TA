from math import ceil

distance = (int(input()) * 100) # cm

s1 = 100 # 小明的行走速度 cm/s
s2 = (2.54 * 30) # 小華的行走速度 cm/s

cm_second = (s1 - s2) # 小明每秒比小華多走的距離 cm/s

time = ceil(distance / cm_second) # math.ceil(x) return 最接近 x 但比 x 大的整數

print(time)

# input: 10
# output: 43