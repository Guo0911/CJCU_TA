contents = []
maxLen = 0

while True:
    try:
        content = input()
        contents.append(content)
        maxLen = max(len(content), maxLen)
    except:
        break

for i in range(maxLen):
    for j in range((len(contents)-1), -1, -1):
        try:
            print(contents[j][i], end='')
        except:
            print(' ', end='')
    print()