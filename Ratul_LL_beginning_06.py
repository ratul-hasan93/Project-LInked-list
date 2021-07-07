# Linked list insert at beginning

class Node:
    def __init__(self, data = "head", next = None):
        self.data = data
        self.next = next

class linked_list:
    def __init__(self):
        self.head = Node()

    def insert(self, data):
        node = Node(data, self.head.next)
        self.head.next = node

    def printing(self):
        if self.head.next is None:
            print("Empty")
            return

        c_node = self.head
        string = ""

        while c_node != None:
            string = string + str(c_node.data) + ' ---> '
            c_node = c_node.next

        print(string)

if __name__ == "__main__" :
    LL = linked_list()

    LL.insert(5)
    LL.insert(3)
    LL.printing()

