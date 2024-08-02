def sum(num1, num2):
    try:
        return num1 + num2
    except (TypeError, ZeroDivisionError) as errror:
        print(errror)


print(sum('1', 2))
