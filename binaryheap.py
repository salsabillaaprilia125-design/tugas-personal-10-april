# Membuat Binary Heap
class Heap:
    def __init__(self, size):
        self.customList = (size + 1) * [None]  # array heap
        self.heapSize = 0                      # jumlah data
        self.maxSize = size + 1               # kapasitas maksimum


# Melihat nilai root heap
def peekofHeap(rootNode):
    if not rootNode:
        return
    return rootNode.customList[1]


# Melihat jumlah data heap
def sizeofHeap(rootNode):
    if not rootNode:
        return
    return rootNode.heapSize


# Menampilkan seluruh isi heap
def levelOrderTraversal(rootNode):
    if not rootNode:
        return

    for i in range(1, rootNode.heapSize + 1):
        print(rootNode.customList[i])


# Menyesuaikan posisi saat insert
def heapifyTreeInsert(rootNode, index, heapType):

    parentIndex = int(index / 2)

    if index <= 1:
        return

    # Min Heap
    if heapType == "Min":
        if rootNode.customList[index] < rootNode.customList[parentIndex]:
            temp = rootNode.customList[index]
            rootNode.customList[index] = rootNode.customList[parentIndex]
            rootNode.customList[parentIndex] = temp

        heapifyTreeInsert(rootNode, parentIndex, heapType)

    # Max Heap
    elif heapType == "Max":
        if rootNode.customList[index] > rootNode.customList[parentIndex]:
            temp = rootNode.customList[index]
            rootNode.customList[index] = rootNode.customList[parentIndex]
            rootNode.customList[parentIndex] = temp

        heapifyTreeInsert(rootNode, parentIndex, heapType)


# Menambah data ke heap
def inserNode(rootNode, nodeValue, heapType):

    if rootNode.heapSize + 1 == rootNode.maxSize:
        return "Heap penuh"

    rootNode.customList[rootNode.heapSize + 1] = nodeValue
    rootNode.heapSize += 1

    heapifyTreeInsert(rootNode, rootNode.heapSize, heapType)

    return "Data berhasil ditambahkan"


# Menyesuaikan posisi saat extract
def heapifyTreeExtract(rootNode, index, heapType):

    leftIndex = index * 2
    rightIndex = index * 2 + 1
    swapChild = 0

    if rootNode.heapSize < leftIndex:
        return

    elif rootNode.heapSize == leftIndex:

        if heapType == "Min":
            if rootNode.customList[index] > rootNode.customList[leftIndex]:
                rootNode.customList[index], rootNode.customList[leftIndex] = \
                    rootNode.customList[leftIndex], rootNode.customList[index]

        else:
            if rootNode.customList[index] < rootNode.customList[leftIndex]:
                rootNode.customList[index], rootNode.customList[leftIndex] = \
                    rootNode.customList[leftIndex], rootNode.customList[index]

        return

    else:

        if heapType == "Min":

            if rootNode.customList[leftIndex] < rootNode.customList[rightIndex]:
                swapChild = leftIndex
            else:
                swapChild = rightIndex

            if rootNode.customList[index] > rootNode.customList[swapChild]:
                rootNode.customList[index], rootNode.customList[swapChild] = \
                    rootNode.customList[swapChild], rootNode.customList[index]

        else:

            if rootNode.customList[leftIndex] > rootNode.customList[rightIndex]:
                swapChild = leftIndex
            else:
                swapChild = rightIndex

            if rootNode.customList[index] < rootNode.customList[swapChild]:
                rootNode.customList[index], rootNode.customList[swapChild] = \
                    rootNode.customList[swapChild], rootNode.customList[index]

    heapifyTreeExtract(rootNode, swapChild, heapType)


# Mengambil data root heap
def extractNode(rootNode, heapType):

    if rootNode.heapSize == 0:
        return

    extractedNode = rootNode.customList[1]

    rootNode.customList[1] = rootNode.customList[rootNode.heapSize]
    rootNode.customList[rootNode.heapSize] = None

    rootNode.heapSize -= 1

    heapifyTreeExtract(rootNode, 1, heapType)

    return extractedNode


# Menghapus seluruh heap
def deleteEntireBP(rootNode):
    rootNode.customList = None


# =====================
# Program Utama
# =====================

newHeap = Heap(5)

# Menambah data
inserNode(newHeap, 4, "Max")
inserNode(newHeap, 5, "Max")
inserNode(newHeap, 2, "Max")
inserNode(newHeap, 1, "Max")

print("Isi Heap:")
levelOrderTraversal(newHeap)

print("\nRoot Heap:", peekofHeap(newHeap))

print("\nJumlah Data:", sizeofHeap(newHeap))

print("\nExtract Root:", extractNode(newHeap, "Max"))

print("\nHeap Setelah Extract:")
levelOrderTraversal(newHeap)

print("\nMenghapus Heap")
deleteEntireBP(newHeap)