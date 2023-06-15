from collections import defaultdict
import cv2
import numpy as np

from MinHeap import *


def huffman_encoder_decoder(string):
    huffmanTree = Huffman(code_map=None, freq_map=None)
    isParagraph = huffmanTree.findFreq(string)
    encodedString = ""
    huffmanTree.HuffmanCodes()
    if not isParagraph:
        for char in string:
            encodedString += huffmanTree.code_map[char]
    else:
        for word in string.lower().split():
            encodedString += huffmanTree.code_map[word]
    decodedString = decodeString(huffmanTree.root, encodedString)
    return encodedString, decodedString, huffmanTree.code_map, huffmanTree.freq_map, huffmanTree.root, isParagraph

def save_string_to_file(string, filename):
    with open(filename, 'w') as file:
        file.write(string)

def encode_image(image_path):
    image = cv2.imread(image_path)
    print(image)
    image_array = np.array(image)
    print(image_array.shape)
    huffmanTree = Huffman(code_map=None, freq_map=None)
    huffmanTree.findFreqImg(image_array)
    encodedString = ""
    huffmanTree.HuffmanCodes()
    # encode
    encoded_array = np.empty_like(image_array, dtype=object)
    for idx, digit in np.ndenumerate(image_array):
        encoded_array[idx] = huffmanTree.code_map[str(digit)]
        # encodedString += huffmanTree.code_map[str(digit)]
    # decode
    decoded_array = np.empty_like(encoded_array)
    for idx, code in np.ndenumerate(encoded_array):
        decoded_array[idx] = decodeString(huffmanTree.root, code)
    # decodedString = decodeString(huffmanTree.root, encodedString)
    decoded_array = decoded_array.astype(np.uint8)
    cv2.imwrite('saved_image/image2.jpg', decoded_array) # saves decoded image as jpg
    cv2.imwrite('saved_image/image23.jpg', encoded_array.astype(np.uint8)) # saves encoded image as jpg
    np.save("output", encoded_array) # save encoded image in a textfile
    encoded_array = encoded_array.astype(int)
    flattened_array = encoded_array.reshape(-1, encoded_array.shape[-1])

    # Save the flattened array to a text file
    np.savetxt("output.txt", flattened_array, delimiter=',',  fmt='%d')
    return encoded_array, decoded_array, huffmanTree.code_map, huffmanTree.freq_map, huffmanTree.root


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
        if len(string) < 200:
            for char in string:
                self.freq_map[char] += 1
            return False
        else:
            words = string.lower().split()
            for word in words:
                self.freq_map[word] += 1
            return True

    def findFreqImg(self, array):
        for number in np.nditer(array):
            self.freq_map[str(number)] += 1
        print(self.freq_map)
