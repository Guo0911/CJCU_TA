x = int(input())

ans = ''

for i in range(1, (x + 1)):
    if ((i % 3) == 0):
        ans += (str(i) + ' ')

# ans = 「3 6 9 」

ans = ans.rstrip(' ')

# ans = 「3 6 9」

print(ans)

# input: 9
# output: 3 6 9