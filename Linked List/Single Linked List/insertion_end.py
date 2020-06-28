class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None

    def insertData(self, data):
        newNode = Node(data)
        temp = self.head
        while(temp.next):
            temp = temp.next
        temp.next = newNode

    def printList(self):
        temp = self.head
        while(temp):
            print(temp.data)
            temp = temp.next

if __name__ == "__main__":
    list = LinkedList()
    list.head = Node(1)
    second = Node(2)
    third = Node(3)
    fourth = Node(4)
    fifth = Node(5)

    list.head.next = second
    second.next = third
    third.next = fourth
    fourth.next = fifth

    list.insertData(6)

    list.printList()