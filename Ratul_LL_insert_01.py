# Linked list insert implementation at spacific index

class Node:
    def  __init__(self, data = "Head" , next = None):
        self.data = data
        self.next = next

class LINKED_LIST:
    def __init__(self):
        self.head = Node()


    def get_length(self):
        CNT = 0
        current_node = self.head
        while current_node:
            CNT += 1
            current_node = current_node.next
        return CNT
   

    def insert(self,index, data):
        if index < 0 or index > self.get_length():
            print("Invalid Index")
            return

        if index == 0:
            self.append(data)
            return

        CNT = 0
        current_node = self.head
        while current_node:
            if CNT == index -1:
                node = Node(data, current_node.next)
                current_node.next = node
                break
            current_node = current_node.next
            CNT += 1

    def printing(self):
        if self.head.next is None:
            print("Empty")
            return

        current_node = self.head
        string = ""
        while current_node:
            string = string + str (current_node.data) + ' --> '
            current_node = current_node.next

        print(string) 

if __name__ == '__main__' :
    LL = LINKED_LIST()

    LL.insert(1, 33)
    LL.insert(2, 25)
    LL.insert(3, 43)
    LL.printing()