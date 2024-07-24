#JT Coleman
#7/20/24
#FinalProject
#Create a program to manage groceries

#main loop
def main():
    execute = True
    
    global inventory
    inventory = {
    'apples': 3.69,
    'berries': 4.00,
    'chocolate': 2.89,
    'turkey': 6.99,
    'cheese': 4.00,
    'pepsi': 7.89,
    'eggs': 3.50,
    'bread': 3.00
    }
    
    show_avail_items(inventory)

    checkout()

    show_cart(cart)

    calc_total(cart, inventory)

    dispense_change()

    print()

    input('Press ENTER to close...')

#show items in a dictionary
def show_avail_items(dict):
    print(f"\n{'Grocery Item'}{'Price':>18}")
    print('-' * 30)
    for item, price in dict.items():
        print(f"{item:<10}{'$':>16}{price:.2f}")
    print('-' * 30, )

#show checkout menu
def checkout():
    global cart
    cart = []

    completed = False
    print('\n*Welcome to the Grocery Checkout*\n')
    while completed == False:
        user_input = input('Enter an item to add to the cart or type <end> to stop adding items: ')

        if user_input == 'end':
            completed = True
        
        elif user_input in inventory:
            cart.append(user_input)

        else:
            print('That item is not in stock.')

def show_cart(list):
    print('\nThe items currently in your cart are:')
    for item in list:
        print(item)

def calc_total(list, dict):
    print('\nGrocery Checkout Receipt')
    print('-' * 30)
    global total
    total = 0
    for item in list:
        price = inventory.get(item)
        print(f"{item:<10}{'$':>16}{price:.2f}")
        total += price
    
    print(f"\nSUBTOTAL:{'$':>5}{total:.2f}")
    tax = total * 0.02
    print(f"\nTAX:{'$':>10}{tax:.2f}")
    total = total + tax
    print(f"TOTAL:{'$':>8}{total:.2f}")

def dispense_change():
    print(f"\nYou owe ${total:,.2f} for the groceries.\n")

    amount_paid = float(input("How much cash will you put in the self-checkout? "))

    change_due = amount_paid - total

    change_due = int(round(change_due * 100))

    #determine whether there is change to be returned
    if change_due == 0:
        print('No change')
    else:
        print(f"\nThe change owed to you is ${amount_paid - total:,.2f}")
        
        print('\nDispensing...\n')

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