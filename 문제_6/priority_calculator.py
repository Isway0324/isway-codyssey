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

def list_devide(a):
    n = len(a)
    number_list = []
    operator_list = []


    if n % 2 == 0 or not n:
        raise ValueError("Invalid input.")
    
    for i in range(n - 1):
        if a[i] == '/' and float(a[i + 1]) == 0:
            raise ZeroDivisionError("Error: Division by zero.")
    
    for i in range((n + 1) // 2):
        try:
            number_list.append(float(a[i * 2]))
        except ValueError:
            raise ValueError("Invalid number.")

    for i in range((n - 1) // 2):
        if a[i * 2 + 1] not in ['+', '-', '*', '/']:
            raise ValueError("Invalid operator")
        
        operator_list.append(a[i * 2 + 1])
    
    return number_list, operator_list


def calculate(a, b):

    if b[0] == '*':                     ## 배열을 합치면 자동으로 줄어든다
        a[1] = multiply(a[0], a[1])
        a[0] = 0
        b[0] = '+'
    if b[0] == '/':
        a[1] = divide(a[0], a[1])
        a[0] = 0
        b[0] = '+'

    for i in range(len(b)):
        if b[i] == '*':
            a[i + 1] = multiply(a[i], a[i + 1])
            a[i] = 0
            b[i] = b[i - 1]
        if b[i] == '/':
            a[i + 1] = divide(a[i], a[i + 1])
            a[i] = 0
            b[i] = b[i - 1]
    
    result = a[0]
    for i in range(len(b)):
        if b[i] == '+':
            result = add(result, a[i + 1])
        if b[i] == '-':
            result = subtract(result, a[i + 1])

    return result


def main():
    try:
        cal_input = list(input("계산할 식을 입력해주세요: ").split())       # list 대신 []

        number, operator = list_devide(cal_input)
    except ZeroDivisionError as e:
        print(f"오류 발생: {e}")
        return
    except ValueError as e:
        print(f"입력 오류: {e}")
        return
    
    if len(number) == 1:
        print(f"Result: {number[0]}")
        return

    result = calculate(number, operator)
    
    print(f"Result: {result}")


if __name__ == "__main__":
    main()