class HashTable:
    def __init__(self,capacity = 31):
        self.data = [None] * capacity
        self.capacity = capacity
    
    def _hash(self,key):
        return hash(key) % self.capacity
    
    def insert(self,key,value):
        index = self._hash(key)
        if self.data[index] is None:
            self.data[index] = []
        else:
            for i,val in enumerate(self.data[index]):
                if val[0] == key:
                    return False
        self.data[index].append([key,value])
    
    def get_item_by_key(self,key):
        index = self._hash(key)
        if self.data[index]:
            for item in self.data[index]:
                k =  item[0]
                if k == key:
                    return item[1]
        return None

    def contains(self,key):
        return self.get_item_by_key(key=key) != None
    
    def get_keys(self):
        all_keys = []
        for item in self.data:
            if item:
                for k in item:
                    all_keys.append(k[0])
        return all_keys            
    
ht = HashTable()
ht.insert("dada","aaaaa3232")
ht.insert("da3da","3232")
ht.insert("da2da","3232")
ht.insert("da1da","3232")
ht.insert("daeda","3232")
ht.insert("dada","323dasda2")
print(ht.contains("da2da"))
#print (ht.get_keys())