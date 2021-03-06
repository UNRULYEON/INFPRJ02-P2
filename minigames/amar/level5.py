import random
from random import randint


def gen_problem(self):
    print("Generating level 5 problem...")

    global sort_answer
    global sort_answer_1
    global sort_answer_2
    global answer
    global extra

    answer = 0
    sort_answer = 0
    sort_answer_1 = ""
    sort_answer_2 = ""

    list = [2, 4, 6, 8, 10, 12, 14, 16, 18, 20, 22, 24, 26, 28, 30]

    a, b, c, extra = random.sample(list, 4)

    sort_answer = randint(1, 8)
    if sort_answer is 1:
        sort_answer = "a x b + c"
        sort_answer_1 = "x"
        sort_answer_2 = "+"
        x = a * b
        y = x + c
        answer = y
    elif sort_answer is 2:
        sort_answer = "a x b - c"
        sort_answer_1 = "x"
        sort_answer_2 = "-"
        x = a * b
        y = x - c
        answer = y
    elif sort_answer is 3:
        sort_answer = "a - b x c"
        sort_answer_1 = "-"
        sort_answer_2 = "x"
        x = b * c
        y = a - x
        answer = y
    elif sort_answer is 4:
        sort_answer = "a + b x c"
        sort_answer_1 = "+"
        sort_answer_2 = "x"
        x = b * c
        y = a + x
        answer = y
    elif sort_answer is 5:
        sort_answer = "a / b + c"
        sort_answer_1 = "/"
        sort_answer_2 = "+"
        x = a / b
        y = x + c
        answer = round(y, 1)
    elif sort_answer is 6:
        sort_answer = "a / b - c"
        sort_answer_1 = "/"
        sort_answer_2 = "-"
        x = a / b
        y = x - c
        answer = round(y, 1)
    elif sort_answer is 7:
        sort_answer = "a + b / c"
        sort_answer_1 = "+"
        sort_answer_2 = "/"
        x = b / c
        y = a + x
        answer = round(y, 1)
    elif sort_answer is 8:
        sort_answer = "a - b / c"
        sort_answer_1 = "-"
        sort_answer_2 = "/"
        x = b / c
        y = a - x
        answer = round(y, 1)

    print("Returning level 5 problem...")
    return a, b, c, sort_answer, sort_answer_1, sort_answer_2, answer, extra
