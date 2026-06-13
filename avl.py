import QueueLinkedList as queue

# Membuat node AVL Tree
class AVLNode:
    def __init__(self, data):
        self.data = data
        self.leftChild = None
        self.rightChild = None
        self.height = 1


# Traversal PreOrder
def preOrderTraversal(rootNode):
    if not rootNode:
        return
    print(rootNode.data)
    preOrderTraversal(rootNode.leftChild)
    preOrderTraversal(rootNode.rightChild)


# Traversal InOrder
def inOrderTraversal(rootNode):
    if not rootNode:
        return
    inOrderTraversal(rootNode.leftChild)
    print(rootNode.data)
    inOrderTraversal(rootNode.rightChild)


# Traversal PostOrder
def postOrderTraversal(rootNode):
    if not rootNode:
        return
    postOrderTraversal(rootNode.leftChild)
    postOrderTraversal(rootNode.rightChild)
    print(rootNode.data)


# Traversal Level Order
def levelOrderTraversal(rootNode):
    if not rootNode:
        return

    customQueue = queue.Queue()
    customQueue.enqueue(rootNode)

    while not customQueue.isEmpty():
        root = customQueue.dequeue()

        print(root.data)

        if root.leftChild is not None:
            customQueue.enqueue(root.leftChild)

        if root.rightChild is not None:
            customQueue.enqueue(root.rightChild)


# Mencari data
def searchNode(rootNode, nodeValue):
    if rootNode is None:
        print("Data tidak ditemukan")
        return

    if rootNode.data == nodeValue:
        print("Data ditemukan")
    elif nodeValue < rootNode.data:
        searchNode(rootNode.leftChild, nodeValue)
    else:
        searchNode(rootNode.rightChild, nodeValue)


# Mengambil tinggi node
def getHeight(rootNode):
    if not rootNode:
        return 0
    return rootNode.height


# Rotasi kanan
def rightRotate(disbalanceNode):
    newRoot = disbalanceNode.leftChild
    disbalanceNode.leftChild = newRoot.rightChild
    newRoot.rightChild = disbalanceNode

    disbalanceNode.height = 1 + max(
        getHeight(disbalanceNode.leftChild),
        getHeight(disbalanceNode.rightChild)
    )

    newRoot.height = 1 + max(
        getHeight(newRoot.leftChild),
        getHeight(newRoot.rightChild)
    )

    return newRoot


# Rotasi kiri
def leftRotate(disbalanceNode):
    newRoot = disbalanceNode.rightChild
    disbalanceNode.rightChild = newRoot.leftChild
    newRoot.leftChild = disbalanceNode

    disbalanceNode.height = 1 + max(
        getHeight(disbalanceNode.leftChild),
        getHeight(disbalanceNode.rightChild)
    )

    newRoot.height = 1 + max(
        getHeight(newRoot.leftChild),
        getHeight(newRoot.rightChild)
    )

    return newRoot


# Menghitung balance factor
def getBalance(rootNode):
    if not rootNode:
        return 0
    return getHeight(rootNode.leftChild) - getHeight(rootNode.rightChild)


# Menambah node
def insertNode(rootNode, nodeValue):
    if not rootNode:
        return AVLNode(nodeValue)

    if nodeValue < rootNode.data:
        rootNode.leftChild = insertNode(rootNode.leftChild, nodeValue)
    else:
        rootNode.rightChild = insertNode(rootNode.rightChild, nodeValue)

    rootNode.height = 1 + max(
        getHeight(rootNode.leftChild),
        getHeight(rootNode.rightChild)
    )

    balance = getBalance(rootNode)

    # LL
    if balance > 1 and nodeValue < rootNode.leftChild.data:
        return rightRotate(rootNode)

    # LR
    if balance > 1 and nodeValue > rootNode.leftChild.data:
        rootNode.leftChild = leftRotate(rootNode.leftChild)
        return rightRotate(rootNode)

    # RR
    if balance < -1 and nodeValue > rootNode.rightChild.data:
        return leftRotate(rootNode)

    # RL
    if balance < -1 and nodeValue < rootNode.rightChild.data:
        rootNode.rightChild = rightRotate(rootNode.rightChild)
        return leftRotate(rootNode)

    return rootNode


# Menghapus seluruh AVL
def deleteAVL(rootNode):
    rootNode.data = None
    rootNode.leftChild = None
    rootNode.rightChild = None
    return "AVL berhasil dihapus"


# =====================
# Program Utama
# =====================

newAVL = AVLNode(5)

newAVL = insertNode(newAVL, 10)
newAVL = insertNode(newAVL, 15)
newAVL = insertNode(newAVL, 20)

print("Level Order Traversal:")
levelOrderTraversal(newAVL)

print("\nMencari data 15:")
searchNode(newAVL, 15)

print("\nMenghapus AVL:")
print(deleteAVL(newAVL))