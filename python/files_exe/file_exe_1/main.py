def open_car_file():
    with open(r"C:\Users\devops\Desktop\1\cars.txt", "r") as car_file:
        for line in car_file:
            car_properties = line.split("-")
            string = "%s mady in year %s" % (car_properties[0], car_properties[1])
            print(string)


if __name__ == '__main__':
    open_car_file()