score  = int(input())

if(score >= 91) and (score <= 100):
    print("A")
else:
    if(score >= 81) and (score <= 90):
        print("B")
    else:
        if(score >= 71) and (score <= 80):
            print("C")
        else:
            if(score >= 60) and (score <= 70):
                print("D")
            else:
                if(score >= 0) and (score <= 59):
                    print("F")
                else:
                    print("Error")

# 在寫 if-else 判斷式時，一定要特別注意「>、<、==」跟「>=、<=」的不同
# 必須同時達到的條件需要使用 and；例如：要騎機車就必須「滿 18 歲」且要「有駕照」
# 如果只需要擇一達成則改用 or；例如：要逛台南大東夜市只能在「禮拜一」或「禮拜二」或「禮拜五」

# 分數介於 91 ~ 100 為 A 等；81 ~ 90 為 B 等；71 ~ 80 為 C 等；60 ~ 70 為 D 等；0 ~ 59 為 F 等；若不在範圍內則輸出 Error

# input:  100
# output: A