class node:
    def __init__(self, data):
        self.data = data
        self.next = None

class Linkedlist:
    def __init__(self):
        self.head = None

    def append(self, newdata):
        newnode = node(newdata)

        if self.head is None:
            self.head = newnode
            return

        last = self.head

        while last.next:
            last = last.next

        last.next = newnode

    def traversal(self):
        temp = self.head    

        while temp:
            print(temp.data, end=" ")
            temp = temp.next

seth = Linkedlist()

seth.append(77)
seth.append(88)
seth.append(66)

seth.traversal()