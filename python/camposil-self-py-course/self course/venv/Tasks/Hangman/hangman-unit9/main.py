def choose_word(file_path, index):
    """"Function open a text file, return number of words except repeated words
    and a word from the list accordingly to received index.
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
        # count the len of the list, ignore repeated words.
        for word in words_list:
            if words_list.count(word) > 1:
                word_count -= 1
                words_list.remove(word)
        return chosen_word


if __name__ == "__main__":
    print(choose_word(r"words-file.txt", 8))