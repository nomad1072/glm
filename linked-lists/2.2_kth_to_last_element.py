class Node:
    def __init__(self, value):
        self.next = None
        self.value = value

def printNodes(head):
        while head is not None:
            print(head.value, '->', end="")
            head = head.next

def kThToLast(head, k):
    kNodes = dict()
    loopIndex = 0
    while head is not None:
        kNodes[loopIndex] = head.value
        head = head.next
        loopIndex += 1
    
    return kNodes[loopIndex - k]


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

print('4th to Last: ', kThToLast(head.next, 4))