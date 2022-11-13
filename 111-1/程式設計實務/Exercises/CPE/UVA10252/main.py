while True:
    try:
        content1 = input().lower()
        content2 = input().lower()

        sub_content = ""
        for i in range(ord('z') - ord('a') + 1):
            w = chr((i + ord('a'))) # 當前尋找的字

            i_of_content1 = content1.count(w)
            i_of_content2 = content2.count(w)

            sub_content += (w * min(i_of_content1, i_of_content2)) # 將字乘上「兩句子中w出現較少的次數(需>0)」

        print(sub_content)
    except:
        break