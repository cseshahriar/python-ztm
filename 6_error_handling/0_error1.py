# Error handling

while True:
    try:
        age = int(input("What is your age? "))
        print(age)
        print(10/age)
        # raise ValueError("Age must be int")  # trough error
    except ValueError:
        print("Invalid input! Age must be a number.")
    except ZeroDivisionError:
        print("Cannot divide by zero.")
    else:
        print("Thank you")
        break
    finally:
        print("This code will always run")
