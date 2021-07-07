
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