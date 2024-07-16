#JT Coleman
#6/25/24
#P2LAB1
#Calculate the dimensions of a circle using the radius

#Load modules needed to perform math
import math

#Check that the user has entered an integer
while True:
    try:
        radius = float(input('What is the radius of the circle? '))
        break
    except ValueError:
        print('Enter a valid integer!')

#Perform math
diameter = radius * 2
circumference = radius * 2 * math.pi
area = math.pi * radius ** 2

print()
print('The diameter of the circle is', format(diameter, '.3f'))
print()
print('The circumference of the circle is', format(circumference, '.3f'))
print()
print('The area of the circle is', format(area, '.3f'))

print()
input('Press ENTER to close...')
