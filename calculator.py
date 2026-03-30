while True:
    print("\n--- Calculator Menu ---")
    print("1. Add")
    print("2. Subtract")
    print("3. Multiply")
    print("4. Divide")
    print("5. Exit")
    try:
        choice = int(input("Enter choice: "))
        if choice == 5:
            print("Exiting...")
            break
        a = float(input("Enter first number: "))
        b = float(input("Enter second number: "))
        if choice == 1:
            print("Result:", a + b)
        elif choice == 2:
            print("Result:", a - b)
        elif choice == 3:
            print("Result:", a * b)
        elif choice == 4:
            if b == 0:
                raise ZeroDivisionError("Cannot divide by zero")
            print("Result:", a / b)
        else:
            print("Invalid Operator")
    except ZeroDivisionError as e:
        print("Error:", e)
