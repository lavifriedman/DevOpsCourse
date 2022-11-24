def print_frutis(*frutis):
    print_list = []
    for n in frutis:
        print_list.append(n)
        print(print_list)

if __name__ == '__main__':
    print_frutis("lemon", "tot", "new lemon", "chery")
