class Node:
    def __init__(self, data = None):
        self.data = data
        self.next = None
        
    def __str__(self):
        return f"[{self.data}]->{self.next} Node"

class Linked_List:
    def __init__(self):
        self.head = None
        
    def append(self, data):
        if self.head is None:
            self.head=Node(data)
            return data
        node = self.head

        while node.next:
            node = node.next

        node.next = Node(data)
        
    def prepend(self, data):
        new_node = Node(data)
        new_node.next = self.head
        self.head = new_node


    def __str__(self):
        return f"{self.head} ->Linked"




kl = Linked_List()
kl.append(5)
kl.append(6)
kl.prepend(3)
kl.prepend(2)
kl.prepend(1)
kl.append(10)
kl.append(20)
kl.append(100)
kl.append(200)
print(kl)
