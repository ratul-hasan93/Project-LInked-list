# Linked list insert at beginning

class NODE:
    def __init__(self, item = "Head", next = None):
        self.item = item
        self.next = next

class L_L:
    def __init__(self):
        self.head = NODE()
    
    def insert_begginning(self,item):
        node = NODE(item, self.head.next)
        self.head.next = node

    def printing(self):
        if self.head.next is None:
            print("Empty linked list")
            return
        

        current_node = self.head
        S = ""
        while current_node != None:
            S = S + str (current_node.item) + ' ---> '
            current_node = current_node.next

        print(S)

if __name__ == "__main__" :
    ll = L_L()

    ll.insert_begginning(10)
    ll.insert_begginning(17)
    ll.insert_begginning(14)
    ll.printing()
        