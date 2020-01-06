# This program says hello and asks for your name

#Basics
print("Hello, World")

#Ask for user's name
print("What is your name?")
yourName = input()

#Print name and give its length
print("It is nice to meet you "+ yourName)
print("The length of your name is ")
print(len(yourName))

#Ask for age and print the age in a year
print("What is your age?")
yourAge = input()
print("you will be " + str(int(yourAge)+1) + " in one year.")