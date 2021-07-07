# linked list finally implementation

from Ratul_LL_finally_done_02 import Node


class NODE:
    def __init__(self, item = "Head", next = None):
        self.item = item
        self.next = next

class LINKED_LIST:
    def __init__(self):
        self.head = NODE()

    def append_at_beginning(self, item):
        node = NODE(item, self.head.next)
        self.head.next = node

    def append_at_end(self, item):
        current_node = self.head
        while current_node.next:
            current_node = current_node.next
        current_node.next = NODE(item, None)

    def Get_length(self):
        cnt = 0
        current_node = self.head
        while current_node:
            cnt += 1
            current_node = current_node.next
        return cnt

    def insert_at(self, index, item):
        if index < 0 or index > self.Get_length():
            print("Invalid Index")
            return

        if index == 0:
            self.append_at_beginning(item)
            return

        cnt = 0
        current_node = self.head
        while current_node:
            if cnt == index - 1:
                node = NODE(item, current_node.next)
                current_node.next = node
                break
            current_node = current_node.next
            cnt += 1

    def printing(self):
        if self.head is None:
            print("Linked list is Empty")
            return

        current_node = self.head
        String = ""
        while current_node:
            String = String + str (current_node.item) + ' ==> '
            current_node = current_node.next
        
        print(String)

if __name__ == '__main__' :
    LL = LINKED_LIST()

    # append at beginning 
    LL.append_at_beginning(32)
    LL.append_at_beginning(22)
    LL.printing()

    # append at end
    LL.append_at_end(43)
    LL.append_at_end(58)
    LL.printing()

    # insert at specific index
    LL.insert_at(3, 90)
    LL.insert_at(4, 100)
    LL.printing()