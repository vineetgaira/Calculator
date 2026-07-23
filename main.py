import colorama
from colorama import Fore

colorama.init()

def user_menu():
    print(Fore.GREEN + "Enter the operation that you want to peform.\n" \
    "1 : ADD\n" \
    "2 : SUB\n" \
    "3 : MULTIPLY\n" \
    "4 : DIVIDE\n"
    "5 : PERCENTAGE\n"
    "6 : EXIT." + Fore.RESET)

def user_input():
    valid_choices={1,2,3,4,5,6}
    while True:
        try:
            user_choice=int(input(Fore.BLUE +"Enter your choice:"+Fore.RESET))
            if user_choice in valid_choices:
                return user_choice
            else:
                print(Fore.RED + "Please enter a valid choice."+Fore.RESET)
        except ValueError:
            print(Fore.RED+"Please enter a valid option from menu." + Fore.RESET)
    
                
def addition():
    while True:
        try:
            numbers=list(map(float,input(Fore.BLUE+"Enter the numbers that you want to add separated by spaces :"+Fore.RESET).split()))
            if not numbers:
                print(Fore.RED+"You didn't enter any numbers. Please try again."+Fore.RESET)
                continue
            total=sum(numbers)
            print(Fore.YELLOW + f"The sum of your numbers is: {total}" + Fore.RESET)
            break
        except ValueError:
            print(Fore.RED + "Please enter valid numbers."+Fore.RESET)


def subtraction():
    while True:
        try:
            number1=float(input(Fore.BLUE+"Enter the first number :"+Fore.RESET))
            number2=float(input(Fore.BLUE+"Enter the number to substract from first number:"+Fore.RESET))

            difference=number1-number2
            print(Fore.YELLOW+f"The subtraction of {number1} by {number2} :{difference:.5f}"+Fore.RESET)
            break
        except ValueError:
            print(Fore.RED+"Please enter valid numbers."+Fore.RESET)

def multiplication():
    while True:
        try:
            numbers_prod=list(map(float,input(Fore.BLUE+"Enter the numbers that you want to multiply separated by spaces :"+Fore.RESET).split()))
            if not numbers_prod:
                print(Fore.RED+"You didn't enter any numbers. Please try again.")
                continue
            prod=1
            for i in numbers_prod:
                prod *=i 
            print(Fore.YELLOW+f"The product of your numbers is: {prod}"+Fore.RESET)
            break
        except ValueError:
            print(Fore.RED+"Please enter valid numbers."+Fore.RESET)


def division():
    while True:
        try:
            number1=float(input(Fore.BLUE+"Enter the number you want to divide :"+Fore.RESET))
            number2=float(input(Fore.BLUE+"Enter the number you want to divide with :"+Fore.RESET))
            division= number1/number2
            print(Fore.YELLOW+f"The division of {number1} by {number2} :{division:.5f}"+Fore.RESET)
            break
        except ZeroDivisionError:
            print(Fore.RED+"Can not divide by Zero."+Fore.RESET)
        except ValueError:
            print(Fore.RED+"Please enter a valid number."+Fore.RESET)

def percentage():
    while True:
        try:
            actual_yield=float(input(Fore.BLUE+"Enter actual yield  :"+Fore.RESET))
            theoritical_yield=float(input(Fore.BLUE+"Enter theoritical yield :"+Fore.RESET))
            percentage = (actual_yield/theoritical_yield)*100
            print(Fore.YELLOW+f"Percentage: {percentage}%"+Fore.RESET)
            break
        except ZeroDivisionError:
            print(Fore.RED+"Theoritical yield can not be Zero."+Fore.RESET)
        except ValueError:
            print(Fore.RED+"Please enter a valid number."+Fore.RESET)

      
def calculator():
    clear_screen()
    while True:
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
            print(Fore.GREEN+"Thanks for using..."+Fore.RESET)
            break
    
if __name__== "__main__":
    calculator()
            


