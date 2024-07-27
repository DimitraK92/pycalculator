from os import system
import signal
from art import logo

def handler(signum, frame):
    system("cls")
    exit(1)

signal.signal(signal.SIGINT, handler)

def add(n1, n2):
  return n1 + n2

def subtract(n1, n2):
  return n1 - n2

def multiply(n1, n2):
  return n1 * n2

def divide(n1, n2):
  return n1 / n2

operations = {
  "+": add,
  "-": subtract,
  "*": multiply,
  "/": divide
}

def validate_num(user_input):
  num = 0
  is_valid = False
  while not is_valid: 
    try:
      num = float(user_input)
      is_valid = True
    except Exception:
      user_input = input("Only numbers are allowed. Try again: ")
  return num
  
def calculator():
  print(logo)
  num1 = validate_num(input("What's the first number?: "))
  for symbol in operations: print(symbol) 
  
  should_continue = True
  while should_continue:
    operation_symbol = input("Pick an operation: ")
    while operation_symbol not in operations.keys():
      operation_symbol = input("Invalid input. Try again: ")
      
    num2 = validate_num(input("What's the next number?: "))
    
    calculation_function = operations[operation_symbol]
    answer = calculation_function(num1, num2)
    print(f"{num1} {operation_symbol} {num2} = {answer}")

    next_option = input(f"Type 'y' to continue calculating with {answer}, or\ntype 'n' to start a new calculation, or\ntype 'e' to exit: ").upper() 
    while next_option not in ['Y', 'N', 'E']:
      next_option = input("Invalid input. Try again: ").upper()
    
    if next_option == 'Y':
      num1 = answer
    elif next_option == 'N':
      should_continue = False
      system("cls")
      calculator()
    else: return
      
calculator()
