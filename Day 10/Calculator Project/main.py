from art import logo

def add(n1, n2):
    return n1 + n2

def subtract(n1, n2):
    return n1 - n2

def multiply(n1, n2):
    return n1 * n2

def divide(n1, n2):
    return n1 / n2

operations = {
     "+" : add,
     "-" : subtract,
     "*" : multiply,
     "/" : divide,
}
should_continue = True
print(logo + "\nWelcome to our calculator")
while should_continue:
    num1 = float(input("What's the first number?: "))
    while True:
        for operator in operations:
            print(operator)
        op = input("Pick an operator: ")
        num2 = float(input("What's the second number?: "))

        result = operations[op](num1, num2)
        print(f"{num1} {op} {num2} = {result}")
        keep_result = input(f"Do you want to continue working with the {result}? y/n: ")
        if keep_result == "y":
            num1 = result
        else:
            break
    keep_calc = input("Do you still want calculating? y/n: ")
    if keep_calc == "n":
        print("Thank you for using our calculator, have a nice day")
        should_continue = False