#JT Coleman
#7/18/24
#P5HW_MathQuiz
#Create a math quiz

import random

def main():
    again = "y"
    print("Welcome to Math Quiz\n")
    while again == "y":
        display_menu()
        number1 = random.randint(10,99)
        number2 = random.randint(10,99)
        choice = input("Please choose one of the menu options: ")
        if choice == '1':
            addition(number1, number2)
        elif choice == '2':
            subtraction(number1, number2)
        elif choice == '3':
            again="n"
        else:
            print("Invalid option")
    print("Thank you for playing...")
    print("Bye!!")

def display_menu():
    print("\nMAIN MENU    ")
    print("--------------------")
    print("1. Adding Random Numbers")
    print("2. Subtracting Random Numbers")
    print("3. Exit\n")

# write your functions here

def addition(add1, add2):
    print("\n ", add1, "\n+", add2)
    answer = add1 + add2
    checkAnswer(answer)

def subtraction(sub1, sub2):
    print("\n ", sub1, "\n-", sub2)
    answer = sub1 - sub2
    checkAnswer(answer)

def checkAnswer(answer):
    guesses_taken = 1
    guess = int(input("\nEnter answer.\n"))

    while guess != answer:
        if guess > answer:
            print("Sorry, guess is too high.\n")
            guess = int(input("Try again: "))
            guesses_taken += 1

        else:
            print("Sorry, guess is too low.\n")
            guess = int(input("Try again: "))
            guesses_taken += 1
    print("Congratulations!!!! Your answer is correct.")
    print("Number of guesses:", guesses_taken)

main()
