#include "MinHeap.cpp"
#include <iostream>
#include <map>
int main() {
    MinHeap<std::pair<char, int>> minHeap;

    // while (!minHeap.empty()) {
    //     std::cout << minHeap.top() << " ";
    //     minHeap.pop();
    // }
    // std::cout << std::endl;

    return 0;
}

std::map<char, int> buildDictionary(std::string& input){
    std::map<char, int> frequencyMap;
    // Count the frequency of each character in the input string
    for (char ch : input) {
        frequencyMap[ch]++;
    }
    return frequencyMap;
}

MinHeap<std::pair<char, int>> buildHeapFromDictionaary(std::map<char, int> frequencyMap){
    MinHeap<std::pair<char, int>> minHeap;
    // Count the frequency of each character in the input string
    for (auto& pair: frequencyMap) {
        minHeap.push(pair);
    }
    return minHeap;
}
