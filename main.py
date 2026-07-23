import colorama
from colorama import Fore
colorama.init(autoreset=True)
from utils import clear_screen

def user_menu():
    print(Fore.GREEN + "Enter the operation that you want to peform.\n" \
    "1 : ADD\n" \
    "2 : SUB\n" \
    "3 : MULTIPLY\n" \
    "4 : DIVIDE\n"
    "5 : PERCENTAGE\n"
    "6 : EXIT.")

def user_input():
    valid_choices={1,2,3,4,5,6}
    while True:
        try:
            user_choice=int(input(Fore.BLUE +"Enter your choice:"))
            if user_choice in valid_choices:
                return user_choice
            else:
                print(Fore.RED + "Please enter a valid choice.")
        except ValueError:
            print(Fore.RED+"Please enter a valid option from menu."  )
    
                
def addition():
    while True:
        try:
            numbers=list(map(float,input(Fore.BLUE+"Enter the numbers that you want to add separated by spaces :").split()))
            if not numbers:
                print(Fore.RED+"You didn't enter any numbers. Please try again.")
                continue
            total=sum(numbers)
            print(Fore.YELLOW + f"The sum of your numbers is: {total}"  )
            break
        except ValueError:
            print(Fore.RED + "Please enter valid numbers.")


def subtraction():
    while True:
        try:
            number1=float(input(Fore.BLUE+"Enter the first number :"))
            number2=float(input(Fore.BLUE+"Enter the number to substract from first number:"))

            difference=number1-number2
            print(Fore.YELLOW+f"The subtraction of {number1} by {number2} :{difference:.5f}")
            break
        except ValueError:
            print(Fore.RED+"Please enter valid numbers.")

def multiplication():
    while True:
        try:
            numbers_prod=list(map(float,input(Fore.BLUE+"Enter the numbers that you want to multiply separated by spaces :").split()))
            if not numbers_prod:
                print(Fore.RED+"You didn't enter any numbers. Please try again.")
                continue
            prod=1
            for i in numbers_prod:
                prod *=i 
            print(Fore.YELLOW+f"The product of your numbers is: {prod}")
            break
        except ValueError:
            print(Fore.RED+"Please enter valid numbers.")


def division():
    while True:
        try:
            number1=float(input(Fore.BLUE+"Enter the number you want to divide" ))
            number2=float(input(Fore.BLUE+"Enter the number you want to divide with" ))
            division= number1/number2
            print(Fore.YELLOW+f"The division of {number1} by {number2} :{division:.5f}")
            break
        except ZeroDivisionError:
            print(Fore.RED+"Can not divide by Zero")
        except ValueError:
            print(Fore.RED+"Please enter a valid number")

def percentage():
    while True:
        try:
            actual_yield=float(input(Fore.BLUE+"Enter actual yield  :"))
            theoritical_yield=float(input(Fore.BLUE+"Enter theoritical yield :"))
            percentage = (actual_yield/theoritical_yield)*100
            print(Fore.YELLOW+f"Percentage: {percentage}%")
            break
        except ZeroDivisionError:
            print(Fore.RED+"Theoritical yield can not be Zero.")
        except ValueError:
            print(Fore.RED+"Please enter a valid number.")

      
def calculator():
    while True:
        input(Fore.GREEN+">>Press ENTER to continue")
        clear_screen()
        user_menu()
        user_choice=user_input()
        if user_choice==1:
            addition()
        elif user_choice==2:
            subtraction()
        elif user_choice==3:
            multiplication()
        elif user_choice==4:
            division()
        elif user_choice==5:
            percentage()
        elif user_choice==6:
            print(Fore.GREEN+"Thanks for using...")
            break
    
if __name__== "__main__":
    calculator()
            


