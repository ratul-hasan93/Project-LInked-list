# linked list finally all implementation

class Node:
    def __init__(self, data = "Head", next = None):
        self.data = data
        self.next = next

class LINKED_LIST:
    def __init__(self):
        self.head = Node()

    def append_at_beginning(self, data):
        node = Node(data, self.head.next)
        self.head.next = node

    def append_at_end(self, data):
        cur_node = self.head
        while cur_node.next:
            cur_node = cur_node.next
        
        cur_node.next = Node(data, None)

    def get_length(self):
        cnt = 0
        cur_node = self.head
        while cur_node:
            cnt += 1
            cur_node = cur_node.next
        return cnt

    def insert_at(self, index, data):
         if index < 0 or index > self.get_length():
             print("Invalid Index")
             return

         if index == 0:
             self.append_at_beginning(data)
             return

         cnt = 0
         cur_node = self.head
         while cur_node:
             if cnt == index - 1:
                 node = Node(data, cur_node.next)
                 cur_node.next = node
                 break
             cur_node = cur_node.next
             cnt += 1


    def printing(self):
        if self.head is None:
            print("Linked list is Empty")
            return

        cur_node = self.head
        r_str = ""
        while cur_node:
            r_str = r_str + str (cur_node.data) + ' --> '
            cur_node = cur_node.next

        print(r_str)


if __name__ == '__main__' :
    LL = LINKED_LIST()
    
    # append at beginning
    LL.append_at_beginning(30)
    LL.append_at_beginning(20)
    LL.printing()

    # append at end
    LL.append_at_end(100)
    LL.append_at_end(200)
    LL.printing()

    # insert at specific index
    LL.insert_at(1, 500)
    LL.insert_at(4, 600)
    LL.printing()







            
