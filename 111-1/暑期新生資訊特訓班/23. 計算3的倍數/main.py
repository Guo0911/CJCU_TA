x = int(input())

i = 1

ans = ''

while(i <= x):
    if ((i % 3) == 0):
        ans += (str(i) + ' ')
    i += 1

ans = ans.rstrip()

print(ans)

# input: 9
# output: 3 6 9