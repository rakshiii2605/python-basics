try:
    num1 = int(input("Enter a number: "))
    num2 = int(input("Enter another number: "))
    result = num1 / num2
    print("Result =", result)
except ValueError:
    print("Error: Please enter valid integers only.")
except ZeroDivisionError:
    print("Error: Division by zero is not allowed.")
finally:
    print("Program execution completed.")
