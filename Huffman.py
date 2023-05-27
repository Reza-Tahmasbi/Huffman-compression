from collections import defaultdict
from MinHeap import *


def huffman_encoder_decoder(str):
    huffmanTree = Huffman()
    huffmanTree.findFreq(str)
    encodedString = ""
    huffmanTree.HuffmanCodes()
    for char in str:
        encodedString += huffmanTree.codeMap[char]
    decodedString = huffmanTree.decodeFile(huffmanTree.root, encodedString)
    return encodedString, decodedString, huffmanTree.codeMap, huffmanTree.freqMap, huffmanTree.root


class Huffman:
    def __init__(self, codeMap={}, freqMap=None):
        if freqMap is None:
            freqMap = defaultdict(int)
        self.codeMap = codeMap
        self.freqMap = freqMap

    def printCodes(self, root, string):
        if root is None:
            return
        if root.data != '$':
            print(root.data, ":", string)
        self.printCodes(root.left, string + "0")
        self.printCodes(root.right, string + "1")

    def storeCodes(self, root, string):
        if root is None:
            return
        if root.key != '$':
            self.codeMap[root.key] = string
        self.storeCodes(root.left, string + "0")
        self.storeCodes(root.right, string + "1")

    def HuffmanCodes(self):
        global minHeap
        minHeap = MinHeap()
        for key in self.freqMap:
            node = MinHeapNode(key, self.freqMap[key])
            minHeap.insert(node)
        while minHeap.size > 1:
            left = minHeap.extract_min()
            right = minHeap.extract_min()
            top = MinHeapNode('$', left.freq + right.freq)
            top.left = left
            top.right = right
            minHeap.insert(top)

        self.root = minHeap.extract_min()
        self.storeCodes(self.root, "")

    def findFreq(self, string):
        for char in string:
            self.freqMap[char] += 1

    def decodeFile(self, root, string):
        ans = ""
        current = root
        n = len(string)
        for i in range(n):
            if string[i] == '0':
                current = current.left
            else:
                current = current.right

            # reached leaf node
            if current.left is None and current.right is None:
                ans += current.key
                current = root
        return ans
