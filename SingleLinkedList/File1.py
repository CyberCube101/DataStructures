# Node class has a constructor that sets the data passed in
# Note that previous node is only used for doubly linked lists


class Node:
    def __init__(self, d, n=None, p=None):
        self.data = d  # 3 attributes to store our data and pointers
        self.next_node = n
        self.prev_node = p

    def __str__(self):
        return ('(' + str(self.data) + ')')


class LinkedList:
    def __init__(self, r=None):
        self.root = r  # keep track of root node
        self.size = 0

    def add(self, d):  # adding a new node, we pass in the data
        new_node = Node(d, n=self.root)  # Create new node, passing in the data and the old root node as next
        self.root = new_node  # change root node to new node
        self.size += 1

    def find(self, d):  # pass in data to search
        this_node = self.root  # variable to keep track of loop
        while this_node is not None:  # as long as its a valid node
            if this_node.data == d:
                return d
            else:
                this_node = this_node.next_node  # bump us to the next node
        return None

    def remove(self, d):  # pass in data
        this_node = self.root
        prev_node = None  # we need this too once we find the one we want to remove as the previous node will now point to the next node

        while this_node is not None:
            if this_node.data == d:
                if prev_node is not None:
                    prev_node.next_node = this_node.next_node
                else:  # data is in root
                    self.root = this_node.next_node
                self.size -= 1
                return True
            else:
                prev_node = this_node  # if we haven't found what we are looking for we need to loop the previous node
                this_node = this_node.next_node  # as well as current node to the next node

    def print_list(self):
        this_node = self.root
        while this_node is not None:
            print(this_node, end='->')
            this_node = this_node.next_node  ## same as i=i+1
        print('None')


myList = LinkedList()
myList.add(5)
myList.add(8)
myList.add(12)
myList.print_list()
myList.remove(8)
myList.print_list()
print(myList.root)
