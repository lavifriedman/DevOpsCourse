def create_squares(length, height, squares):
    #create the square of sells
    list_len = []
    while len(list_len) < length:
        list_len.append("ded")
    while len(squares) < height:
        squares.append(list_len)
    return squares

#def put_the_first_alive_sell(length_location, height_location, squares):
   # squares[length_location][height_location] = "alive"

def main():
    squares = []
    create_squares(100, 100, squares)
    #put_the_first_alive_sell(0, 0, squares)
    squares[0][0] = "alive"
    for n in squares:
        print(n)

if __name__ == "__main__":
    main()