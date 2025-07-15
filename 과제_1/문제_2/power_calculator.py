def main():
    number_input = input("Enter number: ")
    try:
        number = float(number_input)
    except ValueError:
        print("Invalid number input.")
        return

    exponent_input = input("Enter exponent: ")
    try:
        # int로 변환 시도
        if "." in exponent_input:
            raise ValueError
        exponent = int(exponent_input)
    except ValueError:
        print("Invalid exponent input.")
        return

    result = 1.0
    for _ in range(abs(exponent)):
        result *= number
    if exponent < 0:
        result = 1 / result
    print(f"Result: {int(result) if result.is_integer() else result}")

if __name__ == "__main__":
    main() 