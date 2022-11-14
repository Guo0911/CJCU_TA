n = int(input())

def F91(n):
    if(n <= 100):
        return F91(F91(n + 11))
    else:
        return (n - 10)

print(F91(n))

# input: 101
# output: 91