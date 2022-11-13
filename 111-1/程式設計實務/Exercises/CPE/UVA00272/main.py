times = 0
while True:
    try:
        content = input()
        newContent = ''
        for i in content:
            if (i == '"'):
                if ((times % 2) == 0):
                    newContent += '``'
                else:
                    newContent += "''"
                times += 1
            else:
                newContent += i
        
        print(newContent)
    except:
        break