"""
Design a HashMap without using any built-in hash table libraries.

Implement the MyHashMap class:

MyHashMap() initializes the object with an empty map.
void put(int key, int value) inserts a (key, value) pair into the HashMap. If the key already exists in the map, update the corresponding value.
int get(int key) returns the value to which the specified key is mapped, or -1 if this map contains no mapping for the key.
void remove(key) removes the key and its corresponding value if the map contains the mapping for the key.
"""
import collections

class ListNode:
  
  def __init__(self, key=None, value=None):
    self.key = key 
    self.value = value
    self.next = None

class MyHashMap:

    def __init__(self):
      self.size = 1000
      self.table = [None] * self.size
      
    def put(self, key: int, value: int) -> None:
      index = key % self.size
      
      if self.table[index] is None:
        self.table[index] = ListNode(key, value)
        return
      
      p = self.table[index]
      
      while p:
        if p.key == key:
          p.value = value
          return
        if p.next is None:
          break
        p = p.next 
      p.next = ListNode(key, value)
      
      
    def get(self, key: int) -> int:
      index = key % self.size
      
      p = self.table[index]
      
      while p:
        if p.key == key:
          return p.value
        p = p.next
      
      return -1
    
    def remove(self, key: int) -> None:
      index = key % self.size
      
      p = self.table[index]
      
      prev = None
      
      while p:
        if p.key == key:
          if prev:
            prev.next = p.next
          else:
            self.table[index] = p.next
          return
        prev, p = p, p.next
      
    

# Your MyHashMap object will be instantiated and called as such:
# obj = MyHashMap()
# obj.put(key,value)
# param_2 = obj.get(key)
# obj.remove(key)