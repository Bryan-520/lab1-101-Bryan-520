# Takes arguments of 3 numbers to then divide
def calculate_average(num1, num2, num3):
  return (num1 + num2 + num3)/3

# Defines numbers
num1 = float(input("#1: "))
num2 = float(input("#2: "))
num3 = float(input("#3: "))

# Prints it out
print(calculate_average(num1,num2,num3))


# Calculates tax of 10%
def add_tax(price):
  return (price * 0.1) + price

# Input to what price is initially
price = float(input("How much: $"))

# Prints out price with tax
print(add_tax(price))


# Defines the output
def greet_user(name):
  return 'Hello ' + name

# Asks for name
name = input("What is your name? ")

# Prints it out with Hello
print(greet_user(name))