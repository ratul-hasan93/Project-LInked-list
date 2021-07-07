#linked list insert at beginning

class NoDe:
    def __init__(self, item = "Head", next = None):
        self.item = item
        self.next = next

class L_list:
    def __init__(self):
        self.head = NoDe()

    def insert_shurute(self, item):
        node = NoDe(item, self.head.next)
        self.head.next = node

    def printing(self):
        if self.head.next == None:
            print("Empty")
            return
        
        borthoman_node = self.head
        string = ""
        while borthoman_node != None:
            string = string + str (borthoman_node.item) + ' ==> '
            borthoman_node = borthoman_node.next

        print(string)

if __name__ == "__main__" :
    LL = L_list()

    LL.insert_shurute(9)
    LL.insert_shurute(7)
    LL.insert_shurute(3)
    LL.printing()

