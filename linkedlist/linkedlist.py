class Node:
    def __init__(self, data = None):
        self.data = data
        self.next = None

    def __str__(self):
        return f"[{self.data}]->{self.next} Node"

class Linkedlist:
    def __init__(self):
        self.head = Node()
    def append(self, data):
        if self.head is None:
            self.head=Node(data)
            return data
        node = self.head
        
        while node.next:
            node = node.next
            
        node.next = Node(data)

    def __str__(self):
        return f"{self.head} ->Linked"





kl = Linkedlist()
kl.append(1)
kl.append(2)
kl.append(10)
kl.append(20)
kl.append(30)
print(kl)
