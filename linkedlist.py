from node import Node, BinarySearchTree


class LinkedList:
    def __init__(self):
        self.head = None
        self.tail = None

    def append_node(self, data):
        node = Node(data)

        if self.head is None:
            self.head = node
            self.tail = node
            return
        else:
            self.tail.next = node
            self.tail = self.tail.next

    def prepend_node(self, data):
        if self.head is None:
            new_node = Node(data)
            self.head = new_node
        else:
            new_node = Node(data)
            new_node.next = self.head
            self.head = new_node
            new_node.prev = None

    def copy_list(self):
        bst = BinarySearchTree()
        cur = self.head
        while cur:
            bst.insert(cur.data)
            cur = cur.next
        return bst

    def contains(self, value):
        this_node = self.head
        while this_node:
            if this_node.get_data() == value:
                return value, True
            else: this_node = this_node.get_next()
        return None
