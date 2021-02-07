'''FIRST IN FIRST OUT

Enqueue when adding to the end of the line
Dequeue when removing an item from the front of the line

'''


class Queue():
    def __init__(self):
        self.Queue = list()

    def enqueue(self, item):
        self.Queue.append(item)

    def dequeue(self):
        if len(self.Queue) > 0:
            return self.Queue.pop(0)
        else:
            return None

    def __repr__(self):
        return str(self.Queue)


my_queue = Queue()

my_queue.enqueue(1)
my_queue.enqueue(3)
my_queue.enqueue(5)
my_queue.enqueue(7)

print(my_queue)
my_queue.dequeue()
print(my_queue)
my_queue.dequeue()
print(my_queue)

