class HashTable:
    def __init__(self,size = 63):
        self.size = size
        self.data = [None] * size   
    def __hash(self,key):
        return hash(key) % self.size
    
    def insert(self,key,value):
        index = self.__hash(key=key)
        if self.data[index] is None:
            self.data[index] = []
        elif self.data[index][0] == key:
            return False
        self.data[index].append([key,value])
    
    def get_keys(self):
        arr = []
        for items in self.data:
            if items is None:
                continue
            for k in range(len(items)):
                arr.append(items[k][0])
        return arr

    def get_values(self):
        arr = []
        for items in self.data:
            if items is None:
                continue
            for k in range(len(items)):
                arr.append(items[k][1])
        return arr

    def get_item(self,key):
        index = self.__hash(key)
        if self.data[index] is None:
            return False
        for item in self.data[index]:
            if item[0] == key:
                return item[1]
        return False

    def print_table(self,show_none=False):
      for i,val in enumerate(self.data):
        if val:
            print (i, ": " ,val)
        elif show_none:
            print (i, ": " ,val)

ht = HashTable()
ht.insert("a","baaaaaa")
ht.insert("9", "u")
ht.insert("9", "ad")
ht.insert("dasd","89")
print("item: ",ht.get_item("9"))
print(ht.get_values())
ht.print_table()