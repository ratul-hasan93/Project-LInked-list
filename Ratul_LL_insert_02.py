# Linked list insert at spacific index

class NODE:
    def __init__(self, item = "Head", next = None):
        self.item = item
        self.next = next

class linked_list:
    def __init__(self):
        self.head = NODE()

    def get_length(self):
        cnt = 0
        c_node = self.head
        while c_node:
            cnt += 1
            c_node = c_node.next
        return cnt

    def insert_at(self, index, item):
        if index < 0 or index >self.get_length():
            print("Invalid index")
            return
        
        if index == 0:
            self.append_at_beginning(item)
            return

        cnt = 0
        c_node = self.head
        while c_node:
            node = NODE(item, c_node.next)
            c_node.next = node
            break
        c_node = c_node.next
        cnt += 1


    def printing(self):
        if self.head.next is None:
            print("Empty")
            return

        c_node = self.head
        info_string =""
        while c_node:
            info_string = info_string + str(c_node.item) + '---'
            c_node = c_node.next

        print(info_string)

if __name__ == '__main__' :
    LL = linked_list()

    LL.insert_at(1, 10)
    LL.insert_at(2, 20)
    LL.insert_at(3, 40)
    LL.printing()