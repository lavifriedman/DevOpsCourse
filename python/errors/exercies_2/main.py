def enter_age(age):
    try:
        if type(age) != int:
            raise TypeError
        if (age > 0) and (age < 150):
            return age
        else:
            raise IndexError
    except IndexError:
        print("this age is out of range")
    except TypeError:
        print("the function receive only a natural numbers.")

if __name__ == '__main__':
    print(enter_age(10.90))