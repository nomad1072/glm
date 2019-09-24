class Node:

    def __init__(self, value):
        self.value = value
        self.next = None

def printNode(head):
    while head is not None:
        print(head.value, '->', end="")
        head = head.next

def IsPalindrome(list1, list2):
    isPalindrome = True
    while (list1 is not None) and (list2 is not None):
        if list1.value != list2.value:
            isPalindrome = False
            break

        list1 = list1.next
        list2 = list2.next
    
    return isPalindrome

numbers = [1, 2, 3, 2, 1]
listHead = listTail = Node(numbers[0])
listReverseHead = listReverseTail = Node(numbers[0]) 
for number in numbers[1:]:
    listTail.next = Node(number)
    listTail = listTail.next

    temp = listReverseHead
    listReverseHead = Node(number)
    listReverseHead.next = temp


print("----------------------------------------------", end="\n")
print('List 1: ', end="\n")
printNode(listHead)
print("\n")
print("----------------------------------------------", end="\n")

print("----------------------------------------------", end="\n")
print('List 2: ', end="\n")
printNode(listReverseHead)
print("\n")
print("----------------------------------------------", end="\n")

print("IsPalindrome: ", IsPalindrome(listHead, listReverseHead))
# print("----------------------------------------------", end="\n")
# print('Add Lists 1 and 2: ', end="\n")
# finalList = addLists(list1Head.next, list2Head.next, len(list1), len(list2))
# printNode(finalList)
# print("\n")
# print("----------------------------------------------", end="\n")

