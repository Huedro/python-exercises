s = "LVIII"

map = {"I": 1, "V": 5, "X": 10, "L": 50, "C": 100, "D": 500, "M": 1000}

answer = 0

for i in range(len(s)):
    if i < len(s) - 1 and map[s[i]] < map[s[i + 1]]:
        answer -= map[s[i]]
else:
    answer += map[s[i]]

print(answer)
