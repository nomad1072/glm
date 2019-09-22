class Node:
    def __init__(self, value):
        self.next = None
        self.value = value

def printNodes(head):
        while head is not None:
            print(head.value, '->', end="")
            head = head.next

def removeNodes(node):
    if node is None or node.next is None:
        return
    
    nextNode = node.next
    node.value = nextNode.value
    node.next = nextNode.next

    return True 

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
