# strs = ["flower", "flow", "flight"]
# strs = ["dog", "racecar", "car"]
# strs = ["Dinosaur", "Dinck", "Dinmonomo"]
# strs = ["flower", "flower", "flower", "flower"]
strs = ["cir", "car"]

# Pegar a primeira palavra do array
# Comparar cada letra da primeira palavra com a primeira letra de todas as outras palavras do array
# Se ela for igual a todas, eu adiciono a letra como um prefix
# Se ela NÃO for igual a todas, eu fecho o programa e entrego o que tem

prefix = ""
first_word = strs[0]
isEndOfPrefix = False

i = 0
while i < len(first_word):
    letter = first_word[i]
    count = 0
    for str in strs:
        if i < len(str) and letter == str[i]:
            count += 1
            if count == len(strs):
                prefix += letter
        else:
            isEndOfPrefix = True
            break
    if isEndOfPrefix:
        break
    i += 1

print(prefix)
