def user_menu():
    print("Enter the operation that you want to peform.\n" \
    "1 : ADDITION\n" \
    "2 : SUBTRACTION\n" \
    "3 : MULTIPLICATION\n" \
    "4 : DIVISION\n"
    "5 : EXIT.")

def user_input():
    valid_choices={1,2,3,4,5}
    while True:
        try:
            user_choice=float(input("Enter your choice:"))
            if user_choice in valid_choices:
                return user_choice
            else:
                print("Please enter a valid choice.")
        except ValueError:
            print("Please enter a valid option from menu.")
    
                
def addition():
    while True:
        try:
            numbers=list(map(float,input("Enter the numbers that you want to add separated by spaces :").split()))
            sum=0
            for i in numbers:
                sum+=i
            print(f"The sum of your numbers is: {sum}")
            break
        except ValueError:
            print("Please enter valid numbers.")


def substraction():
    while True:
        try:
            number1=float(input("Enter the first number :"))
            number2=float(input("Enter the number to substract from first number:"))

            difference=number1-number2
            print(f"The substraction of {number1} by {number2} :{difference:.5f}")
            break
        except ValueError:
            print("Please enter valid numbers.")

def multiplication():
    while True:
        try:
            numbers_prod=list(map(float,input("Enter the numbers that you want to multiply separated by spaces :").split()))
            prod=1
            for i in numbers_prod:
                prod *=i 
            print(f"The product of your numbers is: {prod}")
            break
        except ValueError:
            print("Please enter valid numbers.")


def division():
    while True:
        try:
            number1=float(input("Enter the number you want to divide :"))
            number2=float(input("Enter the number you want to divide with :"))
            division= number1/number2
            print(f"The division of {number1} by {number2} :{division:.5f}")
            break
        except ZeroDivisionError:
            print("Can not divide by Zero.")
        except ValueError:
            print("Please enter a valid number.")
      
def calculator():
    while True:
        user_menu()
        user_choice=user_input()
        if user_choice==1:
            addition()
        elif user_choice==2:
            substraction()
        elif user_choice==3:
            multiplication()
        elif user_choice==4:
            division()
        elif user_choice==5:
            print("Thanks for using...")
            break
    
if __name__== "__main__":
    calculator()
            


