from operator import itemgetter


def sort_prices(list_of_tupels):
   return sorted(list_of_tupels, key = itemgetter(1), reverse = True)


if __name__ == "__main__":
    list_of_tupels = [('milk', '5.5'), ('candy', '2.5'), ('bread', '9.0')]
    print(sort_prices(list_of_tupels))