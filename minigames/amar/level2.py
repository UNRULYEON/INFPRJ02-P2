import random
from random import randint


def gen_problem(self):
    print("Generating level 2 problem...")

    global sort_answer
    global sort_answer_1
    global sort_answer_2
    global answer
    global extra

    answer = 0
    sort_answer = 0
    sort_answer_1 = ""
    sort_answer_2 = ""

    a, b, c, extra = random.sample(range(1, 51), 4)

    sort_answer = randint(1, 4)
    if sort_answer is 1:
        sort_answer = "a + b + c"
        sort_answer_1 = "+"
        sort_answer_2 = "+"
        x = a + b
        y = x + c
        answer = y
    elif sort_answer is 2:
        sort_answer = "a - b + c"
        sort_answer_1 = "-"
        sort_answer_2 = "+"
        x = a - b
        y = x + c
        answer = y
    elif sort_answer is 3:
        sort_answer = "a + b - c"
        sort_answer_1 = "+"
        sort_answer_2 = "-"
        x = a + b
        y = x - c
        answer = y
    elif sort_answer is 4:
        sort_answer = "a - b - c"
        sort_answer_1 = "-"
        sort_answer_2 = "-"
        x = a - b
        y = x - c
        answer = y

    print("Returning level 1 problem...")
    return a, b, c, sort_answer, sort_answer_1, sort_answer_2, answer, extra
