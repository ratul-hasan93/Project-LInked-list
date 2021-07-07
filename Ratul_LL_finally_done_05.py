# linked list finally implementation

from typing import Counter


class Node:
    def __init__(self, element = "start" ,  next = None):
        self.element = element
        self.next = next

class linked_list:
    def __init__(self):
        self.head = Node()

    def append_at_beginning(self, element):
        node = Node(element, self.head.next)
        self.head.next = node

    def append_at_end(self, element):
        c_node = self.head
        while c_node.next:
            c_node = c_node.next
        c_node.next = Node(element, None)

    def get_length(self):
        cnt = 0
        c_node = self.head
        while c_node:
            cnt += 1
            c_node = c_node.next
        return cnt

    def insert_at_specific_index(self, index, element):
        if index < 0 or index > self.get_length():
            print("Invalid Index")
            return

        if index == 0:
            self.append_at_beginning(element)
            return
        
        cnt = 0
        c_node = self.head
        while c_node:
            if cnt == index - 1 :
                node = Node(element, c_node.next)
                c_node.next = node
                break
            c_node = c_node.next
            cnt += 1

    def printing(self):
        if self.head is None:
            print("Empty Linked list")
            return

        c_node = self.head
        result = ""
        while c_node:
            result = result + str (c_node.element) + ' ---> '
            c_node = c_node.next

        print(result)

if __name__ == '__main__' :
    LL = linked_list()

    # append at beginning
    LL.append_at_beginning(500)
    LL.append_at_beginning(400)
    LL.printing()

    # append at end
    LL.append_at_end(600)
    LL.append_at_end(700)
    LL.printing()

    # insert at specific index
    LL.insert_at_specific_index(3, 4352)
    LL.insert_at_specific_index(5, 8097)
    LL.printing()