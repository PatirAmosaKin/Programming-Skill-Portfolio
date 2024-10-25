# -*- coding: utf-8 -*-
"""
Created on Fri Oct 18 17:27:21 2024

@author: enaje
"""

# Print a message indicating that user authentication is required
print("User authentication needed in order to continue")

# Set the number of attempts the user has to enter the correct password
count = 5
# Define the correct password for verification
password = "12345"

# Start a loop that continues until the user runs out of attempts
while count != 0:
    # Prompt the user to enter their password
    password = input("Please enter your password here: ")
    
    # Check if the entered password is correct
    if password == '12345':
        print('User verified. Access granted.')  
        # Inform the user that access is granted
        break  
    # Exit the loop since the user has entered the correct password
    
    # If the password is incorrect
    if password != '12345':
        print('Incorrect password. Please try again.')  
        # Inform the user of the incorrect password
        count -= 1  # Decrement the number of remaining attempts
        print(f'You have {count} attempts remaining.')  
        # Display the number of attempts left

# If the user exhausts all attempts, the else block will execute
else:
    print("No more attempts remaining. Authorities have been alerted.")  
    # Notify the user of no remaining attempts
    
