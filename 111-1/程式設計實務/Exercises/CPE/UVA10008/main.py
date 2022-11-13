times = int(input())

num_of_word = {}
for t in range(times):
    content = input().upper() # 所有字母轉大寫

    for i in content:
        if (ord('A') <= ord(i) <= ord('Z')):
            if (i in num_of_word):
                num_of_word[i] += 1
            else:
                num_of_word[i] = 1

sort_dict = {}

for i in num_of_word.keys():
    if (num_of_word[i] in sort_dict):
        sort_dict[num_of_word[i]].append(i)
    else:
        sort_dict[num_of_word[i]] = [i]

num = sorted(sort_dict, reverse=True)
for i in num:
    for j in sorted(sort_dict[i]):
        print(j, i)