""" By Yourname
# Title: maths_ops_task4.py
# date: 8/02/23
# Maths Operations Task 3


#this imports task3.py
import task3 #you don't need the suffix .py
"""
# Convert a list to an integer
list_of_ages = ["11", "12", "13", "14"]

# convert a string into an integer
age = input("How old are you?") # string "16"
int_age = int(age)

'''
w3schools example
fruits = ['apple', 'banana', 'cherry']
fruits.append("orange")
'''

list_of_ages.append(age)

print("updated list: ?", list_of_ages)

# setup variables
sub_total = 0
list_of_new_ages = []

for item in list_of_ages:
  new_int = int(item)
  list_of_new_ages.append(new_int)
  sub_total += new_int 
  # sub_total = sub_total + new_int


print("New list:" , list_of_new_ages)
print("Sum of ages: ", sub_total)
