# -*- coding: utf-8 -*-
"""
Created on Sat Oct 19 00:54:57 2024

@author: enaje
"""


def hello():
    # Print "Hello" to the console
    print("Hello")  

def Main():  # Define the Main function (capitalized for style)
    # Call the hello() function to execute its code
    hello()  

# Check if the script is being run directly (not imported as a module)
if _name_ == "_main_":
    # Call the Main function to start the program
    Main()