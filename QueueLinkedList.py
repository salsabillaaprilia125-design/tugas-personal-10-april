# Membuat node untuk menyimpan data
class Node:
    def __init__(self, value=None):
        self.value = value
        self.next = None

    def __str__(self):
        return str(self.value)


# Membuat Linked List
class LinkedList:
    def __init__(self):
        self.head = None
        self.tail = None


# Membuat Queue menggunakan Linked List
class Queue:
    def __init__(self):
        self.linkedList = LinkedList()

    # Menambah data ke belakang queue
    def enqueue(self, value):
        newNode = Node(value)

        # Jika queue masih kosong
        if self.linkedList.head is None:
            self.linkedList.head = newNode
            self.linkedList.tail = newNode
        else:
            # Sambungkan node baru ke belakang
            self.linkedList.tail.next = newNode
            self.linkedList.tail = newNode

    # Mengecek apakah queue kosong
    def isEmpty(self):
        return self.linkedList.head is None

    # Menghapus data paling depan (FIFO)
    def dequeue(self):
        if self.isEmpty():
            return "Queue kosong"

        tempNode = self.linkedList.head

        # Jika hanya ada 1 node
        if self.linkedList.head == self.linkedList.tail:
            self.linkedList.head = None
            self.linkedList.tail = None
        else:
            self.linkedList.head = self.linkedList.head.next

        return tempNode.value

    # Melihat data paling depan
    def peek(self):
        if self.isEmpty():
            return "Queue kosong"
        return self.linkedList.head.value

    # Menghapus seluruh queue
    def delete(self):
        self.linkedList.head = None
        self.linkedList.tail = None


# ======================
# Program Utama
# ======================

custQueue = Queue()

custQueue.enqueue(1)
custQueue.enqueue(2)
custQueue.enqueue(3)

print("Data depan :", custQueue.peek())

print("Hapus data :", custQueue.dequeue())

print("Data depan sekarang :", custQueue.peek())