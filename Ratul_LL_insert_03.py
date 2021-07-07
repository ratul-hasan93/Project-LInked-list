# Linked list insert at spacific index


class Node:
    def __init__(self, element = "Head", next = None):
        self.element = element
        self.next = next

class linked_list:
    def __init__(self):
        self.head = Node()

    def get_length(self):
        cnt = 0
        current_node = self.head
        while current_node:
            cnt += 1
            current_node = current_node.next
        return cnt
    
    def insert_at(self, index, element):
        if index < 0 or index > self.get_length():
            print("Invalid index")
            return
        
        if index == 0:
            self.append_at_beginning(element)
            return

        cnt = 0
        Current_node = self.head
        while Current_node:
            node = Node(element, self.head.next)
            self.head.next = node
            break
        Current_node = Current_node.next
        cnt += 1
    
    
    def printing(self):
        if self.head.next is None:
            print("Empty")
            return

        current_node = self.head
        info_string =""
        while current_node:
            info_string = info_string + str(current_node.element) + '-->'
            current_node = current_node.next

        print(info_string)

if __name__ == '__main__' :
    LL = linked_list()

    LL.insert_at(1, 20)
    LL.insert_at(2, 30)
    LL.printing()
    