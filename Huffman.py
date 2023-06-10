from collections import defaultdict
from MinHeap import *


def huffman_encoder_decoder(string):
    huffmanTree = Huffman(code_map=None, freq_map=None)
    huffmanTree.findFreq(string)
    encodedString = ""
    huffmanTree.HuffmanCodes()
    for char in string:
        encodedString += huffmanTree.code_map[char]
    decodedString = decodeString(huffmanTree.root, encodedString)
    return encodedString, decodedString, huffmanTree.code_map, huffmanTree.freq_map, huffmanTree.root


class Huffman:
    def __init__(self, code_map=None, freq_map=None):
        self.root = None
        if code_map is None:
            code_map = {}
        if freq_map is None:
            freq_map = defaultdict(int)
        self.code_map = code_map
        self.freq_map = freq_map

    def printNodes(self, root, string):
        if root is None:
            return
        if root.data != '$':
            print(root.data, ":", string)
        self.printNodes(root.left, string + "0")
        self.printNodes(root.right, string + "1")

    def saveBinary(self, root, string):
        if root is None:
            return
        if root.key != '$':
            self.code_map[root.key] = string
        else:
            self.saveBinary(root.left, string + "0")
            self.saveBinary(root.right, string + "1")

    def HuffmanCodes(self):
        minHeap = MinHeap()
        for key in self.freq_map:
            node = MinHeapNode(key, self.freq_map[key])
            minHeap.insert(node)
        while minHeap.size > 1:
            left = minHeap.extract_min()
            right = minHeap.extract_min()
            top = MinHeapNode('$', left.freq + right.freq)
            top.left = left
            top.right = right
            minHeap.insert(top)
        self.root = minHeap.extract_min()
        self.saveBinary(self.root, "")
        if self.root.left is None and self.root.right is None:
            self.code_map[self.root.key] = "0"

    def findFreq(self, string):
        for char in string:
            self.freq_map[char] += 1

def decodeString(root, string):
    result_str = ""
    currentNode = root
    n = len(string)
    for i in range(n):
        if string[i] == '0':
            currentNode = currentNode.left
        else:
            currentNode = currentNode.right

        # reached leaf node
        if currentNode.left is None and currentNode.right is None:
            result_str += currentNode.key
            currentNode = root
    return result_str