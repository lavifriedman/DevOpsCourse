def all_numbers_divide_by_five_and_small_then_150(list_of_numbers):
    for n in list_of_numbers:
        if (n > 500) or (n == 500):
            break
        if (n % 5 == 0) and (n < 150):
            print(n)

if __name__ == '__main__':
    a_list_of_numbers = [12,75,150,180,145,525,50]
    all_numbers_divide_by_five_and_small_then_150(a_list_of_numbers)