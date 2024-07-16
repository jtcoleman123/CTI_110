#JT Coleman
#6/30/24
#P2HW2
#Collect grades and display their statistics

#Create a list
gradebook = []

#Get user input for each grade
gradebook.append(float(input('Enter grade for Module 1: ')))
gradebook.append(float(input('Enter grade for Module 2: ')))
gradebook.append(float(input('Enter grade for Module 3: ')))
gradebook.append(float(input('Enter grade for Module 4: ')))
gradebook.append(float(input('Enter grade for Module 5: ')))
gradebook.append(float(input('Enter grade for Module 6: ')))

#Display results, performing math where needed
print()
print(12*'-', 'Results', 12*'-')
print(f'{"Lowest Grade: ":<20}{min(gradebook):.1f}')
print(f'{"Highest Grade: ":<20}{max(gradebook):.1f}')
print(f'{"Sum of Grades: ":<20}{sum(gradebook):.1f}')
print(f'{"Average: ":<20}{sum(gradebook)/len(gradebook):.2f}')
print(33 * '-')

'''

Create the gradebook

Ask for the grade for module 1 and store as a float
Ask for the grade for module 2 and store as a float
Ask for the grade for module 3 and store as a float
Ask for the grade for module 4 and store as a float
Ask for the grade for module 5 and store as a float
Ask for the grade for module 6 and store as a float

Print the header
Get the lowest integer in the list and print it
Get the highest integer in the list and print it
Get the sum of all integers in the list and print it
Get the average of all integers in the list and print it
'''
