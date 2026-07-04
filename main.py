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
            user_choice=int(input("Enter your choice:"))
            if user_choice in valid_choices:
                return user_choice
            else:
                print("Please enter a valid choice.")
        except ValueError:
            print("Please enter a valid option from menu.")
    
                
def addition():

    numbers=list(map(int,input("Enter the numbers that you want to add separated by spaces :").split()))
    sum=0
    for i in numbers:
        sum+=i
    print(f"The sum of your numbers is: {sum}")

def subtraction():
    pass

def multiplication():
    numbers_prod=list(map(int,input("Enter the numbers that you want to multiply separated by spaces :").split()))
    prod=1
    for i in numbers_prod:
       prod *=i 
    print(f"The product of your numbers is: {prod}")

def division():
    pass

def calculator():
    while True:
        user_menu()
        user_choice=user_input()
        if user_choice==1:
            addition()
        elif user_choice==3:
            multiplication()
        elif user_choice==5:
            print("Thanks for using...")
            break
    
if __name__== "__main__":
    calculator()