# Error Checking
# Author: Caleb Bull
# Date: 24/10/2025
# Version 1

# Code that tests whether a valid input is given (v1)
'''done = False
while not done:
    num = int(input("Please enter your value: "))
    done = True

print(f"The number that you have entered is {num}.")'''

# Code that tests whether a value input is given (v1.1)
# Use the try and excpet method to catch errors
'''done = False
while not done:
    try: # This method tries for a valid input
        num = float(input("Please enter a number: "))
        done = True

    except ValueError:
        print("That is not a valid number. \n")

print(f"The number that you have entered is {num}.")'''

# Code that tests whether a value input is given (v1.2)
# Create a function to call every time I ask the user for a number. A function is a chunk of code that does something.
# Functions can be used over and over again.
# To use a function (call it), write out its name with parantheses at the end.
# To create a function, sart with word def
'''def test_int_num():
    done = False
    while not done:
        try:
            num = int(input("Please enter a number: "))
            done = True

        except ValueError:
            print("That is not a valid integer")

    print(f"THe number that you have entered is {num}.")

# Main routine
test_int_num() # This calls the function so that we can use it'''

# Code that tests whether a value input is given (v1.3)
# Use function parameters to make my code more pythonic.

'''def test_int(question): # 'question' is a placeholder
    done = False
    while not done:
        error = "That is not a valid integer"
        print(question)
        try:
            num = int(input())
            done = True
        except ValueError:
            print(error)
    
    return(num) # Gives back the value of 'num' so that I can use it outside of the function.

# Main routine
num1 = test_int("Please enter your first integer: ")
print(f"Your first number entered is {num1}. \n")

num2 = test_int("Please enter your second number: ")
print(f"The second number you entered is {num2}. \n")

sum = num1 + num2
print(f"Your numbers added together equal to {sum}.")'''

# Code that tests whether a value input is given (v1.4)
# Use function parameters to make my code more pythonic.

def valid_num(question, low, high):
    error = f"Whoops, that's not an integer between {low} and {high}."
    while True:
        try:
            response = int(input(question))
            # if response >= 1 and response <= 10:
            if low <= response <= high:
                break # This stops the loop

            else:
                print(f"{error}\n")

        except ValueError:
            print(f"{error}\n")
    return response # This makes the response available to be used

num_1 = valid_num("Enter a number between 1 and 10: ",1,10)
print(f"You entered {num_1}.\n")

num_2 = valid_num("Enter a number between 15 and 25: ",15,25)
print(f"You entered {num_2}.\n")

num_3 = valid_num("Enter a number between 70 and 90: ",70,90)
print(f"You entered {num_3}.\n")

sum = num_1 + num_2 + num_3
print(f"The total of {num_1}, {num_2} and {num_3} is {sum}.\n")

multiply = num_1 * num_2 * num_3
print(f"Your three numbers multplied together is {multiply}.\n")