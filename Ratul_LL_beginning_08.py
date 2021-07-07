# linked list insert at beginning

class Node:
    def __init__(self, data = "head" , next = None):
        self.data = data
        self.next = next

class Link_L:
    def __init__(self):
        self.head = Node()

    def  insert_at_beg(self, data):
        node = Node(data, self.head.next)
        self.head.next = node

    def print_beg(self):
        if self.head.next == None:
            print("Empty")
            return
        
        cnt = self.head
        result = ""

        while cnt != None:
            result = result + str (cnt.data) + ' ---> '
            cnt = cnt.next

        print(result)

if __name__ == '__main__':
    LL = Link_L()

    LL.insert_at_beg(45)
    LL.insert_at_beg(85)
    LL.insert_at_beg(65)
    LL.insert_at_beg(35)
    LL.print_beg()
