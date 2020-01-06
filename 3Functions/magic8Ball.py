import random

def getAnswer(answerNumber):
    if answerNumber == 1:
        return "It is certain"
    elif answerNumber == 2:
        return "It is decidedly so"
    elif answerNumber == 3:
        return "yes"
    elif answerNumber == 4:
        return "reply hazy, ask AGANE"
    elif answerNumber == 5:
        return "Ask again later"
    elif answerNumber == 6:
        return "cencentrate and ask again"
    elif answerNumber == 7:
        return "my reply is no"
    elif answerNumber == 8:
        return "Outlook not so good"
    elif answerNumber == 9:
        return "very doubtful"

# r = random.randint(1,9)
# fortune = getAnswer(r)
print(getAnswer(random.randint(1,9)))