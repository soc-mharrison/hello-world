''' DOCSTRING
Week 5 Class Challenge Tasks 1-3
by Yourname
date: 29.02.24
version 2
'''

# Functions -----------


# Task 2 copy Functions poster code functions.py
# Number machine
def number_machine(x):
  x = x * 10 / 2
  print(int(x))
  return x


# GST Calculator
def gst_calculator(amount):
  amount_with_gst = amount * 1.15
  return amount_with_gst


# Task 1) copy lists poster code.py

#Task 1 - copy code to RUN it (PRIMM)
marvel = ["spiderman", "venom", "Black Widow"]
capcom = ["Ryu", "Chun-li", "Poison"]

# MODIFY index -1 means the last item in list
print(marvel[-1], "vs", capcom[1])

# example of calling number machine function
number_machine(10)

# example Task 2 calling
amount = int(input("Enter a price before GST:\n"))
gst_included = gst_calculator(amount)
print("The item for", str(amount), "will cost", str(gst_included), "with GST")
