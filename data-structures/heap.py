def getLeftChild(idx):
    return idx * 2 + 1


def getRightChild(idx):
    return idx * 2 + 2


def getParent(idx):
    return (idx - 1) // 2


class Heap:
    def __init__(self, arr=[]):
        self.arr = arr
        self.length = len(arr)

    def heapifyDown(self, idx):
        leftIdx = getLeftChild(idx)
        if leftIdx >= self.length:
            return
        rightIdx = getRightChild(idx)
        value = self.arr[idx]
        if (rightIdx >= self.length or self.arr[leftIdx] < self.arr[rightIdx]) and self.arr[leftIdx] < value:
            self.arr[idx] = self.arr[leftIdx]
            self.arr[leftIdx] = value
            self.heapifyDown(leftIdx)
        elif self.arr[rightIdx] <= self.arr[leftIdx] and self.arr[rightIdx] < value:
            self.arr[idx] = self.arr[rightIdx]
            self.arr[rightIdx] = value
            self.heapifyDown(rightIdx)

    def heapifyUp(self, idx):
        if idx == 0:
            return
        parentIdx = getParent(idx)
        print(idx, parentIdx)
        if self.arr[idx] < self.arr[parentIdx]:
            temp = self.arr[idx]
            self.arr[idx] = self.arr[parentIdx]
            self.arr[parentIdx] = temp
            self.heapifyUp(parentIdx)

    def push(self, value):
        self.arr.append(value)
        self.heapifyUp(self.length)
        self.length += 1

    def pop(self):
        self.arr[0] = self.arr[self.length-1]
        self.length -= 1
        del self.arr[self.length]
        self.heapifyDown(0)


heap = Heap([1, 5, 9, 45, 100])
heap.push(1)
heap.push(300)
heap.push(546)
heap.push(234)
heap.push(68)
heap.push(54)
heap.pop()
heap.pop()
heap.pop()
print(heap.arr)
