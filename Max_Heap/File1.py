'''Every node must be less than or equal to its parent
INSERT in O(log n)
Max in O(1)
Remove Max in O(log n)

Implemented using a list

parent(i)=i/2
left_child(i)=i*2
right_child(i)=i*2+1

Push (insert)
Peek (get max)
Pop (remove max)

A MaxHeap always bubbles the highest value to the top, so it can be removed instantly
Public Functions: push, peek, pop
Private Functions: swap, _floatUp, _bubbleDown, _str
'''


class MaxHeap:
    def __init__(self, items=[]):
        self.heap = [0]  # we want to start at index =1 so this makes index=0 unused
        for item in items:
            self.heap.append(item)
            self.__floatUp(len(self.heap) - 1)

    def push(self, data):
        self.heap.append(data)
        self.__floatUp(len(self.heap) - 1)

    def peek(self):
        if self.heap[1]:
            return self.heap[1]
        else:
            return False

    def pop(self):
        if len(self.heap) > 2:
            self.__swap(1, len(self.heap) - 1)
            max = self.heap.pop()
            self.__bubbleDown(1)  # bubbledown our new first item
        elif len(self.heap) == 2:  # since we filled heap[0] this means there is only 1 item
            max = self.heap.pop()
        else:
            max = False
        return max

    def __swap(self, i, j):
        self.heap[i], self.heap[j] = self.heap[j], self.heap[i]

    def __floatUp(self, index):  # index is the item we want to float up
        parent = index // 2  # get index of its parent
        if index <= 1:
            return
        elif self.heap[index] > self.heap[parent]:
            self.__swap(index, parent)
            self.__floatUp(parent)  # calls recursively on the parent to keep going until it floats up

    def __bubbleDown(self, index):
        left = index * 2  # finds left child
        right = index * 2 + 1  # finds right child
        largest = index
        if len(self.heap) > left and self.heap[largest] < self.heap[left]:
            # if the item we are bubbling down is less than its left child, swap positions with left child
            largest = left
        if len(self.heap) > right and self.heap[largest] < self.heap[right]:  # ""
            largest = right
        if largest != index:
            self.__swap(index, largest)
            self.__bubbleDown(largest)  # keep calling until it reaches its proper position

    def __str__(self):
        return str(self.heap)


if __name__ == '__main__':
    m = MaxHeap([95, 3, 21])
    m.push(10)
    m.push(100)
    m.push(101)

    print(m)
