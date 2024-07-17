#Implement a Python class MaxHeap that supports the following operations: insert, delete, and get_max. Ensure the operations maintain the properties of a max-heap.
class MaxHeap:
    def __init__(self):
        self.heap = []

    def insert(self, value):
        self.heap.append(value)
        self._sift_up(len(self.heap) - 1)

    def delete(self):
        if len(self.heap) == 0:
            return None
        if len(self.heap) == 1:
            return self.heap.pop()

        max_value = self.heap[0]
        self.heap[0] = self.heap.pop()
        self._sift_down(0)
        return max_value

    def get_max(self):
        if self.heap:
            return self.heap[0]
        return None

    def _sift_up(self, index):
        parent_index = (index - 1) // 2
        if parent_index >= 0 and self.heap[index] > self.heap[parent_index]:
            self.heap[index], self.heap[parent_index] = self.heap[parent_index], self.heap[index]
            self._sift_up(parent_index)

    def _sift_down(self, index):
        left_child_index = 2 * index + 1
        right_child_index = 2 * index + 2
        largest = index

        if (left_child_index < len(self.heap) and 
            self.heap[left_child_index] > self.heap[largest]):
            largest = left_child_index

        if (right_child_index < len(self.heap) and 
            self.heap[right_child_index] > self.heap[largest]):
            largest = right_child_index

        if largest != index:
            self.heap[index], self.heap[largest] = self.heap[largest], self.heap[index]
            self._sift_down(largest)

# Example usage:
heap = MaxHeap()
heap.insert(10)
heap.insert(20)
heap.insert(5)
heap.insert(30)
print(heap.get_max())  
print(heap.delete())   
print(heap.get_max())
    
