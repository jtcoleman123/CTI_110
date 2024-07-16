#JT Coleman
#7/11/24
#P4LAB2
#Write a program that displays a multiplication table.

#While loop to control program.
execute = 'Yes'
multiple = 0

while execute.lower() == 'yes': #Check the running variable
    integer = int(input('Enter an integer: ')) #Ask the user for an integer

    print()

    if integer >= 0: #Check if integer is above zero

        for i in range(13): #Repeat this loop 13 times

            print(integer, ' * ', multiple, ' = ', integer * multiple) #Do math and print results

            multiple += 1 #Increment the number to multiply 'integer' by

    else:

        print('Negative integers are not accepted.') #Print if integer is below zero

    execute = input('\nWould you like to run this program again? ') #Ask the user if the program should run again.

print('Program ended')
