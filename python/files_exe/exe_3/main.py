def get_supermarket_inventory():
    with open(r"C:\Users\devops\Desktop\3\inventory.txt", "r") as inventory:
        inventory_list = {}
        for line in inventory:
            product = line.split(": ")
            inventory_list[product[0]] = int(product[1])
        return inventory_list


def client_purchase(inventory_list):
    grocery_name = input("Enter the name of the grocery: ")
    while grocery_name != "stop":
        if grocery_name not in inventory_list.keys():
            grocery_name = input("you enter not legal grocery name, please enter a new grocery: ")
            continue
        grocery_units = input("Enter how many unit you want to bay: ")
        while True:
            if not grocery_units.isdigit():
                grocery_units = input("You enter a illegal units number, please enter again: ")
                continue
            if int(grocery_units) > inventory_list[grocery_name]:
                shortage_message = """The %s unit number you ask is to high (currently there are only %s left).
                please select a new number of units.""" % (grocery_name, inventory_list[grocery_name])
                print(shortage_message)
                grocery_units = input("Please enter again: ")
                continue
            inventory_list[grocery_name] -= int(grocery_units)
            break
        grocery_name = input("Enter the name of the grocery: ")
    return inventory_list


def update_supermarket_inventory_file(inventory_list):
    with open(r"C:\Users\devops\Desktop\3\inventory.txt", "w") as inventory_file:
        for key in inventory_list.keys():
            grocery = "%s: %d" % (key, inventory_list[key])
            inventory_file.write(grocery + "\n")


if __name__ == "__main__":
    print(get_supermarket_inventory())
    update_supermarket_inventory_file(client_purchase(get_supermarket_inventory()))
