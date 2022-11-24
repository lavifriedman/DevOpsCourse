import random

def three_random_age():
    a = random.randint(0, 120)
    b = random.randint(0, 120)
    c = random.randint(0, 120)
    two_first_ages_are_small_then_three_age = a + b < c
    if two_first_ages_are_small_then_three_age:
        if a > b:
            return a
        else:
            return b
    else:
        return a

def main():
    print(three_random_age())

if __name__ == '__main__':
    main()

