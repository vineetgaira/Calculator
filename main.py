def user_menu():
    print("Enter the operation that you want to peform.\n" \
    "1 : ADDITION\n" \
    "2 : SUBTRACT\n" \
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

    numbers=list(map(float,input("Enter the numbers that you want to add separated by spaces :").split()))
    sum=0
    for i in numbers:
        sum+=i
    print(f"The sum of your numbers is: {sum}")

def substraction():
    number1=float(input("Enter the first number :"))
    number2=float(input("Enter the number to subsctract from first number:"))

    difference=number1-number2

    print(f"The subtraction of {number1} by {number2} :{difference:.5f}")

def multiplication():
    numbers_prod=list(map(float,input("Enter the numbers that you want to multiply separated by spaces :").split()))
    prod=1
    for i in numbers_prod:
       prod *=i 
    print(f"The product of your numbers is: {prod}")

def division():
    number1=float(input("Enter the number you want to divide :"))
    while True:
        number2=float(input("Enter the number you want to divide with :"))
        if number2==0:
            print("Can not divide by Zero.")
        else:
            division= number1/number2
            print(f"The division of {number1} by {number2} :{division:.5f}")
            break


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