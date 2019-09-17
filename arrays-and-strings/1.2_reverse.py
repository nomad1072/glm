def string_reverse(input_str):
    # return input_str[::-1]
    strlen = len(input_str)
    output_str = list(input_str)
    for index in range(0, int(len(input_str)/2)):
        temp = output_str[index]
        output_str[index] = output_str[strlen - index - 1]
        output_str[strlen - index - 1] = temp

    return "".join(output_str)

print('Reverse String: ', string_reverse('Siddharth'))