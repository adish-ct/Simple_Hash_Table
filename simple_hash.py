
class Hash_Table:
    def __init__(self):
        self.table = [None] * 10

    def generate_key(self, key):
        key_value = 0
        for i in key:
            key_value = key_value + ord(i)
        return key_value

    def hash_key(self, key):
        key_value = generate_key(key)
        hash_index = (key_value * 23) % 10
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
