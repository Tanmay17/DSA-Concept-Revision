class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None

    def insertData(self, data, pos):
        newNode = Node(data)
        if pos != 1:
            count = 1
            temp = self.head
            while count < pos-1:
                temp = temp.next
                count = count + 1
            newNode.next = temp.next
            temp.next = newNode
        
        if pos == 1:
            newNode.next = self.head
            self.head = newNode
    
    def printList(self):
        temp = self.head
        while (temp):
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

    pos = int(input())
    list.insertData(6, pos)

    list.printList()