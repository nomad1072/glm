def replace_space(input_str):
    st = list(input_str)

    for index, letter in enumerate(st):
        if letter == " ":
            st[index] = "%20"

    return "".join(st)

print('Replace Space: ', replace_space('Sai Siddharth Lanka'))
print('Replace Space: ', replace_space('Sai Siddharth Lanka   '))
