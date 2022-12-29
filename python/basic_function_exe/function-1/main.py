def receive_words_list(words_list):
    for word in words_list:
        if word == 'Hello':
            return 'Welcome'
        elif word == 'Goodbye':
            return 'Goodbye'
        else:
            return 'have a nice day'


def small_to_big(number_list):
    return sorted(number_list)


def find_birth_year(age, current_yer):
    birth_year = current_yer - age
    return birth_year

