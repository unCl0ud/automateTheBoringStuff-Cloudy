import random, sys

number = random.randint(1,100)
count = 0

print("I'm thinking of a number between 1 and 100")

while True:
    print("\nTake a guess")
    guess = input()
    try:
        guess = int(guess)
        if guess < number:
            print("Your guess is too low")
            count = count + 1
            continue
        elif guess > number:
            print("Your Guess is too high")
            count = count + 1
            continue
        elif guess == number:
            count = str(count)
            print("Good job you guessed my number it took "+ count+ " guesses.")
            sys.exit()
        else:
            print("Please enter a vaild guess")
    except ValueError:
        print("Please enter a vaild guess")