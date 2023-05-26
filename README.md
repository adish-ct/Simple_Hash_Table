# Simple_Hash_Table

It is a simplest form of Hash Table and it contains basic operations. Included Get, Insert, Remove and also Hash Function


class Hash_Table:
    def __init__(self):
        self.table = [None] * 10

    def hash_key(self, key):
        hash_index = (key * 23) % 10
        return hash_index

    def insert(self, key, value):
        index = self.hash_key(key)
        self.table[index] = [key, value]

    def remove(self, key):
        index = self.hash_key(key)
        self.table[index] = None

    def get(self, key):
        index = self.hash_key(key)
        return self.table[index][1]


table = Hash_Table()
table.insert(12, 100)
table.insert(15, 400)
table.insert(17, 700)

table.remove(17)
print(table.get(12))

print(table.table)
