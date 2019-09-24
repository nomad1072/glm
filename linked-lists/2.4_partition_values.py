class Node:
    def __init__(self, value):
        self.value = value
        self.next = None

def printNodes(head):
    while head is not None:
        print(head.value, '->', end="")
        head = head.next

# Shifts are expensive, maintain two lists and merge them into one. This solution would be more optimal
def partitionNodes(head, partition):
    if head is None:
        return
    
    finalListHead = finalListTail = Node("partition")
    while head is not None:
        if head.value < partition:
            temp = finalListHead
            finalListHead = Node(head.value)
            finalListHead.next = temp
        else:
            finalListTail.next = Node(head.value)
            finalListTail = finalListTail.next
        
        head = head.next

    return finalListHead


numbers = [1, 1, 2, 2, 3, 3, 4, 4, 5, 5, 5, 6, 6, 6, 7, 7, 7, 8, 8, 8, 9, 9, 9, 9, 10, 11, 11, 11]
if len(numbers):
    head = tail = Node(numbers[0])
    for number in numbers[1:]:
        tail.next = Node(number)
        tail = tail.next
    
    printNodes(head)
    finalList = partitionNodes(head, 7)
    print('-'*50, end="\n")
    printNodes(finalList)

