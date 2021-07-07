# linked list insert at end  
#implementation

class Node:
    def __init__(self, data = "Head", next = None):
        self.data = data
        self.next = next

class L_L:
    def __init__(self):
        self.head = Node()

    def insert_at_End(self, data):
        CNT = self.head
        while CNT.next:
            CNT = CNT.next
        CNT.next = Node(data, None)

    def print_end(self):
        if self.head.next is None:
            print("Linked List is Empty")
            return
        
        CNT = self.head
        R_S = ""
        while CNT:
            R_S = R_S + str (CNT.data) + ' --> '
            CNT = CNT.next
        
        print(R_S)

if __name__ == '__main__' :
    ll = L_L()

    ll.insert_at_End(44)
    ll.insert_at_End(76)
    ll.insert_at_End(65)
    ll.print_end()
