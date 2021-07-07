# Linked list insert at beginning

class NODE:
    def __init__(self, data = "Head", next= None):
        self.data = data
        self.next = next

class LINKEDLIST:
    
    def __init__(self):
        self.head = NODE()

    def insert_at_begginning(self, data):
        node = NODE(data, self.head.next)
        self.head.next = node

    def printing_linkedlist(self):
        if self.head.next is None:
            print("Empty")
            return
        
        current_node = self.head

        string = ""
        while current_node != None:
            string = string + str (current_node.data) + ' --> '
            current_node = current_node.next

        print(string)

if __name__ == '__main__' :
    LL = LINKEDLIST()

    LL.insert_at_begginning(15)
    LL.insert_at_begginning(10)
    LL.insert_at_begginning(20)
    LL.printing_linkedlist()