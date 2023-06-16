# define min-heap node class
class MinHeapNode:
    def __init__(self, key, freq):
        self.key = key
        self.freq = freq
        self.left = None
        self.right = None

    # def __lt__(self, other):
    #     if self.freq == other.freq:
    #         return self.key < other.key
    #     return self.freq < other.freq


# define min-heap class
class MinHeap:
    def __init__(self):
        self.heap = []
        self.size = 0

    def parent(self, i):
        return (i - 1) // 2

    def left_child(self, i):
        return 2 * i + 1

    def right_child(self, i):
        return 2 * i + 2
    

    # insert a new node to min-heap tree
    def insert(self, node):
        self.heap.append(node)
        self.size += 1
        i = self.size - 1
        parent = self.parent(i)
        # sorting min-heap nodes with order of logn
        while i != 0 and self.heap[parent].freq > self.heap[i].freq:
            self.heap[i], self.heap[parent] = self.heap[parent], self.heap[i]
            i = parent

    # extract the root node(smallest value)
    def extract_min(self):
        if self.size == 0:
            return None

        if self.size == 1:
            self.size -= 1
            return self.heap.pop()

        root = self.heap[0]
        self.heap[0] = self.heap.pop()
        self.size -= 1
        self.min_heapify(0)
        return root
    

    # min-heapify algorithm from notebook, nlogn
    def min_heapify(self, i):
        smallest = i
        left = self.left_child(i)
        right = self.right_child(i)

        if left < self.size and self.heap[left].freq < self.heap[smallest].freq:
            smallest = left

        if right < self.size and self.heap[right].freq < self.heap[smallest].freq:
            smallest = right

        if smallest != i:
            self.heap[i], self.heap[smallest] = self.heap[smallest], self.heap[i]
            self.min_heapify(smallest)
