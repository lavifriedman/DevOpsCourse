def hangman_pictures():
    picture1 = """   x-------x"""

    picture2 = """
    :(
        x-------x
        |
        |
        |
        |
        |

    """
    picture3 = """
    :(
        x-------x
        |       |
        |       0
        |
        |
        |

    """
    picture4 = """ 
    :(
        x-------x
        |       |
        |       0
        |       |
        |
        |

    """
    picture5 = r"""
    :(
        x-------x
        |       |
        |       0
        |      /|\ 
        |
        |

    """
    picture6 = r"""
    :(
        x-------x
        |       |
        |       0
        |      /|\ 
        |      /
        |

    """
    picture7 = r"""
    :(
        x-------x
        |       |
        |       0
        |      /|\ 
        |      / \
        |

    """

    HANGMAN_PHOTOS = (picture1, picture2, picture3, picture3, picture4, picture5, picture6, picture7)
    return HANGMAN_PHOTOS


def print_hangman():
    """Function print a huge output of 'Hangman'.
     :return: None"""
    print(r"""  
      _    _                                         
     | |  | |                                        
     | |__| | __ _ _ __   __ _ _ __ ___   __ _ _ __  
     |  __  |/ _` | '_ \ / _` | '_ ` _ \ / _` | '_ \ 
     | |  | | (_| | | | | (_| | | | | | | (_| | | | |
     |_|  |_|\__,_|_| |_|\__, |_| |_| |_|\__,_|_| |_|
                          __/ |                      
                         |___/""")


def check_win(secret_word, old_letters_guessed):
    """function check if all the letters in secret_word str are in old_letters_guessed list.
    :param secret_word: string of a word the player need to guess.
    :param old_letters_guessed: list of ll the letters the player all ready guess.
    :type secret_word: str.
    :type old_letters_guessed: list.
    :return: True/False if all the letters of secret_word are in old_letters_guessed.
    :rtype: bool."""
    for n in secret_word:
        if not(n in old_letters_guessed):
            return False
    return True


def show_hidden_word(secret_word, old_letters_guessed):
    """Function receive a string of word and a list of letters,
    and find which letters from the list are all ready located in the string.
    :param secret_word: a string of word.
    :param old_letters_guessed: list of old letters guess.
    :type secret_word: str.
    :type old_letters_guessed: list.
    :return word_status: a string of hide letters except the one that are also in old_letters_guessed.
    :r type: str."""
    word_status = ""
    for letter in secret_word:
        if letter in old_letters_guessed:
            word_status = word_status + letter + " "
        else:
            word_status = word_status + "_ "
    return word_status


def check_valid_input(letter_guessed, old_letters_guessed):
    """Check if the letter_guessed is a single letter from the english alphabet.
    :param letter_guessed: the user input guessed
    :param old_letters_guessed: list of letters the player all ready use.
    :type letter_guessed: str
    :type old_letters_guessed: list
    :return: True/False if letter_guessed is a single letter
    :rtype: bool.
    """
    letter_guessed_is_single_letter = (len(letter_guessed) == 1) and (letter_guessed.isalpha())
    # check if letter is single english letter.
    if not letter_guessed_is_single_letter:
        return False
    # check if letter_guessed is a letter the player all ready use.
    for letter in old_letters_guessed:
        if letter_guessed.lower() == letter:
            return False
    return True


def try_update_letter_guessed(letter_guessed, old_letters_guessed):
    """The function check if the player guess is a single letter that was not guessed before.
    :param letter_guessed: string that present the player guess.
    :param old_letters_guessed: list that contain all the letters the player all ready guessed
    :type letter_guessed: str
    :type old_letters_guessed: list
    :return: True/False if letter_guessed is a single letter that wasn't guessed before
    :rtype: boll."""
    str_of_guessed_letters = ""
    # check if letter_guess is a single letter that is guessed fo the first time.
    if check_valid_input(letter_guessed, old_letters_guessed):
        old_letters_guessed.append(letter_guessed.lower())
        return True
    elif len(letter_guessed) != 0 and not letter_guessed.isalpha():
        print("X")
        return False
    else:
        # convert the list of old letters to a string.
        for n in old_letters_guessed:
            str_of_guessed_letters = str_of_guessed_letters + "->" + n
        print("X\n" + str_of_guessed_letters[2:])
        return False


def choose_word(file_path, index):
    """"Function open a text file, return a word from the list accordingly to received index.
    :param file_path: the path of the text file contain list of words
    :param index: index location of a word from the text file.
    :type file_path: str
    :type index: int
    :return: Word from the file.
    ":rtype: str
    """
    index = index - 1
    with open(file_path, "r") as words_file:
        words_list = words_file.read().split(" ")
        word_count = len(words_list)
        # collect a word from the file.
        while index >= len(words_list):
            index -= word_count
        chosen_word = words_list[index]
        return chosen_word


def hangman(file_path, index):
    """Function run a hangman game, the function collect word from a file with accordingly to the index.
    :param file_path: Path of a file contain words.
    :param: index for a word location in the file.
    :type file_path: str.
    :type index: int
    :return: String that indiceate
    :rtype: bool"""
    secret_word = choose_word(file_path, index)
    old_letter_guessed = []
    MAX_TRIES = 6
    num_of_tries = 0
    HANGMAN_PHOTOS = hangman_pictures()
    print_hangman()
    print(HANGMAN_PHOTOS[num_of_tries])
    print(show_hidden_word(secret_word, old_letter_guessed))
    letter_guess = input("Enter your guess here: ")
    # The game will continue until player number of tries reach to the max of 6 tries.
    while num_of_tries <= MAX_TRIES:
        # Check that the guess of the player is legal.
        if not try_update_letter_guessed(letter_guess, old_letter_guessed):
            letter_guess = input("Enter your guess here: ")
            continue
        # Check if the player is wining.
        if check_win(secret_word, old_letter_guessed):
            return secret_word + "\n" + "WIN"
        else:
            # Check if player guess is not correct.
            if letter_guess not in secret_word:
                num_of_tries += 1
                print(HANGMAN_PHOTOS[num_of_tries])
            print(show_hidden_word(secret_word, old_letter_guessed))
            letter_guess = input("Enter your guess here: ")
    print(HANGMAN_PHOTOS[-1])
    return "LOSE"


def collect_file_path():
    """Function receive from the user the path of a file and check the path is correct.
    :return: True if path for the file is correct or False if file is not found.
    :rtype: bool"""
    file_path = input("Enter please the file path: ")
    while True:
        try:
            with open(file_path, "r"):
                return file_path
        except FileNotFoundError:
            print("Cant find this file, please check the file path agine.")
            file_path = input("Enter please the file path: ")
            return False


def collect_index():
    """Function receive form the user index and convert it to int type variable.
    :return: index type int
    :rtype: int"""
    index = input("Enter please a index: ")
    while True:
        try:
            index = int(index)
            if index < 0:
                return index * -1
            return index
        except ValueError:
            print("You dont enter a whole number for index, please enter a legal number agine.")
            index = input("Enter please a index: ")


def main():
    file_path = collect_file_path()
    index = collect_index()
    print(hangman(file_path, index))


if __name__ == "__main__":
    main()