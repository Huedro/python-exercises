roman_dict = {
    "I": 1,
    "IV": 4,
    "IX": 9,
    "V": 5,
    "X": 10,
    "XL": 40,
    "XC": 90,
    "L": 50,
    "C": 100,
    "CD": 400,
    "CM": 900,
    "D": 500,
    "M": 1000,
}

string = "MCMXCIV"
string_array = list(string)
temp = ""
integer_number = 0

i = 0
while i < len(string_array):
    if temp == "":
        temp = string[i]
    if (
        (temp != "")
        and (i != len(string_array) - 1)
        and (roman_dict.get(string_array[i]) < roman_dict.get(string_array[i + 1]))
    ):
        temp += string_array[i + 1]
        integer_number += roman_dict.get(temp)
        temp = ""
        i += 2
        continue
    elif (
        (temp != "")
        and (i != len(string_array) - 1)
        and (roman_dict.get(string_array[i]) >= roman_dict.get(string_array[i + 1]))
    ):
        integer_number += roman_dict.get(temp)
        temp = ""
        i += 1
        continue
    integer_number += roman_dict.get(temp)
    i += 1

print(integer_number)
