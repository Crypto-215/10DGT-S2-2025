# Demonstrate how variables are created amd how they work.
# Author: Caleb Bull
# Date: 08-10-2025
# Version 1.1

# Different types of variables
# Store a string
greeting = "Hello World!"
print(greeting)

# Store a number
my_number = 80
print(my_number)

my_number2=7
print(my_number2)

# Assign the value of one variable to another
my_number = greeting
print(my_number)

'''Do calculations with variables and store the result 
in another variable. I can now 
press enter as many times 
as 
I 
like'''

# Create new variable
num_1 = 5
num_2 = 18

sum1 = 5 + 18
print(sum1)

sum1 = num_1 + num_2
print(sum1)

sum_string1 = "18"
sum_string2 = "5"

# Adding two strings together. This is called concatenation
sum = sum_string1 + sum_string2
print(sum)

# Print formatting. f stands for 'format' and insert the value of variables into the curly brackets
print(f"My calculation for {num_1} and {num_2} together is {sum1}.")