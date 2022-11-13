score  = int(input())

if(score > 90) and (score <= 100):
    print("A")
else:
    if(score > 80) and (score <= 90):
        print("B")
    else:
        if(score > 70) and (score <= 80):
            print("C")
        else:
            if(score >= 60) and (score <= 70):
                print("D")
            else:
                if(score >= 0) and (score <= 59):
                    print("F")
                else:
                    print("Error")