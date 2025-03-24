"""
functions.py
by Matt Harrison
date: 25/3/25
version 1
"""
####################################
# SET UP FUNCTIONS
# basic function from w3schools.com
def my_function():
  print("Hello from a function")
  
def number_machine(x):
  x = x * 10 / 2
  print("x =:", x)
  
def dog_years(x):
  x = x * 7
  print("Your dog is: ", x, "years old")
  
####################################
# SET UP variables & CONSTANTS
user_input = 0  
  
####################################
# MAIN 
# call FUNCTIONS
my_function()

user_input = int(input("Enter dog's age 1-20"))
#call number_machine() to user the user_input
dog_years(user_input)
