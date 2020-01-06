# This is my practice program for this chapter

################ TASK ###############

# Write a function named collatz() that has one parameter named number. 
# If number is even, then collatz() should print number // 2 and return this value. 
# If number is odd, then collatz() should print and return 3 * number + 1.
# Then write a program that lets the user type in an integer and that 
# keeps calling collatz() on that number until the function returns the value 1. 
# (Amazingly enough, this sequence actually works for any integer—sooner or later, 
# using this sequence, you’ll arrive at 1! Even mathematicians aren’t sure why. 
# Your program is exploring what’s called the Collatz sequence, sometimes called 
# “the simplest impossible math problem.”)
# Remember to convert the return value from input() to an integer with the int() 
# function; otherwise, it will be a string value.

############## END TASK ##############

def collatz(number):
    '''take an input number and // 2 if even. If the input number is odd the function
    will return 3 * number + 1.'''
    try:
        number = int(number)
        if number % 2 == 0:
            return number // 2
        else:
            return 3 * number + 1
    except ValueError:
        return "/!\ Please enter an integer /!\\"
    

keep = None
while keep != 1:
    invalue = input("Please enter a number: ")
    keep = collatz(invalue)
    print(keep)