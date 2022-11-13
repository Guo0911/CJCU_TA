x = int(input())

for i in range(1, (x - 2)):
    if ((i % 3) == 0):
        print(str(i), end = ' ')

for i in range((x - 2), (x + 1)):
    if ((i % 3) == 0):
        print(str(i))

# input: 9
# output: 3 6 9