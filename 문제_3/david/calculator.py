def add(a, b):
    c = a + b
    return c

def subtract(a, b):
    c = a - b
    return c

def multiply(a, b):
    c = a * b
    return c

def divide(a, b):
    c = a / b
    return c


def main():

    try:
        number_input = input("계산할 숫자를 입력하세요: ")
        number = int(number_input)
    except ValueError:
        print("Invalid number input.")
        return

    try:
        number2_input = input("두번째 숫자를 입력하세요: ")
        number2 = int(number2_input)
    except ValueError:
        print("Invalid number input.")
        return
    

    operator_input = input("연산자를 입력하세요: ")

    arithmetic_operators = {'+', '-', '*', '/'}
    if operator_input not in arithmetic_operators:
        print("Invalid operator.")
        return

    if number2 == 0 and operator_input == '/':      # 0으로 나눌려고 시도
        print("Error: Division by zero.")
        return


    if operator_input == '+':
        result = add(number, number2)
    elif operator_input == '-':
        result = subtract(number, number2)
    elif operator_input == '*':
        result = multiply(number, number2)
    elif operator_input == '/':
        result = divide(number, number2)

    
    print(f"{number} {operator_input} {number2} = {result} 입니다")
    print(f"Result: {result}")


if __name__ == "__main__":
    main()