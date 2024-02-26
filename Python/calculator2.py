# Filename : calculator.py
# learn by : youtube jenny
# data : 2024-2-26

def add(a,b):
    return a+b
def subtract(a,b):
    return a-b
def multiply(a,b):
    return a*b
def divide(a,b):
    return a/b

operations_dict={
    "+":add,
    "-":subtract,
    "*":multiply,
    "/":divide
}

def calculator():
    number1=int(input("enter your first number:"))
    for symbol in operations_dict:
        print(symbol)

    continue_flag=True
    while continue_flag:
        op_symbol=input("pick an operation")
        number2=int(input("enter next number:"))
        calulator_function=operations_dict[op_symbol]
        output=calulator_function(number1,number2)
        print(f"{number1}{op_symbol}{number2}={output}")
        should_continue=input(f"enter 'y‘ to continue calculation with {output} or 'n' to start a new calculation or 'x' to exit").lower()
        if should_continue=='y':
            number1=output
        elif should_continue=='n':
            continue_flag = False
            calculator()
        else:
            continue_flag=False
            print("Bye")

calculator()
