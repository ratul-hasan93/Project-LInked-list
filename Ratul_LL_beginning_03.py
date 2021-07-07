
class Node:
    def __init__(self, data = "Start", next = None):
        self.data = data
        self.next = next

class Link_list:
    
    def __init__(self):
        self.head = Node()

    def insert_begginning(self, data):
        node = Node(data, self.head.next)
        self.head.next = node

    def printing(self):
        if self.head.next is None:
            print("empty")
            return

        curr_node = self.head

        string = ""

        while curr_node != None:
            string = string + str (curr_node.data) + ' --> '
            curr_node = curr_node.next
        
        print(string)

if __name__ == '__main__' :
    LL = Link_list()

    LL.insert_begginning(3)
    LL.insert_begginning(2)
    LL.insert_begginning(1)
    LL.printing()