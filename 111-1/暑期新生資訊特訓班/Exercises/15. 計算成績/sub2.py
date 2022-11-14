score = int(input())

if(score >= 101) or (score <= -1):
    print("Error")
elif(score >= 91):
    print("A")
elif(score >= 81):
    print("B")
elif(score >= 71):
    print("C")
elif(score >= 60):
    print("D")
else:
    print("F")