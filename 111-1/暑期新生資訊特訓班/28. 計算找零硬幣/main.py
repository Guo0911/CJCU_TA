price = int(input())

money = (1000 - price) # 要找零的數量

five_hundred, money = (money // 500), (money % 500)

hundred, money = (money // 100), (money % 100)

fifty, money = (money // 50), (money % 50)

ten, money = (money // 10), (money % 10)

five, money = (money // 5), (money % 5)

one = money

print(five_hundred, hundred, fifty, ten, five, one)

# input: 499
# output: 1 0 0 0 0 1