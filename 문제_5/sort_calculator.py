def bubble_sort(a):
    n = len(a)
    for i in range(n):
        for j in range(n - 1 - i):
            if a[j] > a[j+1]:
                a[j], a[j+1] = a[j+1], a[j]
    return a

def main():
    try:
        number_input = list(map(float, input("숫자들을 입력하세요: ").split()))
        print(f"입력받은 숫자는 {number_input} 입니다")

        if not number_input:
            raise ValueError
    
    except ValueError:
        print("Invalid number input")
        return
    
    result = bubble_sort(number_input)

    print(f"Sorted: {result}")


if __name__ == "__main__":
    main()
