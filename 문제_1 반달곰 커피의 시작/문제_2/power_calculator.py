def main():
    try:
        number_input = input("계산할 숫자를 입력하세요: ")
        number = float(number_input)
    except ValueError:
        print("Invalid number input.")
        return

    try:
        exponent_input = input("지수를 입력하세요: ")
        exponent = int(exponent_input)
    except ValueError:
        print("Invalid exponent input.")
        return
    
    if number == 0.0 and exponent < 0:
        print("0의 음수 제곱은 정의되지 않습니다.")
        return
    

    result = 1.0
    for _ in range(abs(exponent)):      # 지수 절댓값
        result *= number

    if exponent < 0:                    # 음의 지수 처리
        result = 1.0 / result

    print(f"Result: {result}")


if __name__ == "__main__":
    main()
