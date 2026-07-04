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
    
                
def addition(user_choice):
    if user_choice==1:
        numbers=list(map(int,input("Enter the number that you want to add separated by spaces :").split()))
    sum=0
    for i in numbers:
        sum+=i
    print(f"The sum of your numbers is: {sum}")
    return sum 
    

def subtraction():
    pass

def multiplication():
    pass

def division():
    pass

def calculator():
    while True:
        user_menu()
        user_choice=user_input()
        if user_choice==5:
            print("Thanks for using...")
            break
        addition(user_choice)
    
calculator()