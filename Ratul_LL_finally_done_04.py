# linked list implementation

from Ratul_LL_finally_done_03 import linked_list


class Node:
    def __init__(self, data = "Head", next = None):
        self.data = data
        self.next = next

class Linked_List:
    def __init__(self):
        self.head = Node()

    def append_at_beginning(self, data):
        node = Node(data, self.head.next)
        self.head.next = node

    def append_at_end(self, data):
        current_node = self.head
        while current_node.next:
            current_node = current_node.next
        current_node.next = Node(data, None)

    def get_length(self):
        cnt = 0
        current_node = self.head
        while current_node:
            cnt += 1
            current_node = current_node.next
        return cnt

    def insert_at_specific_index(self, index, data):
        if index < 0 or index > self.get_length():
            print("Invalid Index")
            return

        if index == 0:
            self.append_at_beginning(data)
            return

        cnt = 0
        current_node = self.head
        while current_node:
            if cnt == index - 1:
                node = Node(data, current_node.next)
                current_node.next = node
                break
            current_node = current_node.next
            cnt += 1

    def printing_function(self):
        if self.head is None:
            print("Empty")
            return

        current_node = self.head
        result_s = ""
        while current_node:
            result_s = result_s + str (current_node.data) + ' --> '
            current_node = current_node.next

        print(result_s)


if __name__ == '__main__' :
    LL = Linked_List()

    # append at beginning
    LL.append_at_beginning(329)
    LL.append_at_beginning(454)
    LL.printing_function()

    # append at End
    LL.append_at_end(786)
    LL.append_at_end(348)
    LL.printing_function()

    # insert at specific index
    LL.insert_at_specific_index(5, 3112)
    LL.insert_at_specific_index(6, 9432)
    LL.printing_function()