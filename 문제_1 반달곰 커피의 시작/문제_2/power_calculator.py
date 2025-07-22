def main():
    try:
        # 사용자로부터 숫자(실수) 입력
        number_input = input("Enter number: ")
        number = float(number_input)
    except ValueError:
        print("Invalid number input.")
        return

    try:
        # 사용자로부터 지수(정수) 입력
        exponent_input = input("Enter exponent: ")
        exponent = int(exponent_input)
    except ValueError:
        print("Invalid exponent input.")
        return

    # 반복문으로 거듭제곱 계산
    result = 1.0
    for _ in range(abs(exponent)):
        result *= number

    # 음수 지수 처리
    if exponent < 0:
        result = 1.0 / result

    print(f"Result: {result}")


if __name__ == "__main__":
    main()
