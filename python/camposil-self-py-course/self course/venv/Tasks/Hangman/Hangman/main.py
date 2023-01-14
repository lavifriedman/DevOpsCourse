def hangman_pictures():
    picture1 = """   x-------x"""

    picture2 = """
        x-------x
        |
        |
        |
        |
        |

    """
    picture3 = """
        x-------x
        |       |
        |       0
        |
        |
        |

    """
    picture4 = """ 
        x-------x
        |       |
        |       0
        |       |
        |
        |

    """
    picture5 = """
        x-------x
        |       |
        |       0
        |      /|\ 
        |
        |

    """
    picture6 = """
        x-------x
        |       |
        |       0
        |      /|\ 
        |      /
        |

    """
    picture7 = """
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
    print("""  _    _                                         
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
    """function receive a string of word and a list of letters,
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
        else :
            word_status = word_status + "_ "
    return word_status


def check_valid_input(letter_guessed, old_letters_guessed):
    """check if the letter_guessed is a single letter from the english alphabet.
    :param letter_guessed: the user input guessed
    :param old_letters_guessed: list of letters the player all radey use.
    :type letter_guessed: str
    :type old_letters_guessed: list
    :return: True/False if letter_guessed is a singl letter
    :rtype: bool.
    """
    english_alphabet = ('a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z')
    letter_guessed_is_single_sing = len(letter_guessed) == 1
    letter_guessed_is_letter = False
    # check if letter_guessed is a letter the player all ready use.
    for letter in old_letters_guessed:
        if letter_guessed.lower() == letter:
            return False
    # check if letter_guessed is a letter in english alphabet
    for letter in english_alphabet:
        if letter == letter_guessed:
            letter_guessed_is_letter = True
            break
    # check if the letter_guessed is a single letter from the englihs alphabet
    if letter_guessed_is_single_sing and letter_guessed_is_letter:
        return True
    else:
        return False


def try_update_letter_guessed(letter_guessed, old_letters_guessed):
    """the function check if the player guess is a single letter that was not guessed before.
    :param letter_guessed: string that present the player guess.
    :param old_letters_guessed: list that contain all the letters the player all ready guessed
    :type letter_guessed: str.
    :type old_letters_guessed: list.
    :return: True/False if letter_guessed is a singel letter that wasnt guessed before.
    :rtype: boll."""
    guessed_is_not_old = True
    str_of_guessed_letters = ""
    # check if letter_guessed was not guessed all ready.
    for letter in old_letters_guessed:
        if letter == letter_guessed:
            guessed_is_not_old = False
            break
    # check if letter_guess is a single letter that is guessed fo the first time.
    if check_valid_input(letter_guessed, old_letters_guessed) and guessed_is_not_old:
        old_letters_guessed.append(letter_guessed.lower())
        return True
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
            index =- len(words_list)
        chosen_word = words_list[index]
        return chosen_word


def hangman(file_path, index):
    """Function run a hangman game, the function collect word from a file with accordingly to the index.
    :param file_path: Path of a file contain words.
    :param: index for a word location in the file.
    :type file_path: str.
    :type index: int
    :return: True if the player win the game 0r False if player los.
    :rtype: bool"""
    secret_word = choose_word(file_path, index)
    old_letter_guessed = []
    MAX_TRIES = 6
    num_of_tries = 0
    HANGMAN_PHOTOS = hangman_pictures()
    print(HANGMAN_PHOTOS[num_of_tries])
    print(show_hidden_word(secret_word, old_letter_guessed))
    letter_guess = input("Enter your guess here: ")
    # The game will continue until player number of tries reach to the max of 6 tries.
    while num_of_tries < MAX_TRIES:
        # Check that the guess of the player is legal.
        if not try_update_letter_guessed(letter_guess, old_letter_guessed):
            letter_guess = input("Enter your guess here: ")
            continue
        # Check if the player is wining.
        if check_win(secret_word, old_letter_guessed):
            return True
        else:
            # Check if player guess is not correct.
            if letter_guess not in secret_word:
                num_of_tries += 1
                print(HANGMAN_PHOTOS[num_of_tries])
            print(show_hidden_word(secret_word,old_letter_guessed))
            letter_guess = input("Enter your guess here: ")
    print(HANGMAN_PHOTOS[MAX_TRIES])
    return False


def main():
    if hangman(r"C:\Users\lavi\DevOpsCourse\DevOpsCourse\python\camposil-self-py-course\self course\venv\Tasks\Hangman\Hangman\venv\words-file", 2):
        print("you win")
    else:
        print("you los")


if __name__ == "__main__":
    main()