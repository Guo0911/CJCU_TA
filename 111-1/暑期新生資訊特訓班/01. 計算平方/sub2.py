print(int(input()) ** 2)

"""
請注意不可使用 「int(input()) * int(input())」

在程式語言中每次的 input 都會需要輸入數值，因此使用 「int(input()) ** int(input())」 會需要輸入兩次數值

但題目只會輸入一次，因此當出現第二次輸入時，程式就會出現錯誤
"""