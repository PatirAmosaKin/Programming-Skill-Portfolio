# -*- coding: utf-8 -*-
"""
Created on Fri Oct 18 18:41:10 2024

@author: enaje
"""

def days_in_month():
    # Dictionary mapping month numbers to their respective number of days
    month_days = {
        1: 31,   # January has 31 days
        2: 28,   # Default for February (not considering leap years)
        3: 31,   # March has 31 days
        4: 30,   # April has 30 days
        5: 31,   # May has 31 days
        6: 30,   # June has 30 days
        7: 31,   # July has 31 days
        8: 31,   # August has 31 days
        9: 30,   # September has 30 days
        10: 31,  # October has 31 days
        11: 30,  # November has 30 days
        12: 31   # December has 31 days
    }

    # Ask the user for the month number and convert the input to an integer
    month = int(input("Enter the month number (1-12): "))

    # Check if the month is February (month number 2)
    if month == 2:
        # Ask the user if it's a leap year
        leap_year = input("Is it a leap year? (yes/no): ").strip().lower()
        # If the user confirms it's a leap year, update February's days to 29
        if leap_year.upper() == str.upper('yes'):
            month_days[2] = 29

# Retrieve the number of days for the specified month, 
#or return an error message for invalid input
    days = month_days.get(month, "Invalid month number")

    # Print the result showing the number of days in the specified month
    print(f"The number of days in month {month} is: {days}")

# Call the function to execute the code
days_in_month()
