def isRotation(s1, s2):
    new_string = s1 + s1
    return isSubstring(s2, new_string)

def isSubstring(s1, s2):
    return s1 in s2

print('Is Rotation: ', isRotation('waterbottle', 'erbottlewat'))
print('Is Rotation: ', isRotation('waterbottle', 'siddharth'))