#ifndef MINHEAP
#define MINHEAP
#include <vector>
#include <map>
template <typename T>
class MinHeap {
private:
    //a vector with functions:
    // front:first element
    // back: last element
    // push_back: add to the end of vector
    // pop_back : remove from the end of venctor
    // size: size of heap tree(vector)
    // empty: check if heap(vector) is empty
    
    std::vector<T> heap;
    // the heapify-up algorithm, moves the new inserted element up to the right place
    void heapifyUp(int index) {
        int parent = (index - 1) / 2;
        while (index > 0 && heap[index].second < heap[parent].second) {
            std::swap(heap[index], heap[parent]);
            index = parent;
            parent = (index - 1) / 2;
        }
    }
    // the heapify-down algorithm, after removing root, moves down the swapped element to restore heap property
    void heapifyDown(int index) {
        int left = 2 * index + 1;
        int right = 2 * index + 2;
        int smallest = index;

        if (left < heap.size() && heap[left].second < heap[smallest].second) {
            smallest = left;
        }

        if (right < heap.size() && heap[right].second < heap[smallest].second) {
            smallest = right;
        }

        if (smallest != index) {
            std::swap(heap[index], heap[smallest]);
            heapifyDown(smallest);
        }
    }

public:
    bool empty() const {
        return heap.empty();
    }

    int size() const {
        return heap.size();
    }

    const T& top() const {
        return heap.front();
    }

    void push(std::pair pair) {
        heap.push_back(pair);
        heapifyUp(heap.size() - 1);
    }

    void pop() {
        if (!empty()) {
            std::swap(heap.front(), heap.back());
            heap.pop_back();
            heapifyDown(0);
        }
    }
};
#endif