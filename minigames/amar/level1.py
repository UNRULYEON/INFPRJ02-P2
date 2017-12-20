import random
from random import randint


def gen_problem(self):
    print("Generating level 1 problem...")
    a, b, c = random.sample(range(1, 11), 3)

    sort_answer = randint(1, 5)
    if sort_answer is 1:
        sort_answer = "a + b + c"
        answer = a + b + c
    elif sort_answer is 2:
        sort_answer = "a - b + c"
        answer = a - b + c
    elif sort_answer is 3:
        sort_answer = "a + b - c"
        answer = a + b - c
    elif sort_answer is 4:
        sort_answer = "a - b - c"
        answer = a - b - c
    elif sort_answer is 5:
        sort_answer = "a + b + c"
        answer = a + b + c

    return a, b, c, sort_answer, answer