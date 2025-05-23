def get_first_element(my_list):
  """
  This function takes a list and returns its first element.
  It returns None if the list is empty.
  """
  if not my_list: # Checks if the list is empty
    return None
  print(my_list[0]) # List indices start at 0 for the first element




def greet_user():
  """
  This function takes a name (string) and returns a personalized greeting.
  """
  name = 'Kane'
  print(f"Hello, {name}! Welcome!")





def add(x, y):
    """Adds two numbers"""
    return x + y

def subtract(x, y):
    """Subtracts two numbers"""
    return x - y

def multiply(x, y):
    """Multiplies two numbers"""
    return x * y

def divide(x, y):
    """Divides two numbers"""
    if y == 0:
        return "Error! Division by zero."
        return x / y

def calculator():
    """
    A simple calculator function that takes user input for operations.
    """
    print("Welcome to my simple Calculator!")
    print("Select operation:")
    print("1. Add")
    print("2. Subtract")
    print("3. Multiply")
    print("4. Divide")
    print("5. Exit")

    while True:
        choice = input("Enter choice(1/2/3/4/5): ")

        if choice in ('1', '2', '3', '4'):
            try:
                num1 = int(input("Enter first number: "))
                num2 = int(input("Enter second number: "))
            except ValueError:
                print("Invalid input. Please enter numbers only.")
                continue

            if choice == '1':
                print(f"{num1} + {num2} = {add(num1, num2)}")
            elif choice == '2':
                print(f"{num1} - {num2} = {subtract(num1, num2)}")
            elif choice == '3':
                print(f"{num1} * {num2} = {multiply(num1, num2)}")
            elif choice == '4':
                print(f"{num1} / {num2} = {divide(num1, num2)}")
        elif choice == '5':
            print("Exiting the calculator. Goodbye!")
            break
        else:
            print("Invalid input. Please enter 1, 2, 3, 4, or 5.")


def oddoreven():
        
        """
        A calculation to determine whether a number is even(buzz) or odd(fizz).
        """

        num = int(input("Enter your number:"))

        if num % 2 == 0:
          print("buzz")
        else:
          print("fizz")   

  
       


