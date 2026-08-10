import os
from colorama import Fore
def clear_screen():
     os.system('cls' if os.name == 'nt' else 'clear')

def show_error(message):
     print(Fore.RED + F"Error: {message}")