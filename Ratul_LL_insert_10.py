# Linked list insert implementation at spacific index

class Node:
    def  __init__(self, data = "Head" , next = None):
        self.data = data
        self.next = next

class Link_list:
    def __init__(self):
        self.head = Node()

    def get_length(self):
        cnt = 0
        c_node = self.head
        while c_node:
            cnt += 1
            c_node = c_node.next
        return cnt

    def insert(self , index, data):
        if index < 0 or index > self.get_length():
            print("Invalid index")
            return
        
        if index == 0:
            self.append(data)
            return
        
        cnt = 0
        c_node = self.head
        while c_node:
            if cnt == index - 1:
                node = Node(data, c_node.next)
                c_node.next = node
                break
            c_node = c_node.next
            cnt += 1

    def printing(self):
        if self.head.next is None:
            print("Empty")
            return

        c_node = self.head
        string = ""
        while c_node:
            string = string + str (c_node.data) + ' --> '
            c_node = c_node.next

        print(string) 

if __name__ == '__main__' :
    LL = Link_list()

    LL.insert(1, 33)
    LL.insert(2, 25)
    LL.insert(3, 43)
    LL.insert(4, 67)
    LL.printing()