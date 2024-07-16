#JT Coleman
#7/16/24
#P5LAB
#Simulate the change return of a self checkout

import random

#main program function
def main():
    total = round(random.uniform(0.01, 100.00), 2)

    print(f"You owe ${total:,.2f}")

    amount_paid = float(input("How much cash will you put in the self-checkout? "))

    print(f"Change is: ${amount_paid - total:,.2f}\n")

    disperse_change(amount_paid - total)

    input('Press Enter to close...')


#Function to return amount of change
def disperse_change(change_due):
    change_due = int(round(change_due * 100))

    #determine whether there is change to be returned
    if change_due == 0:
        print('No change')

    #get the number of dollars
    dollars = change_due // 100
    change_due = change_due - (dollars * 100)

    #get the number of quarters
    quarters = change_due // 25
    change_due = change_due - (quarters * 25)

    #get the number of dimes
    dimes = change_due // 10
    change_due = change_due - (dimes * 10)

    #get the number of nickels
    nickels = change_due // 5
    change_due = change_due - (nickels * 5)

    #get the number of pennies
    pennies = change_due // 1

    #display amount of dollars
    if dollars > 0:
        print(dollars, end=' ')
        if dollars == 1:
            print("Dollar")
        else:
            print("Dollars")

    #display amount of quarters
    if quarters > 0:
        print(quarters, end=' ')
        if quarters == 1:
            print("Quarter")
        else:
            print("Quarters")

    #display number of dimes
    if dimes > 0:
        print(dimes, end=' ')
        if dimes == 1:
            print("Dime")
        else:
            print("Dimes")

    #display number of nickels
    if nickels > 0:
        print(nickels, end=' ')
        if nickels == 1:
            print("Nickel")
        else:
            print("Nickels")

    #display number of pennies
    if pennies > 0:
        print(pennies, end=' ')
        if pennies == 1:
            print("Penny")
        else:
            print("Pennies")

main()
