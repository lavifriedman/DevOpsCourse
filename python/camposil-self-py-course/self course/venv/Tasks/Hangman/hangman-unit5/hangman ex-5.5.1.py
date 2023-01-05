def is_vallid_input(letter_guessed):
    """check if the letter_guessed is a singl letter from the englihs alphabet.
    :param letter_guessed: the user input guessed
    :param str_of_english_alphabet: str of capital/lowr letters of english alphabet.
    :param leteer_guessed_is_singl_sing: check if the len of letter_guessed is one
    :param letter_guessed_is_letter: check if letter_guessed is a letter in english alphabet
    :type letter_guessed: str
    :type str_of_english_alphabet: str
    :type leteer_guessed_is_singl_sing: bool
    :type letter_guessed_is_letter: bool
    :return: True/False if letter_guessed is a singl letter
    :rtype: bool
    """
    str_of_english_alphabet = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"
    leteer_guessed_is_singl_sing = len(letter_guessed) == 1
    letter_guessed_is_letter = False
    #check if letter_guessed is a letter in english alphabet
    for n in str_of_english_alphabet:
        if n == letter_guessed:
            letter_guessed_is_letter = True
            break
    #check if the letter_guessed is a singl letter from the englihs alphabet
    if (leteer_guessed_is_singl_sing) and (letter_guessed_is_letter):
        return True
    else:
        return False

def main():
    #call and check function is_vallid_input
    help(is_vallid_input)
    user_str = input("Enter your guessed here: ")
    print(is_vallid_input(user_str))

if __name__ == "__main__":
    main()
