# -*- coding: utf-8 -*-
"""
Created on Fri Oct 18 18:30:05 2024

@author: enaje
"""

# Function to check if a number is even or odd

def check_even_odd(number):
    # Check if the number is even
    if number % 2 == 0:
        return "even"  # Return "even" if the number is divisible by 2
    else:
        return "odd"   # Return "odd" if the number is not divisible by 2

# Input from the user, converting the input to an integer
num = int(input("Enter a number: "))

# Call the check_even_odd function with the user input and store the result
result = check_even_odd(num)

# Print the result indicating whether the number is even or odd
print(f"The number {num} is an {result} number.")




