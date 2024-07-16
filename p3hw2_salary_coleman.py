#JT Coleman
#7/9/24
#P3HW2
#Create a program to calculate and display an employee's salary

#Collect necessary information from user
employeeName = input("Enter employees's name: ")
hoursWorked = float(input("Enter numbers of hours worked: "))
payRate = float(input("Enter employee's pay rate: "))

#Calculate overtime and overtime pay if hoursWorked is greater than 40
if hoursWorked > 40:
    overtimeHours = hoursWorked - 40
    overtimePay = overtimeHours * (payRate * 1.5)
    regularPay = payRate * 40
    grossPay = regularPay + overtimePay

#Calculate pay if hoursWorked is less less than 40
else:
    overtimeHours = 0
    overtimePay = 0
    regularPay = payRate * hoursWorked
    grossPay = regularPay

#Display chart
print('-' * 40)
print(f'Employee Name: {employeeName:>5}\n')
print(f'{"Hours Worked":<15}{"Pay Rate":<12}{"Overtime":<12}{"Overtime Pay":<15}{"Regular Pay":<15}{"Gross Pay"}')
print('-' * 80)
print(f'{hoursWorked:<15}{payRate:<12}{overtimeHours:<12.1f}{"$"}{overtimePay:<14,.2f}{"$"}{regularPay:<14,.2f}{"$"}{grossPay:,.2f}')

#Dummy input to prevent terminal from closing once the program finishes
input('Press ENTER to close...')

#Get the employees name
#Get how many hours the employee has worked
#Get the pay rate for the employee

#If the hours worked exceed 40
#   Subtract 40 from worked hours to get overtime
#   Calculate overtime pay
#   Calculate the regular pay
#   Calculate the gross pay

#If the hours worked do not exceed 40
#   Set overtime variables to zero
#   Calculate regular pay and gross pay normally

#Print hyphens for separation
#Print the employee name
#Print the table headers
#More hyphens
#Print the formatted results

#Hold the program until the user is ready to quit
