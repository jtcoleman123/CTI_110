# JT Coleman
# 6/20/24
# P1HW2
# Create program to calculate travel expenses

print('This program calculates and displays travel expenses')

# Collect needed information
budget = int(input('Enter Budget:'))
location = input('Enter your travel destination:')
fuel_est = int(input('How much do you think you will spend on gas? '))
hotel = int(input('Approximately, how much will you need for accomodation/hotel? '))
food = int(input('Last, how much do you need for food? '))

#Perform subtraction
total = budget - fuel_est - hotel - food

#Display results
print('\n--------Travel Expenses--------')
print()
print('Location: ', location)
print('Initial Budget: ', budget)
print()
print('Fuel: ', fuel_est)
print('Accomodation: ', hotel)
print('Food: ', food)
print()

print('Remaining Balance: ', total)

print()
input('Press ENTER to close this window')
