# -*- coding: utf-8 -*-
"""
Created on Sat Oct 19 01:02:48 2024

@author: enaje
"""


def main():
    # Get user input for full name
    name = input("Enter your full name: ")
    # Get user input for hometown
    hometown = input("Enter your hometown: ")
    
    # Start an infinite loop to get a valid age input
    while True:
        age_input = input("Enter your age: ")  # Prompt user for age
        try:
            age = int(age_input)  # Try to convert the input to an integer
            break  # Exit the loop if conversion is successful
        except ValueError:
            # Handle case where input is not a valid integer
            print("Please enter a valid number for age.")

    # Store the user's information in a dictionary
    user_info = {
        "name": name,        # Store name
        "hometown": hometown,  # Store hometown
        "age": age           # Store age
    }

    # Print the user's information on separate lines
    print(f"Name: {user_info['name']}\nHometown: {user_info['hometown']}\nAge: {user_info['age']}")

# Check if this script is being run as the main program
if __name__ == "__main__":
    main()
    
    # Call the main function to execute the program