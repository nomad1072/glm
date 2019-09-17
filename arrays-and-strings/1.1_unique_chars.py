def unique_chars(input_str):
    d = dict()
    for letter in input_str:
        if letter in d:
            return False
        d[letter] = 1
    
    return True


# Unique String without extra space O(N^2)
def unique_chars_alt(input_str):
    for index, letter in enumerate(input_str):
        for indexj, letterj in enumerate(input_str):
            if index != indexj:
                if letter == letterj:
                    return False

    return True

print('Unique String: ', unique_chars('siddharth'))
print('Unique String: ', unique_chars('abcde'))

print('Unique String Alt: ', unique_chars('siddharth'))
print('Unique String Alt: ', unique_chars('abcde'))
