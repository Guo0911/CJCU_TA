h, w = map(float, input().split())

def bmi(h, w):
    result = round((w / (h ** 2)), 2)
    return result

h = (h / 100)

print('你的BMI為', bmi(h, w))