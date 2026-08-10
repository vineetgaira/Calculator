import colorama
from colorama import Fore
colorama.init(autoreset=True)
from utils import clear_screen, show_error



menu_choices = {
    1: "add", 
    2: "sub",
    3: "mul",
    4: "div",
    5: "percentage",
    6: "exit"
}

def user_menu():
    print(Fore.MAGENTA + "="*40)
    print("         CALCULATOR")
    print(Fore.MAGENTA + "="*40)

    print(Fore.WHITE + " [1] ", Fore.LIGHTCYAN_EX + "ADD" )
    print(Fore.WHITE + " [2] ", Fore.LIGHTCYAN_EX + "SUB" )
    print(Fore.WHITE + " [3] ", Fore.LIGHTCYAN_EX + "MUL" )
    print(Fore.WHITE + " [4] ", Fore.LIGHTCYAN_EX + "DIVISION" )
    print(Fore.WHITE + " [5] ", Fore.LIGHTCYAN_EX + "PERCENTAGE" )
    print(Fore.WHITE + " [6] ", Fore.RED + "EXIT" )

def user_input(options, prompt):
    valid_choices=set(options.keys())
    while True:
        try:
            user_choice=int(input(Fore.BLUE +prompt))
            if user_choice in valid_choices:
                return options[user_choice]
            else:
                show_error("Please enter a valid choice.")
        except ValueError:
            show_error("Please enter a valid option from menu.")
    
                
def addition():
    while True:
        try:
            numbers=list(map(float,input(Fore.BLUE+"Enter the numbers that you want to add separated by spaces :").split()))
            if not numbers:
                show_error("You didn't enter any numbers. Please try again.")
                continue
            total=sum(numbers)
            print(Fore.YELLOW + f"The sum of your numbers is: {total}"  )
            break
        except ValueError:
            show_error("Please enter valid numbers.")


def subtraction():
    while True:
        try:
            number1=float(input(Fore.BLUE+"Enter the first number :"))
            number2=float(input(Fore.BLUE+"Enter the number to substract from first number:"))

            difference=number1-number2
            print(Fore.YELLOW+f"The subtraction of {number1} by {number2} :{difference:.5f}")
            break
        except ValueError:
            show_error("Pplease enter valid numbers.")

def multiplication():
    while True:
        try:
            numbers_prod=list(map(float,input(Fore.BLUE+"Enter the numbers that you want to multiply separated by spaces :").split()))
            if not numbers_prod:
                show_error("You did not enter any numbers, try again.")
                continue
            prod=1
            for i in numbers_prod:
                prod *=i 
            print(Fore.YELLOW+f"The product of your numbers is: {prod}")
            break
        except ValueError:
            show_error("Please enter valid numbers.")


def division():
    while True:
        try:
            number1=float(input(Fore.BLUE+"Enter the number you want to divide: " ))
            number2=float(input(Fore.BLUE+"Enter the number you want to divide with: " ))
            division= number1/number2
            print(Fore.YELLOW+f"The division of {number1} by {number2} :{division:.5f}")
            break
        except ZeroDivisionError:
            show_error("Can not divide by Zero")
        except ValueError:
            show_error("Please enter valid numbers.")

def percentage():
    while True:
        try:
            actual_yield=float(input(Fore.BLUE+"Enter actual yield  :"))
            theoritical_yield=float(input(Fore.BLUE+"Enter theoritical yield :"))
            percentage = (actual_yield/theoritical_yield)*100
            print(Fore.YELLOW+f"Percentage: {percentage}%")
            break
        except ZeroDivisionError:
            show_error("Theoritical yield can not be Zero.")
        except ValueError:
            show_error("Please enter a valid number.")

action = {
    "add": addition,
    "sub": subtraction,
    "mul": multiplication,
    "div": division,
    "percentage": percentage,
}
      
def calculator():
    while True:
        user_menu()
        user_choice=user_input(menu_choices, "Enter your choice: ")
        if user_choice == "exit":
            print(Fore.GREEN + "Thanks for using...")
            return
        else:
            fn = action[user_choice]
            fn()
            input(Fore.MAGENTA + "Press [Enter] to return to main menu.")
            clear_screen()

if __name__== "__main__":
    calculator()
            


