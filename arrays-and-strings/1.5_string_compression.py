from collections import OrderedDict

# O(N^2) Solution

def compressedString(input_str):
    outputList = list()
    for index in range(0, len(input_str)):
        outputList.append(input_str[index])
        count = 1
        for indexj in range(index, len(input_str)):
            if input_str[indexj] == index:
                count += 1
        
        outputList.append(str(count))
    
    return "".join(outputList)

print('Compress Siddharth: ', compressedString('Siddharth'))
            



