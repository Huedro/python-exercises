s = "]"

stack = []

char_pairs = {")": "(", "]": "[", "}": "{"}

for char in s:
    if char in ["(", "[", "{"]:
        stack.append(char)
        continue
    if char in [")", "]", "}"]:
        last_opened_char = ""
        if len(stack) != 0:
            last_opened_char = stack.pop()
        if last_opened_char in [")", "]", "}"] or last_opened_char != char_pairs[char]:
            print(False)
print(True)
