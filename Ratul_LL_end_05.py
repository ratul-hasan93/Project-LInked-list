# linked list insert at End
#implementation

class Node:
    def __init__(self, data = "H-START:-->",  next = None):
        self.data = data
        self.next = next

class linked_list:
    def __init__(self):
        self.head = Node()

    def inseart_at_end(self, data):
        c_node = self.head
        while c_node.next:
            c_node = c_node.next

        c_node.next = Node(data, None)

    def printing(self):
        if self.head.next is None:
            print("Linked list is Empty")
            return
        
        c_node = self.head
        r_string = ""
        while c_node:
            r_string = r_string + str (c_node.data) + ' <--< '
            c_node = c_node.next

        print(r_string)


if __name__ == '__main__':
    ll = linked_list()

    ll. inseart_at_end(33)
    ll.inseart_at_end(44)
    ll.inseart_at_end(54)
    ll.inseart_at_end(23)
    ll.printing()