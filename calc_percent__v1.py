"""
calc_score_percent.py

take user input score, number questions, 
calculate percentage 

by Matt Harrison
date: 01/4/25
version 2
"""

###################
# setup functions
def calc_percentage(a,b):
  result = a/b*100
  return result

###################
# setup variables

score = int(input("Enter score"))
number_questions = int(input("Enter the number of questions"))

percentage = calc_percentage(score, number_questions)
print("The player's percentage:", percentage, "%")
