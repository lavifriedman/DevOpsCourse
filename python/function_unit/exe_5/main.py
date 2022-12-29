import itertools

word = 'ur mom is a very nice lady'
word_list = list(word)
for l in range(len(word_list) + 1):
    for combo in itertools.combinations(word, l):
        print(combo)
