#calculator - its an infinite loop execution, kill the terminal to exit

logo = """
 _____________________
|  _________________  |
| | Pythonista   0. | |  .----------------.  .----------------.  .----------------.  .----------------. 
| |_________________| | | .--------------. || .--------------. || .--------------. || .--------------. |
|  ___ ___ ___   ___  | | |     ______   | || |      __      | || |   _____      | || |     ______   | |
| | 7 | 8 | 9 | | + | | | |   .' ___  |  | || |     /  \     | || |  |_   _|     | || |   .' ___  |  | |
| |___|___|___| |___| | | |  / .'   \_|  | || |    / /\ \    | || |    | |       | || |  / .'   \_|  | |
| | 4 | 5 | 6 | | - | | | |  | |         | || |   / ____ \   | || |    | |   _   | || |  | |         | |
| |___|___|___| |___| | | |  \ `.___.'\  | || | _/ /    \ \_ | || |   _| |__/ |  | || |  \ `.___.'\  | |
| | 1 | 2 | 3 | | x | | | |   `._____.'  | || ||____|  |____|| || |  |________|  | || |   `._____.'  | |
| |___|___|___| |___| | | |              | || |              | || |              | || |              | |
| | . | 0 | = | | / | | | '--------------' || '--------------' || '--------------' || '--------------' |
| |___|___|___| |___| |  '----------------'  '----------------'  '----------------'  '----------------' 
|_____________________|
"""


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

# #to add two numbers
# print(operations["+"](1, 1))

# #to multiply two numbers
# print(operations["*"](1, 1))

def get_first_num():
    return float(input("What's the first number?: "))

def get_operation():
        print("+ - / *")
        return input("Pick an operation: ")

def get_second_number():
    return float(input("What's the next number?: "))

def calculator():
    print(logo)
    accumulate = True
    try:
        n1 = get_first_num()
    except:
        print("Invalid input")
        calculator()

    while accumulate:
        try:
            op = get_operation()
            if op not in operations:
                raise Exception
            n2 = get_second_number()        
            result = operations[op](n1, n2)
            print(f"{n1} {op} {n2} = {result}")
            choice = input(f"Type 'y' to calulate with {result} or 'n' to start a new calculation: ")
            if choice.lower() == 'y':
                n1 = result
            else:
                accumulate = False
                calculator() #recursive func call
        except: 
            print("Invalid input")
            calculator()

calculator()