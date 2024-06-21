def getLeftChild(idx):
    return idx * 2 + 1


def getRightChild(idx):
    return idx * 2 + 2


def getParent(idx):
    return (idx - 1) // 2


def heapifyDown(arr, idx):
    leftIdx = getLeftChild(idx)
    if leftIdx >= len(arr):
        return
    rightIdx = getRightChild(idx)
    value = arr[idx]
    if rightIdx >= len(arr):
        if arr[leftIdx] > value:
            arr[idx] = arr[leftIdx]
            arr[leftIdx] = value
            heapifyDown(arr, leftIdx)
            return
    elif arr[leftIdx] > arr[rightIdx] and arr[leftIdx] > value:
        arr[idx] = arr[leftIdx]
        arr[leftIdx] = value
        heapifyDown(arr, leftIdx)
    elif arr[rightIdx] > value:
        arr[idx] = arr[rightIdx]
        arr[rightIdx] = value
        heapifyDown(arr, rightIdx)


def heapifyUp(arr, idx):
    if idx == 0:
        return
    parentIdx = getParent(idx)
    if arr[idx] < arr[parentIdx]:
        temp = arr[idx]
        arr[idx] = arr[parentIdx]
        arr[parentIdx] = temp
        heapifyUp(parentIdx)


def push(arr, value):
    arr.append(value)
    heapifyUp(arr, len(arr))


def pop(arr):
    arr[0] = arr[len(arr)-1]
    del arr[len(arr)-1]
    heapifyDown(arr, 0)


def swapRootandLast(arr):
    temp = arr[0]
    arr[0] = arr[-1]
    arr[-1] = temp
    return arr


def heapify(arr):
    idx = getParent(len(arr)-1)
    while idx >= 0:
        heapifyDown(arr, idx)
        idx -= 1
    return arr


def heapSort(arr):
    aux = []
    for i in range(len(arr)):
        heapify(arr)
        swapRootandLast(arr)
        aux.append(arr.pop())
    for i in range(len(aux)):
        arr.append(aux.pop())
    return arr


arr = [4, 7, 54, 3, 300, 8, 5, 34, 767, 32, 9, 234, 23]
sorted_arr = heapSort(arr)
print(sorted_arr)
