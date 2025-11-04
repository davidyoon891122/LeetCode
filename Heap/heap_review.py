

class MinHeap:
  
  def __init__(self):
    self.heap = []
  
  def push(self, value):
    self.heap.append(value)
    self._heapify_up(len(self.heap) - 1)
    
  def _heapify_up(self, index):
    parent = index * 1 // 2
    
    if index > 0 and self.heap[index] < self.heap[parent]:
      self.heap[parent], self.heap[index] = self.heap[index], self.heap[parent]
      self._heapify_up(parent)
  
  def pop(self):
    if self.heap is None:
      return None
    if len(self.heap) == 1:
      return self.heap.pop()
    
    root = self.heap[0]
    self.heap[0] = self.heap.pop()
    self._heapify_down(0)
    
    return root
  
  def _heapify_down(self, index):
    left = index * 2 + 1
    right = index * 2 + 2
    smallest = index 
    
    if left < len(self.heap) and self.heap[left] < self.heap[smallest]:
      smallest = left
    if right < len(self.heap) and self.heap[right] < self.heap[smallest]:
      smallest = right
      
    if smallest != index:
      self.heap[index], self.heap[smallest] = self.heap[smallest], self.heap[index]
      self._heapify_down(smallest)
    
  def peak(self):
    return self.heap[0] if self.heap else None
  
  

h = MinHeap()
for num in [5, 3, 8, 1, 2]:
    h.push(num)

print(h.heap)     # [1, 2, 8, 5, 3] (힙 형태)
print(h.pop())    # 1
print(h.heap)     # [2, 3, 8, 5]
print(h.pop())    # 2
print(h.heap)     # [3, 8, 5]
print(h.pop())    # 3
print(h.heap)     # [8, 5]
print(h.pop())    # 8
print(h.heap)     # [5]