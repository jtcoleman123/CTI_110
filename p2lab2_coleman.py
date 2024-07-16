#JT Coleman
#6/25/24
#P2LAB2
#Create a dictionary to store data

#Create the dictionary
my_dict = {
    'Camaro': 18.21,
    'Prius': 52.36,
    'Model S': 110,
    'Silverado': 26
    }
#Assign variable
keys = my_dict.keys()

print(keys)
print()

#Get user input
vehicle = input("Enter a vehicle to see it's MPG: ")
print()

mpg = float(my_dict.get(vehicle))

#Display selected vehicle
print('The', vehicle, 'gets', mpg, 'MPG.')
print()

#Get mileage info
miles = float(input('How many miles will you drive the ' + vehicle + '? '))
print()

#Perform required math
fuel_needed = miles / mpg


print(f"{format(fuel_needed, '.2f')} gallon(s) of gas are needed to drive the {vehicle} {miles} miles.")
print()
input('Press ENTER to close!')
