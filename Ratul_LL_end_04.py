# linked list insert at end

class NODE:
    def __init__(self, element = 'Head', next = None):
        self.element = element
        self.next = next

class LINKED_LIST:
    def __init__(self):
        self.head = NODE()

    def insert_at_end(self, element):
        current_node = self.head
        while current_node.next:
            current_node = current_node.next

        current_node.next = NODE(element, None)

    
    def printing(self):
        if self.head.next == None:
            print("LIST IS EMPTY")
            return

        Current_node = self.head
        result_s = ""
        while Current_node:
            result_s = result_s + str (Current_node.element) + ' <-- '
            Current_node = Current_node.next

        print(result_s)

if __name__ == '__main__' :
    LL = LINKED_LIST()

    LL.insert_at_end(23)
    LL.insert_at_end(93)
    LL.insert_at_end(73)
    LL.insert_at_end(43)
    LL.printing()