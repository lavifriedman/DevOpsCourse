def all_the_numbers_between_one_to_hundred_that_divide_by_seven():
    for n in range(0, 100):
        if n % 7 == 0:
            print(n)

if __name__ == '__main__':
    all_the_numbers_between_one_to_hundred_that_divide_by_seven()
