
class NODE:
    def __init__(self, data = 'link-list', next = None):
        self.data = data
        self.next = next

class Linked_List:
    def __init__(self):
        self.head = NODE()

    def insert_at_beginning(self, data):
        node = NODE(data, self.head.next)
        self.head.next = node

