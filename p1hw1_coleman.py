# JT Coleman
# 6/18/24
# P1HW1
# Create a script that performs mathematical functions

# Create header
print('----Calculating Exponents----')
print()

# Requests input from user
base = int(input('Enter a value as the base integer:'))
exponent = int(input('Enter a value as the exponent:'))

# Performs the equation treating input as integers
total = pow(base, exponent)

# Shows results
print(str(base), ' to the power of ', str(exponent), ' is ', str(total))

print()
print()

# Create header
print('----Addition and Subtraction---')

#Request input from user
number = int(input('Enter a value as the starting integer:'))
add = int(input('Enter a value as the integer to add:'))
sub = int(input('Enter a value as the integer to subtract:'))

#Perform equation
result = number + add - sub

#Display results
print(number, ' + ', add, " - ", sub, " is equal to", result)
