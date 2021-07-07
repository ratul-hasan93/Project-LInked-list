# Linked list insert at beginning

class nOdE:
    def __init__(self, element = "head", next = None):
        self.element = element
        self.next = next

class LL:
    def __init__(self):
        self.head = nOdE()

    def insert(self, element):
        node = nOdE(element, self.head.next)
        self.head.next = node

    def print(self):
        if self.head.next == None:
            print("kali")


        c_node = self.head
        r_str = ""

        while c_node != None:
            r_str = r_str + str (c_node.element) + ' :--:> '
            c_node = c_node.next

        print(r_str)

if __name__ == "__main__":
    ll = LL()

    ll.insert(300)
    ll.insert(200)
    ll.insert(100)
    ll.print()


