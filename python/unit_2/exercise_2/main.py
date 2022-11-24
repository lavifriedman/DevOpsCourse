def longest_list(list_one, list_two):
    """function receive two list and return the longest one
    :param list_one: one of the two list function receive.
    :param list_two: one of the two list function receive.
    :return: the name and value of the longest list.
    :rtype: str"""
    if len(list_one) > len(list_two):
        return f'{list_one=}'
    elif len(list_two) > len(list_one):
        return  f'{list_two=}'
    else:
        return "the len of the two list is equal."
def main():
    list_one = [0, 1, 2, 3, 4, 5]
    list_two = [0, 1, 2 ,3,0,0]
    print(longest_list(list_one, list_two))

if __name__ == '__main__':
    main()


