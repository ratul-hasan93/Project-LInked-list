# linked list insert at end


class NODE:
    def __init__(self, item = "start", next = None):
        self.item = item
        self.next = next

class Linked_List:
    def __init__(self):
        self.head = NODE()

    def insert_at_end(self , item):
        current_node = self.head
        while current_node.next:
            current_node = current_node.next
            
        current_node.next = NODE(item, None)

    def printing(self):
        if self.head.next is None:
            print("Linked list is Empty")
            return
        
        current_node = self.head
        string = ""
        while current_node:
            string = string + str (current_node.item) + ' <-- '
            current_node = current_node.next

        print(string)

if __name__ == '__main__':
    ll = Linked_List()

    ll.insert_at_end(300)
    ll.insert_at_end(600)
    ll.insert_at_end(700)
    ll.printing()
