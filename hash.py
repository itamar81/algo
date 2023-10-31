

class Node:
  def __init__(self,key,value):
    self.value = value


class HashTable:
  def __init__(self,size = 63):
    self.data_map = [None] * size 
    self.size = size    
  def __hash(self,key):
    return hash(key) % self.size
  # hashsum =0
  #for idx , c in enumerate(key):
  #  hashsum += (idx + len(key)) ** ord(c)
  # hashsum = hashsum %self.capacity
  #return hashsum
  
  def print_table(self):
    for i,val in enumerate(self.data_map):
     # self.data_map[i] = hash(i)
      print (i, ": " ,val)

  def set_item(self,key,value):
    hash = self.__hash(key)
    if self.data_map[hash] is None:
      self.data_map[hash] = []
    self.data_map[hash].append([key,value])

  def get_item(self,key):
    hash = self.__hash(key)
    if self.data_map[hash]:
      for i in range(len(self.data_map[hash])):
        if self.data_map[hash][i][0] == key:
          return self.data_map[hash][i][1]
    return None 
  
  def get_keys(self):
    all_keys = []
    for i in range(len(self.data_map)):
      if self.data_map[i] is not None:
        for j in range(len(self.data_map[i])):
          all_keys.append(self.data_map[i][j][0])
    return all_keys
ht = HashTable(10)
ht.set_item("key2","val")
ht.set_item("key","val")
ht.set_item("keyf","val2")
print(ht.get_item("keyf"))
ht.print_table()
print(ht.get_keys())
