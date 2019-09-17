# Solution with extra space
def isPermutation(input_str, next_str):
    d = dict()
    for letter in input_str:
        if letter not in d:
            d[letter] = 1
        else:
            d[letter] += 1

    for letter in next_str:
        if letter not in d:
            return False
        else:
            d[letter] -= 1

    return True


# Another solution is an O(N^2) match which is not ideal

print("Is Permutation: ", isPermutation('sidd', 'dis'))
print("Is Permutation: ", isPermutation('sidd', 'pis'))