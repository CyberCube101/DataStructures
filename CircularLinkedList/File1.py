# Node class has a constructor that sets the data passed in
# Note that previous node is only used for doubly linked lists


class Node:
    def __init__(self, d, n=None, p=None):
        self.data = d  # 3 attributes to store our data and pointers
        self.next_node = n
        self.prev_node = p

    def __str__(self):
        return ('(' + str(self.data) + ')')


class CircularLinkedList:
    def __init__(self, r=None):
        self.root = r  # keep track of root node
        self.size = 0

    def add(self, d):  # adding a new node, we pass in the data
        if self.size == 0:
            self.root = Node(d)  # initially it points back to itself
            self.root.next_node = self.root  # initially it points back to itself
        else:
            new_node = Node(d, self.root.next_node)
            self.root.next_node = new_node
        self.size += 1

    def find(self, d):  # pass in data to search
        this_node = self.root  # variable to keep track of loop
        while this_node is not None:  # as long as its a valid node
            if this_node.data == d:
                return d
            elif this_node.next_node == self.root:  # we have circled back
                return False
            this_node = this_node.next_node

    def remove(self, d):  # pass in data
        this_node = self.root
        prev_node = None  # we need this too once we find the one we want to remove as the previous node will now point to the next node

        while this_node is not None:
            if this_node.data == d:  # found
                if prev_node is not None:
                    prev_node.next_node = this_node.next_node
                else:
                    while this_node.next_node != self.root:
                        this_node = this_node.next_node
                    this_node.next_node = self.root.next_node
                    self.root = self.root.next_node
                self.size -= 1
                return True
            elif this_node.next_node == self.root:
                return False  # data not found
            prev_node = this_node
            this_node = this_node.next_node

    def print_list(self):
        if self.root is None:
            return
        this_node = self.root
        print(this_node, end='->')
        while this_node.next_node != self.root:
            this_node = this_node.next_node
            print(this_node, end='->')
        print()


cll = CircularLinkedList()
for i in [5, 7, 3, 8, 9]:
    cll.add(i)

my_node = cll.root
print(my_node, end='->')
for i in range(8):
    my_node = my_node.next_node
    print(my_node, end='->')
print()

cll.remove(5)
cll.print_list()
