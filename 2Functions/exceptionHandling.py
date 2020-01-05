import random

def spam(divideBy):
    try:
        return 42 / divideBy
    except ZeroDivisionError:
        print("I cannot divide by zero")

for i in range(0,100):
    num = random.randint(0,10)
    print(spam(num))