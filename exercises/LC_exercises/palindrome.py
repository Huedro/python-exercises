x = 364

if x < 0:
    print(False)

reversed_num = 0
temp = x

while temp != 0:
    digit = temp % 10
    reversed_num = reversed_num * 10 + digit
    temp //= 10

print(reversed_num == x)
