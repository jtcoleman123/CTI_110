#JT Coleman
#7/6/24
#P3LAB
#Calculate change needed to match the entered amount

#Get amount as float, convert to int and multiply by 100 for easier math
money = float(input('Enter the amount of money as a float: '))
money = int(money * 100)

#Check if any change is necessary
if money == 0:
    print('No change')

#Perform calculations
dollars = money // 100
money = money - (dollars * 100)

quarters = money // 25
money = money - (quarters * 25)

dimes = money // 10
money = money - (dimes * 10)

nickels = money // 5
money = money - (nickels * 5)

pennies = money // 1

if dollars > 0:
    print(dollars, end=' ')
    if dollars == 1:
        print("Dollar")
    else:
        print("Dollars")

if quarters > 0:
    print(quarters, end=' ')
    if quarters == 1:
        print("Quarter")
    else:
        print("Quarters")
        
if dimes > 0:
    print(dimes, end=' ')
    if dimes == 1:
        print("Dime")
    else:
        print("Dimes")

if nickels > 0:
    print(nickels, end=' ')
    if nickels == 1:
        print("Nickel")
    else:
        print("Nickels")

if pennies > 0:
    print(pennies, end=' ')
    if pennies == 1:
        print("Penny")
    else:
        print("Pennies")

input('Press Enter to close...')