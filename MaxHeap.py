class MaxHeap:
    def __init__(self):
        self.heap = []

    def insert(self, val):
        self.heap.append(val)
        self._heapify_up(len(self.heap) - 1)

    def delete(self, val):
        if len(self.heap) == 0:
            raise IndexError("Cannot delete from empty heap")
        
        idx = self.heap.index(val)
        if idx == -1:
            raise ValueError(f"{val} not found in heap")

        last_elem = self.heap.pop()
        if idx < len(self.heap):
            self.heap[idx] = last_elem
            self._heapify_down(idx)

    def get_max(self):
        if len(self.heap) == 0:
            raise IndexError("Heap is empty")
        return self.heap[0]

    def _heapify_up(self, idx):
        parent_idx = (idx - 1) // 2
        while idx > 0 and self.heap[idx] > self.heap[parent_idx]:
            # Swap current node with its parent
            self.heap[idx], self.heap[parent_idx] = self.heap[parent_idx], self.heap[idx]
            idx = parent_idx
            parent_idx = (idx - 1) // 2

    def _heapify_down(self, idx):
        left_child_idx = 2 * idx + 1
        right_child_idx = 2 * idx + 2
        largest_idx = idx
        
        # Compare with left child
        if left_child_idx < len(self.heap) and self.heap[left_child_idx] > self.heap[largest_idx]:
            largest_idx = left_child_idx
        
        # Compare with right child
        if right_child_idx < len(self.heap) and self.heap[right_child_idx] > self.heap[largest_idx]:
            largest_idx = right_child_idx
        
        # If the largest node is not the current node, swap and heapify down
        if largest_idx != idx:
            self.heap[idx], self.heap[largest_idx] = self.heap[largest_idx], self.heap[idx]
            self._heapify_down(largest_idx)
# Example usage
heap = MaxHeap()
heap.insert(5)
heap.insert(3)
heap.insert(8)
heap.insert(1)

print("Max element:", heap.get_max())  # Output: 8

heap.delete(8)
print("Max element after deletion:", heap.get_max())  # Output: 5