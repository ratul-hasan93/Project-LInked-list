# linked list insert at end

class Node:
    def __init__(self, data = "Head", next = None):
        self.data = data
        self.next = next
    
class L_end:
    def __init__(self):
        self.head = Node()

    def insert_at_end(self, data):
        c_node = self.head
        while c_node.next:
            c_node = c_node.next

        c_node.next = Node(data, None)

    def printing(self):
        if self.head.next is None:
            print("Empty")
            return

        c_node = self.head
        r_str = ""
        while c_node:
            r_str = r_str + str (c_node.data) + ' -- '
            c_node = c_node.next

        print(r_str)

if __name__ == "__main__" :
    LL = L_end()

    LL.insert_at_end(32)
    LL.insert_at_end(65)
    LL.insert_at_end(323)
    LL.printing()

       
       
