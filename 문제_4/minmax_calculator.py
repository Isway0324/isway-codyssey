def minimum(a):
    min_number = a[0]

    for num in a:
        if num < min_number:
            min_number = num
    
    return min_number

def maximum(a):
    max_number = a[0]

    for num in a:
        if num > max_number:
            max_number = num
    
    return max_number


def main():
    try:
        number_input = list(map(float, input("숫자를 입력해주세요: ").split()))
    except ValueError:
        print("Invalid number input.")
        return

    print(f"입력받은 숫자는 {number_input} 입니다")

    min = minimum(number_input)
    max = maximum(number_input)


    print(f"최소값: {min}, 최대값: {max}")


if __name__ == "__main__":
    main()