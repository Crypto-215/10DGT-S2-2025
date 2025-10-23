# Author: Caleb Bull
# Date: 17-10-2025
# Version 3

# Making the program more pythonic.
'''keep_going = ""
while keep_going == "":
    # Covert answer to lowercase using .lower()
    like_coffee = input("Do you like coffee? ") .lower()
    if like_coffee == "yes" or like_coffee == "y":
        print("That's great! I like coffee too!")

    elif like_coffee == "no" or like_coffee == "n":
        print("You are missing out! Why not give it a try?")

        like_tea = input("Do you like tea instead?") .upper() # Convert input to uppercase using .upper()
        if like_tea == "YES" or like_tea == "Y":
            print("Good for you. Give coffee another try :)")

        elif like_tea == "NO" or like_tea == "N":
            print("I am sorry. That is all I have for now.")

        else:
            print("I don't undertsand. Please answer with either Yes or No.")

    else: # Error Message
        print("I don't understand. Please answer with either Yes or No.")

    keep_going = input("Press <ENTER> to contine, or any other key to quit. Thanks!")'''

# Version 3.1
def coffee_program():
    keep_going = ""
    while keep_going == "":
        # Covert answer to lowercase using .lower()
        like_coffee = input("Do you like coffee? ") .lower()
        if like_coffee == "yes" or like_coffee == "y":
            print("That's great! I like coffee too!")

        elif like_coffee == "no" or like_coffee == "n":
            print("You are missing out! Why not give it a try?")

            like_tea = input("Do you like tea instead? ") .upper() # Convert input to uppercase using .upper()
            if like_tea == "YES" or like_tea == "Y":
                print("Good for you. Give coffee another try :)")

            elif like_tea == "NO" or like_tea == "N":
                print("I am sorry. That is all I have for now.")

            else:
                print("I don't undertsand. Please answer with either Yes or No.")

        else: # Error Message
            print("I don't understand. Please answer with either Yes or No.")

        keep_going = input("Press <ENTER> to contine, or any other key to quit. Thanks!")
 
# Main Routine
if __name__ == "__main__":
    coffee_program()
