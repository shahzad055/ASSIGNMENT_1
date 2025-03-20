try:
    firstNumber = int(input("Enter the first number: "))
    secondNumber = int(input("Enter the second number: "))
    print(f"Addition : {firstNumber + secondNumber}")

    print(f"Subtraction : {firstNumber - secondNumber}")

    print(f"Multiplication : {firstNumber * secondNumber}")

    print(f"Division : {firstNumber / secondNumber}")
except ValueError:
    print("Enter valid Numbers!!")
