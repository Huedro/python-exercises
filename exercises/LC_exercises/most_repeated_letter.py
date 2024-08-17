sentence = "This is a common interview question"
letters = set([*sentence])
letters.remove(" ")

letters_count = ([letter, sentence.count(letter)] for letter in letters)
most_repeated = ["", 0]
for letter in letters_count:
    if letter[1] > most_repeated[1]:
        most_repeated = letter


print("Letter:", most_repeated[0])
