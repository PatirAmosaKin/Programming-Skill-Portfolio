# -*- coding: utf-8 -*-
"""
Created on Fri Oct 18 16:38:45 2024

@author: enaje
"""

# Initialize the score and question number
score = 0
question_no = 0

# Increment the question number for the first question
question_no += 1
# Prompt the user for the capital of France, converting input to lowercase
ques = input(f'\n{question_no}. What is the capital of France? ').lower()
# Check if the answer matches "Paris" (case insensitive)
if ques.upper() == str.upper("Paris"):
    score += 1  # Increment score for correct answer
    print('Correct! you got 1 point')
else:
    print('Incorrect!')
    print(f'Correct answer is --> Paris')

# ------1
# Increment the question number for the second question
question_no += 1
# Prompt the user for the capital of Netherlands
ques = input(f'\n{question_no}. What is the capital of Netherlands? ').lower()
# Check if the answer matches "Amsterdam"
if ques.upper() == str.upper("Amsterdam"):
    score += 1
    print('Correct! you got 1 point')
else:
    print('Incorrect!')
    print(f'Correct answer is --> Amsterdam')

# -----2
# Increment the question number for the third question
question_no += 1
# Prompt the user for the capital of Finland
ques = input(f'\n{question_no}. What is the capital of Finland? ').lower()
# Check if the answer matches "Helsinki"
if ques.upper() == str.upper("Helsinki"):
    score += 1
    print('Correct! you got 1 point')
else:
    print('Incorrect!')
    print(f'Correct answer is --> Helsinki')

# -----3
# Increment the question number for the fourth question
question_no += 1
# Prompt the user for the capital of Estonia
ques = input(f'\n{question_no}. What is the capital of Estonia? ').lower()
# Check if the answer matches "Tallinn"
if ques.upper() == str.upper("Tallinn"):
    score += 1
    print('Correct! you got 1 point')
else:
    print('Incorrect!')
    print(f'Correct answer is --> Tallinn')

# -----4
# Increment the question number for the fifth question
question_no += 1
# Prompt the user for the capital of Greece
ques = input(f'\n{question_no}. What is the capital of Greece? ').lower()
# Check if the answer matches "Athens"
if ques.upper() == str.upper("Athens"):
    score += 1
    print('Correct! you got 1 point')
else:
    print('Incorrect!')
    print(f'Correct answer is --> Athens')

# ------5 
# Increment the question number for the sixth question
question_no += 1
# Prompt the user for the capital of Denmark
ques = input(f'\n{question_no}. What is the capital of Denmark? ').lower()
# Check if the answer matches "Copenhagen"
if ques.upper() == str.upper("Copenhagen"):
    score += 1
    print('Correct! you got 1 point')
else:
    print('Incorrect!')
    print(f'Correct answer is --> Copenhagen')

# ------6
# Increment the question number for the seventh question
question_no += 1
# Prompt the user for the capital of Hungary
ques = input(f'\n{question_no}. What is the capital of Hungary? ').lower()
# Check if the answer matches "Budapest"
if ques.upper() == str.upper("Budapest"):
    score += 1
    print('Correct! you got 1 point')
else:
    print('Incorrect!')
    print(f'Correct answer is --> Budapest')

# ------7
# Increment the question number for the eighth question
question_no += 1
# Prompt the user for the capital of Norway
ques = input(f'\n{question_no}. What is the capital of Norway? ').lower()
# Check if the answer matches "Oslo"
if ques.upper() == str.upper("Oslo"):
    score += 1
    print('Correct! you got 1 point')
else:
    print('Incorrect!')
    print(f'Correct answer is --> Oslo')

# ------8
# Increment the question number for the ninth question
question_no += 1
# Prompt the user for the capital of Italy
ques = input(f'\n{question_no}. What is the capital of Italy? ').lower()
# Check if the answer matches "Rome"
if ques.upper() == str.upper("Rome"):
    score += 1
    print('Correct! you got 1 point')
else:
    print('Incorrect!')
    print(f'Correct answer is --> Rome')

# ------9
# Increment the question number for the tenth question
question_no += 1
# Prompt the user for the capital of Germany
ques = input(f'\n{question_no}. What is the capital of Germany? ').lower()
# Check if the answer matches "Berlin"
if ques.upper() == str.upper("Berlin"):
    score += 1
    print('Correct! you got 1 point')
else:
    print('Incorrect!')
    print(f'Correct answer is --> Berlin')

# ------10
# Increment the question number for the eleventh question
question_no += 1
# Prompt the user for the capital of Spain
ques = input(f'\n{question_no}. What is the capital of Spain? ').lower()
# Check if the answer matches "Madrid"
if ques.upper() == str.upper("Madrid"):
    score += 1
    print('Correct! you got 1 point')
else:
    print('Incorrect!')
    print(f'Correct answer is --> Madrid')

# ------11

# ------

# Display the total number of questions and the user's score
print(f'\nNumber of questions is {question_no}')
print(f'Your score is {score}')
try:
    # Calculate the percentage of correct answers
    percentage = (score * 100) / question_no
except ZeroDivisionError:
    print('0% questions are correct')  
    # Handle division by zero if no questions were asked

# Display the percentage of correct answers
print(f'{percentage}% questions are correct.')