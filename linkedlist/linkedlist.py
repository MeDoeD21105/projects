class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
        
        
class Linkedlist:
    def __init__(self):
        self.head = None
    def append(self, data):
        if self.head is None:
            self.head=Node(data)


    def length(self):
        count = 0
        node = self.head

        while node:
            count += 1

    def elem(self):
        elements = []
        node = self.head
        while node:
            elements.append(node.data)
            node = node.next
        print(elements)

    def __str__(self):
        return f"{self.head} ->Linked"

kl = Linkedlist()
kl.append(1)
kl.append(2)
kl.append(30)
print(kl)
print(kl.length())
kl.elem()