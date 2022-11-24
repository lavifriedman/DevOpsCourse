def create_box_tuple():
    length = int(input("enter box length: "))
    width = int(input("enter box width:"))
    height = int(input("enter box height: "))
    return (length, width, height)

def create_closet_tuple():
    length = int(input("enter closet length: "))
    width = int(input("enter closet width:"))
    height = int(input("enter closet height: "))
    return (length, width, height )

def mathc_closet_to_box(box_list, closet_list):
    for closet in closet_list:
        good_mathc = [-1, closet]
        for box in box_list:
            current_box = (10000, 10000, 10000)
            if (box[0] * box[1] *box[2] >= closet[0] * closet[1] * closet[2]):
                if (box[0] * box[1] *box[2] < current_box[0] * current_box[1] * current_box[2]):
                    good_mathc = [box_list.index(box), closet_list.index(closet)]
                    box_list.remove(box)
        print(good_mathc)

def main():
    user_instructions_str = """"wellcome to the closet and box macht app.
    for add a closet please enter 'addcloset'.
    for add box please enter 'addbox'.
    for star match between closet enter 'stop'."""
    closet_list = []
    box_list = []
    print(user_instructions_str)
    user_input = input(": ")
    while user_input != "stop":
        if user_input == 'addcloset':
            new_closet = create_closet_tuple()
            closet_list.append(new_closet)
        elif user_input == 'addbox':
            new_box = create_box_tuple()
            box_list.append(new_box)
        else:
            print("you enter a illegal command, please enter agen a correct command.")
        user_input = input(": ")
    mathc_closet_to_box(box_list, closet_list)

if __name__ == "__main__":
    main()