class Node:
    def __init__(self, value):
        self.next = None
        self.value = value

def printNodes(head):
        while head is not None:
            print(head.value, '->', end="")
            head = head.next

def removeDuplicatesExtraSpace(head):
    if head is None:
        return
        
    nodesVisited = {}
    
    finalListHead = finalListTail= Node(head.value)
    nodesVisited[head.value] = True
    
    head = head.next

    while head is not None:
        
        if head.value not in nodesVisited:
            finalListTail.next = Node(head.value)
            finalListTail = finalListTail.next
            nodesVisited[head.value] = True

        head = head.next
    
    return finalListHead


numbers = [1, 1, 2, 2, 3, 3, 4, 4, 5, 5, 5, 6, 6, 6, 7, 7, 7, 8, 8, 8, 9, 9, 9, 9, 10, 11, 11, 11]
head = tail = Node(numbers[0])

for index, number in enumerate(numbers):
    tail.next = Node(number)
    tail = tail.next

print('-'*100)
print('Input List: ', end="\n")
printNodes(head.next)
print("", end="\n")
print('-'*100)
finalList = removeDuplicatesExtraSpace(head.next)
print("", end="\n")
print('-'*100)
print('Final List: ', end="\n")
printNodes(finalList)
print("", end="\n")
print('-'*100)

    


