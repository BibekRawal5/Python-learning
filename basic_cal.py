def calculate(operation, n1, n2):
    if operation == '+' :
        return n1 + n2
    elif operation == '-' :
        return n1 - n2
    elif operation == '*':
        return n1 * n2
    else:
        return n1 / n2

def main():
    x = float(input("Enter the first number: "))
    y = float(input("Enter second number: "))
    op = input("Enter the operation to be performed: ")

    result = calculate(op, x, y)

    print(result)


main()