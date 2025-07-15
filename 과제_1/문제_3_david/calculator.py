def add(a, b):
    return a + b

def subtract(a, b):
    return a - b

def multiply(a, b):
    return a * b

def divide(a, b):
    if b == 0:
        print("Error: Division by zero.")
        return None
    return a / b


def expression_calculator():
    print("※ 숫자와 연산자를 반드시 띄어쓰기로 구분해서 입력하세요. (예: 2 + 3)")
    print("※ 사용 가능한 연산자는 +, -, *, / 입니다.")
    expr = input("Enter expression: ")
    parts = expr.strip().split()
    if len(parts) != 3:
        print("Invalid expression format.")
        return
    a_str, op, b_str = parts
    try:
        a = float(a_str)
        b = float(b_str)
    except ValueError:
        print("Invalid number input.")
        return
    result = None
    if op == '+':
        result = add(a, b)
    elif op == '-':
        result = subtract(a, b)
    elif op == '*':
        result = multiply(a, b)
    elif op == '/':
        if b == 0:
            print("Error: Division by zero.")
            return
        result = divide(a, b)
    else:
        print("Invalid operator.")
        return
    if result is not None:
        print(f"Result: {result}")

def main():
    mode = input("Select mode: 1) Basic 2) Expression (1/2): ")
    if mode == '2':
        expression_calculator()
        return
    try:
        a = int(float(input("Enter first number: ")))
        b = int(float(input("Enter second number: ")))
    except ValueError:
        print("Invalid number input.")
        return
    op = input("Enter operator (+, -, *, /): ")
    result = None
    if op == '+':
        result = add(a, b)
    elif op == '-':
        result = subtract(a, b)
    elif op == '*':
        result = multiply(a, b)
    elif op == '/':
        result = divide(a, b)
    else:
        print("Invalid operator.")
        return
    if result is not None:
        print(f"Result: {result}")

if __name__ == "__main__":
    main() 