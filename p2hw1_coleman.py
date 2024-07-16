# JT Coleman
# 6/27/24
# P2HW1
# Create program to calculate travel expenses

print('This program calculates and displays travel expenses')
print()
# Collect needed information
budget = float(input('Enter Budget: '))
location = input('\nEnter your travel destination: ')
fuel_est = float(input('\nHow much do you think you will spend on gas? '))
hotel = float(input('\nApproximately, how much will you need for accomodation/hotel? '))
food = float(input('\nLast, how much do you need for food? '))

#Perform subtraction
total = budget - fuel_est - hotel - food

broke = False

if total < 0:
    broke = True
else:
    broke = False

#Display results
print()
print(12 * "-", 'Travel Expenses', 12 * "-")
print(f'{"Location:":<20}{location}')
print(f'{"Initial Budget:":<20}${budget:,.2f}')
print(f'{"Fuel:":<20}${fuel_est:,.2f}')
print(f'{"Accomodation:":<20}${hotel:,.2f}')
print(f'{"Food:":<20}${food:,.2f}')
print("-----------------------------------------\n")
print(f'{"Remaining Balance:":<20}${total:,.2f}')
print()

input('Press ENTER to close this window')
