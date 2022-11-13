length = int(input())

num = list(map(int, input().split()))
for i in range(1, length):
    num[i] += num[i-1]

times = int(input())
for i in range(times):
    l, r = list(map(int, input().split()))
    
    if (l <= 1):
        print(num[r-1])
    else:
        print(num[r-1] - num[l-2])