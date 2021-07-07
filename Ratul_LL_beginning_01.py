# Linked list implementation insert at beginning

class NODE:
    def __init__(self, data = 'link-list', next = None):
        self.data = data
        self.next = next

class Linked_List:
    def __init__(self):
        self.head = NODE()

    def insert_at_beginning(self, data):
        node = NODE(data, self.head.next)
        self.head.next = node

    def printing_linked_list(self):
        if self.head.next is None:
            print("linked list is Empty")
            return
        
        current_node = self.head
        
        result_str = ""
        while current_node != None:
            result_str = result_str + str (current_node.data) + ' --> '
            current_node = current_node.next

        print(result_str)

if __name__ == "__main__":
    LL = Linked_List()

    LL.insert_at_beginning(10)
    LL.insert_at_beginning(15)
    LL.insert_at_beginning(6)
    LL.printing_linked_list()