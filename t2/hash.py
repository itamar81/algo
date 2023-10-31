class HashTable:
    def __init__(self,capacity = 64):
        self.capacity = capacity
        self.size = 0
        self.data = [None] * capacity
    
    def _hash(self,key):
        return hash(key) % self.capacity
    
    def insert(self,key,value):
        index = self._hash(key)    
        if self.data[index] is None:
            self.data[index] = []
        for i,n in enumerate(self.data[index]):
            if n[0] == key:
                n[1] = value
                return
        self.data[index].append([key,value])

    def search(self,key):
        index = self._hash(key)    
        if self.data[index] is None:
            return None
        for i, n in enumerate(self.data[index]):
            k = n[0]
            if k == key:
                return n[1]
        return None
    
ht = HashTable()
ht.insert("ds1a","aaaa")
ht.insert("ds12a","aaaaaa")
ht.insert("ds23a","aaaaaa")
ht.insert("dsa4","awaaaaa")
ht.insert("dsa4a","22aaasaaa")
ht.insert("dsa4a","111aaasaaa")
print(ht.search("dsa4a"))