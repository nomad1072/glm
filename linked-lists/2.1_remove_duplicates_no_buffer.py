class Node:
    def __init__(self, value):
        self.next = None
        self.value = value

def printNodes(head):
        while head is not None:
            print(head.value, '->', end="")
            head = head.next

def removeDuplicatesNoBuffer(head):
    if head is None:
        return
    
    print('Here1')
    finalListHead = finalListTail= Node(head.value)
    head = head.next
    print('Here12')

    while head is not None:
        print('Head: ', head.value)
        runner = head
        print('Runner!!', runner.next.value)

        printNodes(runner)
        while runner is not None:
            if runner.next is None:
                break

            if runner.next.value == head.value:
                finalListTail.next = head.next.next
            else:
                finalListTail.next = runner.next

            runner = runner.next
            finalListTail = finalListTail.next

        head = head.next
    
    print('Final List Tail: ', finalListTail)
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
finalList = removeDuplicatesNoBuffer(head.next)
print("", end="\n")
print('-'*100)
print('Final List: ', end="\n")
printNodes(finalList)
print("", end="\n")
print('-'*100)