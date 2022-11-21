times = int(input())

def Computing(a, b, c):
    if (((a + b) > c) and ((a + c) > b) and ((b + c) > a)):
        return True
    else:
        return False

for t in range(times):
    nums = list(map(int, input().split(',')))

    result =[0, 0] # True, False

    for i in range(0, len(nums), 3):
        a, b, c = map(int, nums[i:(i+3)])

        if Computing(a, b, c):
            result[0] += 1
        else:
            result[1] += 1

    print(",".join(list(map(str, result))))