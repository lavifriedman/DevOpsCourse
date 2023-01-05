def show_hidden_word(secret_word, old_letters_guessed):
    """fuction receive a string of word and a list of letters,
    and find wich letters from the list are all ready located in the string.
    :param secret_word: a string of word.
    :param old_letters_guessed: list of old letters geussed.
    :type secret_word: str.
    :type old_letters_guessed: list.
    :return word_status: a string of hiden letters except the one that are also in old_letters_guessed.
    :r type: str."""
    word_status = ""
    for n in secret_word:
        if n in old_letters_guessed:
            word_status = word_status + n + " "
        else :
            word_status = word_status + "_ " 
    return word_status

def main():
    secret_word = "mammals"
    old_letters_guessed = ['s', 'p', 'j', 'i', 'm', 'k']
    print(show_hidden_word(secret_word, old_letters_guessed))

if __name__ == "__main__":
    main()