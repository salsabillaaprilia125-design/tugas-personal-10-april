# Membuat node Trie
class TrieNode:
    def __init__(self):
        self.children = {}          # menyimpan huruf berikutnya
        self.endOfString = False    # penanda akhir kata


# Membuat Trie
class Trie:
    def __init__(self):
        self.root = TrieNode()      # root / akar Trie

    # Menambah kata ke Trie
    def insertString(self, word):
        current = self.root

        for i in word:
            ch = i
            node = current.children.get(ch)

            # Jika huruf belum ada, buat node baru
            if node == None:
                node = TrieNode()
                current.children.update({ch: node})

            current = node

        # Menandai akhir kata
        current.endOfString = True
        print("Successfully inserted")

    # Mencari kata dalam Trie
    def searchString(self, word):
        currentNode = self.root

        for i in word:
            node = currentNode.children.get(i)

            if node == None:
                return False

            currentNode = node

        # Jika sampai akhir kata
        if currentNode.endOfString == True:
            return True
        else:
            return False


# Menghapus kata dari Trie
def deleteString(root, word, index):

    ch = word[index]
    currentNode = root.children.get(ch)

    canThisNodeBeDeleted = False

    # Jika node punya banyak cabang
    if len(currentNode.children) > 1:
        deleteString(currentNode, word, index + 1)
        return False

    # Jika sudah di huruf terakhir
    if index == len(word) - 1:

        if len(currentNode.children) >= 1:
            currentNode.endOfString = False
            return False

        else:
            root.children.pop(ch)
            return True

    # Jika node juga menjadi akhir kata lain
    if currentNode.endOfString == True:
        deleteString(currentNode, word, index + 1)
        return False

    canThisNodeBeDeleted = deleteString(currentNode, word, index + 1)

    if canThisNodeBeDeleted == True:
        root.children.pop(ch)
        return True
    else:
        return False


# =====================
# Program Utama
# =====================

newTrie = Trie()

# Menambah kata
newTrie.insertString("App")
newTrie.insertString("Appl")

# Menghapus kata App
deleteString(newTrie.root, "App", 0)

# Mencari kata App
print(newTrie.searchString("App"))