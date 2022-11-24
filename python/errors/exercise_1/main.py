def divide_two_numbers(num1, num2):
    try:
        num1 = num1 / num2
        return num1
    except ZeroDivisionError:
        print("cant divide a number by zero")

if __name__ == '__main__':
    print(divide_two_numbers(10, 0))


