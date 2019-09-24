class Node:

    def __init__(self, value):
        self.value = value
        self.next = None

def printNode(head):
    while head is not None:
        print(head.value, '->', end="")
        head = head.next

def addLists(list1, list2, length1, length2):
    if list1 is None:
        return list2
    if list2 is None:
        return list1

    finalListHead = finalListTail = Node(0)
    carry = 0
    while ((list1 is not None) and (list2 is not None)):
        value = carry + list1.value + list2.value
        print('Value: ', value)
        carry = 1 if value >= 10 else 0
        print('Carry: ', carry)
        finalListTail.next = Node(value % 10)
        finalListTail = finalListTail.next

        list1 = list1.next
        list2 = list2.next

    loopIter = 0
    if list1 is not None:
        if carry > 0 and loopIter == 0:
            finalListTail.next = Node(carry + list1.value)
            finalListTail = finalListTail.next
        else:
            finalListTail.next = Node(list1.value)
            finalListTail = finalListTail.next

        list1 = list1.next
    
    if list2 is not None:
        if carry > 0 and loopIter == 0:
            finalListTail.next = Node(carry + list2.value)
            finalListTail = finalListTail.value
        else:
            finalListTail.next = Node(list2.value)
            finalListTail = finalListTail.value
        
        list2 = list2.next

    return finalListHead.next

        

# Number place values from right to left i.e., units place is last element of the array 
list1 = [1, 2, 3, 4, 5]
list2 = [1, 2, 3, 4, 5]

list1Head = list1Tail = Node(list1[len(list1) - 1])
list2Head = list2Tail = Node(list2[len(list2) - 1])

for number in list1[::-1]:
    list1Tail.next = Node(number)
    list1Tail = list1Tail.next

for number in list2[::-1]:
    list2Tail.next = Node(number)
    list2Tail = list2Tail.next

print("----------------------------------------------", end="\n")
print('List 1: ', end="\n")
printNode(list1Head.next)
print("\n")
print("----------------------------------------------", end="\n")

print("----------------------------------------------", end="\n")
print('List 2: ', end="\n")
printNode(list2Head.next)
print("\n")
print("----------------------------------------------", end="\n")


print("----------------------------------------------", end="\n")
print('Add Lists 1 and 2: ', end="\n")
finalList = addLists(list1Head.next, list2Head.next, len(list1), len(list2))
printNode(finalList)
print("\n")
print("----------------------------------------------", end="\n")




