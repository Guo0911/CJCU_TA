def function(n):
    total = 0
    for i in n:
        total += int(i)
    
    return str(total)

while True:
    n = input()
    
    if (n == "0"):
        break

    while (len(n) > 1):
        n = function(n)

    print(n)