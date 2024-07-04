s = "()"

character_stack = []

for char in s:
    character_stack.append(char)

temp = ""
i = 0
while len(character_stack) != 0:
    if (i + 1) >= len(character_stack):
        break
    if (
        character_stack[i] == "("
        or character_stack[i] == "["
        or character_stack[i] == "{"
    ):
        temp = character_stack[i]
        if (
            character_stack[i + 1] == "("
            or character_stack[i + 1] == "["
            or character_stack[i + 1] == "{"
        ):
            i += 1
        else:
            if temp == "(":
                if character_stack[i + 1] != ")":
                    break
                if character_stack.count(")") >= 1:
                    character_stack.pop(character_stack.index(")"))
                    character_stack.pop(i)
                else:
                    break
            elif temp == "[":
                if character_stack[i + 1] != "]":
                    break
                if character_stack.count("]") >= 1:
                    character_stack.pop(character_stack.index("]"))
                    character_stack.pop(i)
                else:
                    break
            elif temp == "{":
                if character_stack[i + 1] != "}":
                    break
                if character_stack.count("}") >= 1:
                    character_stack.pop(character_stack.index("}"))
                    character_stack.pop(i)
                else:
                    break
            else:
                print("Error")
                break
            i = 0
    else:
        print("Error")
        break

if len(character_stack) == 0:
    print("Valid")
else:
    print("Invalid")
