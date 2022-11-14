while True:
    score = int(input())

    if (0 <= score <= 100):
        if (100 >= score >= 95):
            result = 'A+'
        elif (94 >= score >= 90):
            result = 'A'
        elif (89 >= score >= 85):
            result = 'B+'
        elif (84 >= score >= 80):
            result = 'B'
        elif (79 >= score >= 75):
            result = 'C+'
        elif (74 >= score >= 70):
            result = 'C'
        elif (69 >= score >= 60):
            result = 'D'
        else:
            result = 'E'

        print(f'您輸入的成績為{score}，等級為{result}')
    else:
        print(f'您輸入的成績為{score}，等級為無法識別')